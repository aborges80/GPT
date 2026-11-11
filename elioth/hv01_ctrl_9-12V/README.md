# ELIOTH HV01 — PCB de controle de 9 a 12 V (REV 0.1)

**Dimensões:** 100 × 75 mm, FR-4 1,6 mm, 2 camadas; montagem THT com quatro furos M3.2.

**IMPORTANTE:** projeto experimental, **não liberado para fabricação ou energização**. Os arquivos nativos KiCad foram gerados programaticamente; não houve ERC/DRC validado em uma instalação do KiCad nem simulação elétrica executada. O roteamento automático preliminar apresenta 0 rede(s) com terminais não conectados: nenhuma no algoritmo; possíveis interferências físicas, conexões e trilhas inadequadas ainda podem ser identificadas pelo DRC.

## Escopo elétrico

Placa contém TLC555CP (R1 2k2, R2 2k2, P1 22k externo, C1 680 pF), driver TC4420CPA e MOSFET IRLZ44N. O gerador **teórico** opera aproximadamente de 42 a 320 kHz, dependendo de tolerâncias, carga e circuito real. A tensão primária vem de um **módulo BUCK externo** com regulagem própria, conectado por J2. Não há ajuste nem medição real da tensão HV nesta PCB. A fonte de alimentação 9–12 V tem de ser limitada em corrente.

O ponto **J5** contém exclusivamente **dois fios de baixa tensão do primário externo**: VP e SW. O transformador/resonador secundário, enrolamento de excitação no dispositivo e terminal de alta tensão **NÃO** devem ser ligados a nenhuma ilha de cobre desta PCB. Não especificamos 1/5/10 kV sem identificar, medir e modelar o magnético, a ressonância e as capacitâncias de acoplamento.

## Ligações externas

| Conector | Pinagem |
|---|---|
| J1 | 1 VIN +9–12 V; 2 GND |
| J2 | 1 VCC (entrada do buck); 2 GND; 3 VADJ (saída buck); 4 GND |
| J3 | potenciômetro 22k: 1 FREQ_A; 2 cursor TIMING; 3 extremidade TIMING |
| J4 | contato NC entre VCC e RESET; aberto = bloqueio do TLC555 |
| J5 | 1 VP (+ primário externo, via F2); 2 SW (MOSFET, saída de comutação LV) |
| J6 | 1 VCC; 2 PWM; 3 GND |
| J7 | 1 SOURCE; 2 GND (shunt RS1) |

## Antes de fabricar

1. Conferir no KiCad simbologia, footprint real, polaridade, intertravamento e DRC/ERC; observar que F1/F2 são **PTC de recuperação lenta**, não disjuntores e não protegem contra sobrecorrentes de comutação rápidas.
2. Resolver todos os erros, redes abertas, distâncias e áreas termicamente insuficientes. Validar o circuito de proteção de sobrecorrente e falha de driver; o protótipo atual **não contém desligamento eletrônico instantâneo por sobrecorrente**.
3. Confirmar com datasheet o MOSFET, driver, dissipação do resistor shunt, resposta do TVS e eventuais picos de VDS.
4. Determinar material, espiras, Ae, AL, auto-ressonância, perdas e isolamento de T1, com ensaios de baixa energia. Evitar repetir pressão de 1–2 bar em tubo PVC não certificado.
5. Medição de alta tensão/alta frequência apenas por profissional e instrumentos/sistemas apropriados.

## Dados de verificação

- `ELIOTH_HV01_CTRL.kicad_sch` — esquemático nativo com símbolos embutidos e etiquetas de redes.
- `ELIOTH_HV01_CTRL.kicad_pcb` — PCB de 100 × 75 mm com pads e roteamento inicial.
- `ELIOTH_HV01_CTRL.kicad_pro` — projeto.
- `BOM.csv`, `NETLIST.csv` e `ROTEAMENTO.csv` — auditoria legível.

**Não há arquivos Gerber de fabricação nesta revisão.**
