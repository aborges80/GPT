"""Biot-Savart free-space comparison: cone versus square pyramid.

Exploratory, not FEM. No rotor, magnetic steel, torque or efficiency.
Both shapes use 3 idealized closed loops at equal peak phase current (5 A).
Conductor lengths differ, so this is NOT an equal-copper or equal-loss test.
"""
import numpy as np
import csv
from pathlib import Path

MU0 = 4e-7 * np.pi
BASE_HALF = 0.072
HEIGHT = 0.233
ROTOR_R = 0.028
CURRENT = 5.0
PHASES = np.array([0, 2*np.pi/3, 4*np.pi/3])

def radial_boundary(phi, shape):
    if shape == "cone":
        return BASE_HALF
    if shape == "pyramid":
        return BASE_HALF / max(abs(np.cos(phi)), abs(np.sin(phi)))
    raise ValueError(shape)

def loop(phi, shape):
    phi0, phi1 = phi - 0.22, phi + 0.22
    path = (
        [(z, phi0) for z in np.linspace(.025, .205, 41)]
        + [(.205, ph) for ph in np.linspace(phi0, phi1, 41)]
        + [(z, phi1) for z in np.linspace(.205, .025, 41)]
        + [(.025, ph) for ph in np.linspace(phi1, phi0, 41)]
    )
    points = []
    for z, ph in path:
        r = radial_boundary(ph, shape) * (1-z/HEIGHT)
        points.append([r*np.cos(ph), r*np.sin(ph), z])
    return np.array(points)

def field(points, wire):
    ends = np.roll(wire, -1, axis=0)
    dl = ends-wire
    mid = (ends+wire)/2
    dr = points[:, None, :] - mid[None, :, :]
    norm = np.linalg.norm(dr, axis=2)
    if np.any(norm < 1e-10):
        raise ValueError("Sampling point on conductor")
    return MU0/(4*np.pi) * np.sum(np.cross(dl[None,:,:], dr)/norm[:,:,None]**3, axis=1)

def run(shape, nr=80, nz=16):
    loops = [loop(p, shape) for p in PHASES]
    lengths = [np.linalg.norm(np.roll(w,-1,axis=0)-w, axis=1).sum() for w in loops]
    angles = np.linspace(0,2*np.pi,nr,endpoint=False)
    heights = np.linspace(.055,.105,nz)
    pts = np.array([[ROTOR_R*np.cos(a), ROTOR_R*np.sin(a), z] for z in heights for a in angles])
    bphase = np.stack([field(pts,w) for w in loops])
    tangents = np.array([[-np.sin(a),np.cos(a),0] for z in heights for a in angles])
    mean_b2, mean_bt2, peaks = [], [], []
    for t in np.linspace(0,2*np.pi,36,endpoint=False):
        amps = CURRENT*np.cos(t-PHASES)
        b = np.einsum("p,pni->ni", amps, bphase)
        mean_b2.append(np.mean(np.sum(b*b,axis=1)))
        mean_bt2.append(np.mean(np.sum(b*tangents,axis=1)**2))
        peaks.append(np.max(np.linalg.norm(b,axis=1)))
    return {
        "shape": shape,
        "wire_length_m": float(sum(lengths)),
        "field_rms_mT": float(1e3*np.sqrt(np.mean(mean_b2))),
        "field_peak_mT": float(1e3*max(peaks)),
        "tangential_field_rms_mT": float(1e3*np.sqrt(np.mean(mean_bt2))),
    }

if __name__ == "__main__":
    results = [run(s) for s in ("cone", "pyramid")]
    with (Path(__file__).parent/"results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)
    for result in results:
        print(result)
    print("No torque/efficiency conclusions: no rotor, no steel, unequal copper lengths.")
