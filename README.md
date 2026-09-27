# Substitution-Ciphers-and-Their-Cryptanalysis

This project mathematically implements classic substitution ciphers (Caesars, Affine, Monoalphabetic and Vigenère) alongside automated cryptoanalysis tools. The foundation relies on the chi-squared statisic, comparing the frequency distribution of raw decrypted texts against theoretical English and Spanish language tables. 

The objective is to demonstrate how statisctical analysis breaks algorithms that preserve the underlying language structure, highlighting the practical weakness of simple substitution compared to modern cryptographic systems.

This project was done for the subject Cryptography, part of Bachelor in Data Science and Engineering, Universidad CEU San Pablo 26/27.

## 1. File Structure

The repository is organized into three logical layers to separate the encryption, analysis and user interface components:

**Interface Layer** --> *crypto.py* acts as the single entry point, utilizing the standard *argparse* library to manage commands, mathematical parameters and local reading/writing.

**Base Cryptography** --> *caesar.py*, *affine.py*, *monoalpha.py* and *vigenere.py* contain the logic for the encryption, decryption and algorithmic coset generation.

**Cryptoanalysis Layer** --> *break_caesar.py*, *break_affine.py* and *break_vigenere.py* execute automated attacks using statistically guided force. *assist.py* generates advance frequency reports (trigrams, bigrams, double letters).

**Validation Folder** --> The *tests/* directory includes automated infrastructure to ensure statistical reliability and guarantee no code regressions occur within the base algorithms.

## 2. Usage Instructions

The program is executed entirely from the terminal by targetting the main executable gile. All commands assume you are in the repository root, with Python 3.11+ and no dependencies beyond the standard library (pytest only if you with to run the automated tests).









frequency distribution : https://en.wikipedia.org/wiki/Letter_frequency
