# ELIOTH HV01 — Interface com a mini Tesla e com o enrolamento externo

## O que esta placa realmente entrega
A PCB de 100 × 75 mm trabalha **exclusivamente em baixa tensão**. Entrada J1: fonte de 9–12 Vcc com corrente limitada. Oscilador TLC555 e driver TC4420 com MOSFET de chaveamento; J2 recebe um **conversor buck AJUSTÁVEL externo** para variar a tensão aplicada ao primário. J3 recebe potenciômetro externo de 22 kΩ para variar a frequência nominal do TLC555. J4 intertravamento NC.

A saída J5 **não é saída de 5 kV**:
- **J5.1 (VP)**: alimentação ajustável e protegida por F2 para uma extremidade do **primário de T1 externo**.
- **J5.2 (SW)**: segunda extremidade do **primário de T1 externo**, comutada pelo dreno do MOSFET Q1.

Nenhuma trilha ou terminal desta PCB transporta a alta tensão do secundário.

## Cabeçote externo T1: pendente de dimensionamento
```text
    J5.1 VP ----[ PRIMÁRIO T1 ]---- J5.2 SW
                           ||  acoplamento ressonante / HF
                       [ SECUNDÁRIO ]
                             |
                    TERMINAL HV_RF (FORA DA PCB)
                             |
               Acoplador / enrolamento EXTERNO no dispositivo
                  (sem contato galvânico com o gás)
```

O esquema é **funcional**; não define a quantidade de terminais do secundário, referencia de retorno, isolamento, conexão galvânica entre primário/secundário, sintonia nem tensão obtida. Em uma mini Tesla com oscilador de um transistor, o secundário **pode ter referência elétrica diferente** de um transformador galvanicamente isolado. Não unir nenhuma dessas referências até caracterizar o módulo original.

**Extremidade externa não conectada**: uma ponta do enrolamento aplicador pode ter comportamento de eletrodo capacitivo aberto. Isso não autoriza deixar uma ponta de alta tensão exposta nem produzir arcos de propósito. Encerrar a ponta em isolamento apropriado após caracterizar distribuição de potencial, ressonância, campo e eventuais arcos.

## Metas (não certificadas)
- Entrada: 9–12 Vcc.
- Frequência TLC555 calculada, aproximadamente 42–320 kHz com R1=2,2k, R2=2,2k, RV1=22k, C1=680 pF. **Não é garantia de frequência útil do ressonador**.
- Amplitude controlada pelo buck externo no primário. **Nenhuma faixa de saída HV é reivindicada ou comprovada**.
- A seleção de T1 exige medir frequência natural, potência, corrente do primário, tensões, indução magnética, perdas, temperatura, isolamento e acoplamento.

## Restrições
Esta revisão foi criada para revisão técnica em KiCad, **não para fabricação**. O circuito não implementa proteção instantânea contra curto e sobretensão/transientes ressonantes. O acionamento direto de um transformador não caracterizado pode saturar o núcleo, destruir Q1 e provocar choque, incêndio ou descarga. O dispositivo pressurizado usado no relato era de PVC não certificado para pressão de gás comprimido: não repetir a montagem sem recipiente apropriado.
