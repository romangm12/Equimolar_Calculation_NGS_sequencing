[README.md](https://github.com/user-attachments/files/27658180/README.md)
# Equimolar Calculation for NGS Sequencing

Command-line calculator for preparing equimolar pools of DNA fragments or amplicons before next-generation sequencing.

## Why this project exists

When several amplicons or DNA fragments are pooled for sequencing, each fragment should ideally contribute a similar number of molecules. This script uses fragment length, DNA mass, and available volume to estimate the concentration in femtomoles per microliter and calculate how much volume should be taken from each fragment.

## What it calculates

- Approximate molecular weight for double-stranded DNA.
- DNA concentration in fmol/uL.
- The maximum equimolar pooling volume possible from the limiting fragment.
- The volume of each fragment needed for the final pool.

## Formula

For double-stranded DNA, the approximate molecular weight is:

```text
MW = (length_bp * 617.96) + 36.04
```

The concentration in femtomoles per microliter is:

```text
fmol/uL = (ng/uL * 1e-9 / MW) * 1e15
```

Which simplifies to:

```text
fmol/uL = ng/uL * 1e6 / MW
```

## How to run

```bash
python equimolar_calculator.py
```

The script will ask for:

- Number of fragments or amplicons.
- Name of each fragment.
- Length in base pairs.
- Total DNA mass in ng.
- Total available volume in uL.

## Example output

```text
Equimolar pooling results
------------------------------------------------------------
Fragment             fmol/uL      Use uL    Available uL
------------------------------------------------------------
Amplicon_1            12.845        3.20           10.00
Amplicon_2             8.153        5.04           10.00
------------------------------------------------------------
Final pool volume: 8.24 uL
Each fragment contributes the same femtomoles to the final pool.
```

## Notes

This tool is intended as a practical laboratory helper. Results should be checked against the requirements of the sequencing provider or library preparation protocol.

## Author

Roman Gonzalez Mora
