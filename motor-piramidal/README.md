# Motor Piramidal — avaliação física independente de Fibonacci

Projeto exploratório. Objetivo: verificar se a geometria piramidal produz vantagens **mensuráveis** sobre a geometria cônica/cilíndrica.

## Estado atual
- Primeiro ensaio executado localmente: integração numérica da lei de Biot–Savart para três bobinas de corrente alternada, sem ferro e sem rotor.
- Não há ainda cálculo de torque, rendimento, perdas no ferro, saturação ou FEM 3D.
- **Nenhuma vantagem da pirâmide foi demonstrada.**

## Resultado do ensaio inicial (5 A de pico por fase)
| Métrica | Cone | Pirâmide |
| --- | ---: | ---: |
| Comprimento de condutores (m) | 1.22665 | 1.26753 |
| Campo RMS na região interna (mT) | 0.02889 | 0.02381 |
| Campo tangencial RMS (mT) | 0.02035 | 0.01675 |

As correntes são iguais, mas o comprimento de cobre não é. Esses valores são sensíveis à distribuição escolhida das bobinas e **não são estimativas de torque ou eficiência**.

## Execução
```bash
python -m pip install numpy
python motor-piramidal/simulate.py
```

## Próximas etapas para uma conclusão de engenharia
1. Geometrias sólidas fechadas e entreferro válido em toda a rotação.
2. Malha 3D (Gmsh) e solução magnetostática (Elmer FEM), com aço elétrico e curva B-H.
3. Validação de malha, condições de contorno e comparação com caso analítico.
4. Rotor em várias posições; torque por tensor de Maxwell/energia virtual.
5. Comparação de torque por corrente, volume, massa e perdas com mesma restrição térmica.
6. Só depois avaliar rendimento e viabilidade do protótipo.

**Nota:** repositório GPT é público. Este projeto não deve conter informações confidenciais de patente.
