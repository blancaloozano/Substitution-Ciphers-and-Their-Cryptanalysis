# Substitution-Ciphers-and-Their-Cryptanalysis

This project mathematically implements classic substitution ciphers (Caesars, Affine, Monoalphabetic and Vigenère) alongside automated cryptoanalysis tools. The foundation relies on the chi-squared statisic, comparing the frequency distribution of raw decrypted texts against theoretical English and Spanish language tables. 

The objective is to demonstrate how statisctical analysis breaks algorithms that preserve the underlying language structure, highlighting the practical weakness of simple substitution compared to modern cryptographic systems.

## 1. How to run everything

The program is executed entirely from the terminal by targetting the main executable file, crypto.py. All commands assume you are in the repository root, with Python 3.11+ and no dependencies beyond the standard library (pytest only if you with to run the automated tests). Here are asome examples on how to run everything:

Part B - The four ciphers
```text
python3 -c "from caesar import encrypt; print(encrypt('MYSECRETMESSAGE', 3))"
python3 -c "from affine import encrypt; print(encrypt('attack', 5,8))"
python3 -c "from monoalpha import encrypt, key_from_keyword; print(encrypt('HELLO', key_from_keyword('CRYPTO')))"
python3 -c "from vigenere import encrypt; print(encrypt('attackatdawn', 'LEMON'))"
```

Part C - The four breakers
```text
python3 -c "from break_caesar import break_caesar; from caesar import encrypt; print(break_caesar(encrypt('THISISASECRETMESSAGE', 11), 'en'))"
python3 -c "from break_affine import break_affine; from affine import encrypt; print(break_affine(encrypt('THISISASECRETMESSAGE', 7, 3), 'en'))"
python3 -c "from break_vigenere import break_vigenere; from vigenere import encrypt; print(break_vigenere(encrypt('THISISASECRETMESSAGEUSEDFORTESTING', 'LEMON'), 5, 'en'))"
python3 -c "from assist import report; print(report('QATNTYSMHQXJOCYHKATM', 'en'))"
```
