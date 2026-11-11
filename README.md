# ENGR 202 Lab 6 English Edition

Characterizing Frequency Dependent Circuits. This repository contains English question guides, dependency trees, and a three-person work plan based on the instructor's Week 7 Lab 6 document. This is experiment preparation; measured data, experimental photographs, and a final report are pending.

- [Three-person work plan](TEAM_PLAN.md)
- [All 19 dependency trees PDF](analysis/Lab6_Dependency_Trees.pdf)
- [LaTeX source](analysis/latex/Lab6_Dependency_Trees.tex)
- [Original instructor document](source/Lab6_Instructions.docx)
- [Measurement and submission guide](MEASUREMENT_GUIDE.md)

## Complete question dependency graph

This is one connected graph covering **all 19 numbered questions**, matching the question-to-question planning format used for Lab 5. Follow the arrows from prerequisites to dependent answers; multiple incoming arrows indicate results that must converge.

**Colors represent proposed responsibility:** blue = Member A (RC), amber = Member B (RL), purple = Member C (simulations and integration), gray = shared inputs or team review. Colors do not indicate completion. All experimental results remain pending.

```mermaid
flowchart TD
    START["Lab 6 · Frequency Dependent Circuits"]
    TEAM["Q1.1 · Team information"]
    START --> TEAM

    subgraph RC["Filter 1 · RC low-pass · Member A"]
        direction TB
        RCINPUT["Given RC schematic · R = 1 kohm · C = 0.22 uF"]
        R1["Q3.1 · Wire circuit and photograph setup"]
        R2["Q3.2 · Identify filter type and explain"]
        R3["Q3.3 · Derive H, magnitude, phase and cutoff"]
        R4["Q3.4 · Substitute values and convert to Hz"]
        R5["Q3.5 · Hand-draw magnitude and phase Bode plots"]
        R6["Q3.6 · Frequency sweep, cursor captures, table, cutoff and slope"]
        R7["Q3.7 · Experimental Bode plots in Excel"]
        R8["Q3.8 · LTspice AC Bode plots · Member C"]
        R9["Q3.9 · Compare theory, simulation and experiment"]
        RCINPUT --> R1
        RCINPUT --> R2
        RCINPUT --> R3
        RCINPUT --> R8
        R3 --> R4
        R3 --> R5
        R4 --> R5
        R1 --> R6
        R6 --> R7
        R2 --> R9
        R4 --> R9
        R5 --> R9
        R6 --> R9
        R7 --> R9
        R8 --> R9
    end

    subgraph RL["Filter 2 · RL high-pass · Member B"]
        direction TB
        RLINPUT["Given RL schematic · R = 690 ohm · L = 0.1 H"]
        L1["Q4.1 · Wire circuit and photograph setup"]
        L2["Q4.2 · Identify filter type and explain"]
        L3["Q4.3 · Derive H, magnitude, phase and cutoff"]
        L4["Q4.4 · Substitute values and convert to Hz"]
        L5["Q4.5 · Hand-draw magnitude and phase Bode plots"]
        L6["Q4.6 · Frequency sweep, cursor captures, table, cutoff and slope"]
        L7["Q4.7 · Experimental Bode plots in Excel"]
        L8["Q4.8 · LTspice AC Bode plots · Member C"]
        L9["Q4.9 · Compare theory, simulation and experiment"]
        RLINPUT --> L1
        RLINPUT --> L2
        RLINPUT --> L3
        RLINPUT --> L8
        L3 --> L4
        L3 --> L5
        L4 --> L5
        L1 --> L6
        L6 --> L7
        L2 --> L9
        L4 --> L9
        L5 --> L9
        L6 --> L9
        L7 --> L9
        L8 --> L9
    end

    START --> RCINPUT
    START --> RLINPUT
    RC ~~~ RL
    REVIEW["Member C · Assemble report and check every required item"]
    TEAM --> REVIEW
    R1 --> REVIEW
    R9 --> REVIEW
    L1 --> REVIEW
    L9 --> REVIEW
    REVIEW --> FINAL["Team review · Final report ready for submission"]

    classDef memberA fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef memberB fill:#fef3c7,stroke:#b45309,color:#451a03
    classDef memberC fill:#ede9fe,stroke:#7c3aed,color:#2e1065
    classDef shared fill:#f1f5f9,stroke:#64748b,color:#0f172a
    class R1,R2,R3,R4,R5,R6,R7,R9 memberA
    class L1,L2,L3,L4,L5,L6,L7,L9 memberB
    class R8,L8,REVIEW memberC
    class START,TEAM,RCINPUT,RLINPUT,FINAL shared
```

### Parallel work and convergence

- Q1.1 and both filter workflows can start independently. Within each filter, setup, classification, analytical derivation, and ideal LTspice simulation can start from the given schematic. Simulation does not need to wait for measured data.
- Q3.4/Q4.4 use the corresponding derivation. Q3.5/Q4.5 use the analytical magnitude and phase and the numerical cutoff frequency.
- Q3.6/Q4.6 require a verified physical circuit. Q3.7/Q4.7 require measured data, including signed phase. Setup photographs remain mandatory even though taking a photograph is not a prerequisite for acquiring data.
- Q3.9/Q4.9 combine classification, theoretical results, hand sketches, the measured table and plots, and LTspice results. Include actual measured cutoff and stopband slope when comparing trends.
- With one ADALM2000, schedule RC and RL measurements sequentially while calculations and simulations overlap. The two filter workflows are independent; their vertical placement is only for readability.
- All 19 questions reach final review directly or through their downstream results. The final review also checks both setup photographs and every required appendix capture.

[Standalone graph source](planning/whole-lab.mmd) · [Three-person work plan](TEAM_PLAN.md)

The individual formula diagrams linked below are additional aids. The connected graph above shows the dependencies between questions across the whole lab.

## Circuits and channels

| Filter | Original component values | Output location | Ideal type | Ideal cutoff |
| --- | --- | --- | --- | --- |
| RC | R = 1000 ohm, C = 0.22 uF | Across capacitor | Low-pass | 723.43 Hz |
| RL | R = 690 ohm, L = 0.1 H | Across inductor | High-pass | 1098.17 Hz |

CH1 = Vin and CH2 = Vout. Use a 2 Vpp sine wave, start setup at 1 kHz, and measure from 10 Hz to 20 kHz. Use the Lab 6 channel mapping and the component values above.

## Question guides

- [Q1.1 Group information](questions/Q1_1.md)
- [Q3.1 RC Setup photograph](questions/Q3_1.md)
- [Q3.2 RC Filter classification](questions/Q3_2.md)
- [Q3.3 RC Transfer function derivation](questions/Q3_3.md)
- [Q3.4 RC Numerical expressions in Hz](questions/Q3_4.md)
- [Q3.5 RC Hand-drawn Bode plots](questions/Q3_5.md)
- [Q3.6 RC Measured frequency sweep](questions/Q3_6.md)
- [Q3.7 RC Experimental Bode plots in Excel](questions/Q3_7.md)
- [Q3.8 RC LTspice AC simulation](questions/Q3_8.md)
- [Q3.9 RC Theory simulation and measurement comparison](questions/Q3_9.md)
- [Q4.1 RL Setup photograph](questions/Q4_1.md)
- [Q4.2 RL Filter classification](questions/Q4_2.md)
- [Q4.3 RL Transfer function derivation](questions/Q4_3.md)
- [Q4.4 RL Numerical expressions in Hz](questions/Q4_4.md)
- [Q4.5 RL Hand-drawn Bode plots](questions/Q4_5.md)
- [Q4.6 RL Measured frequency sweep](questions/Q4_6.md)
- [Q4.7 RL Experimental Bode plots in Excel](questions/Q4_7.md)
- [Q4.8 RL LTspice AC simulation](questions/Q4_8.md)
- [Q4.9 RL Theory simulation and measurement comparison](questions/Q4_9.md)

## Work sequence

For each filter, wiring, theory, and ideal simulation can start in parallel. Complete the measured table and cursor captures before building experimental Excel plots and writing the final comparison. Q3.9 and Q4.9 depend on the corresponding theoretical, simulated, and experimental evidence.

## Rebuilding

Run `xelatex Lab6_Dependency_Trees.tex` inside `analysis/latex` in a complete TeX installation with TikZ. The PDF and PNG previews use Computer Modern mathematical rendering. The accompanying TikZ source can also be compiled independently.

The separate [original Lab6 repository](https://github.com/OutisNemosseus/Lab6) is retained.
