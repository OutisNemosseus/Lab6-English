# Measurement and submission guide

## Evidence to collect

For each filter measure 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, and 20000 Hz. Add points near cutoff. Save a full Scopy oscilloscope capture at every point, showing CH1 and CH2, both VRMS and Vpp readings, frequency, and the cursor time difference. Enable mean measurements to check offsets. Adjust the time base to show approximately one or two full cycles.

CH1 = Vin; CH2 = Vout. Use a 2 Vpp sine wave and start setup at 1 kHz.

Place RC traces in Appendix B and RL traces in Appendix C. Q4.6 refers to Appendix B, but the final appendix heading explicitly identifies Appendix C for RL. Suggested names: rc_1000Hz_scope.png and rl_1000Hz_scope.png.

## Calculation conventions

- Gain ratio a = Vout_rms / Vin_rms; G = 20 log10(a). Use the same amplitude convention for input and output.
- Define delta t = t_out - t_in using adjacent zero crossings with the same direction. Phase phi = -360 f delta t in degrees. If output occurs first, delta t is negative and phase is positive. Resolve cycle ambiguity before calculating.
- Ideal low-pass phase is -atan(f/fc); ideal high-pass phase is 90 degrees - atan(f/fc), with atan expressed in degrees. These are reference trends, not replacement measurements.
- For an ideal unity-passband filter, half power occurs at |H| = 1/sqrt(2), or -3.0103 dB. If measured passband gain differs from 1, additionally report the frequency 3.01 dB below that measured passband and distinguish it from the absolute ratio 0.7071.
- Stopband slope m = (G2-G1)/log10(f2/f1), in dB/decade. Choose points well inside the stopband. Ideal RC slope is -20; ideal RL slope is +20 with increasing frequency. If the measured range is too short, label the result a local estimate.
- In Excel use XY scatter charts with a logarithmic numeric frequency axis. Overlay theoretical curves and experimental points using the same axes.

## RL nonideal behavior

The instructor states that a clear deviation from ideal behavior will occur, but do not claim to have observed it before collecting evidence. With the circuit unpowered and the inductor disconnected, measure its DC resistance rL as one possible explanation. For output across the whole physical coil, a candidate model is H = (rL + j omega L)/(R + rL + j omega L), with low-frequency gain rL/(R+rL) and pole frequency (R+rL)/(2 pi L). Test this model against measurements. Parasitic capacitance, loading, and other effects may also matter.

## Instruction corrections

In Q4.3/Q4.4, capacitor C and R and C should refer to inductor L and R and L. In Q4.5, the reference to Q3.3 should be read as the RL derivation Q4.3. The original instructor document is preserved unchanged.

## Final checks

For each filter include the Q.1 photograph, Q.3 derivation, Q.5 hand sketch, Q.6 table and every cursor capture, Q.7 Excel plots, Q.8 AC simulation, and Q.9 comparison. Dependency diagrams do not replace experimental evidence.
