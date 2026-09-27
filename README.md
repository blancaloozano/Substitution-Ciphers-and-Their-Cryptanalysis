# Substitution-Ciphers-and-Their-Cryptanalysis

This project forms part of the subject Cryptography for Bachelor in Data Science and Engineering, CEU San Pablo University 26/27. It mathematically implements classic substitution ciphers (Caesars, Affine, Monoalphabetic and Vigenère) alongside automated cryptoanalysis tools. The foundation relies on the chi-squared statisic, comparing the frequency distribution of raw decrypted texts against theoretical English and Spanish language tables. 

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

Part C - The four breakers & Measurement task
```text
python3 -c "from break_caesar import break_caesar; from caesar import encrypt; print(break_caesar(encrypt('THISISASECRETMESSAGE', 11), 'en'))"
python3 -c "from break_affine import break_affine; from affine import encrypt; print(break_affine(encrypt('THISISASECRETMESSAGE', 7, 3), 'en'))"
python3 -c "from break_vigenere import break_vigenere; from vigenere import encrypt; print(break_vigenere(encrypt('THISISASECRETMESSAGEUSEDFORTESTING', 'LEMON'), 5, 'en'))"
python3 -c "from assist import report; print(report('QATNTYSMHQXJOCYHKATM', 'en'))"
python3 measure.py
```

Part D - Command Line Interface (CLI)
```text
python crypto.py <cipher> <mode> [key arguments] [--in FILE] [--out FILE] [--lang en|es]

python crypto.py caesar encrypt --key 3 --in message.txt
python crypto.py affine decrypt --a 5 --b 8 --in cipher.txt --out plain.txt
...
```

## 2. Key Space for each cipher
* Caesar: There are 26 distinct keys, since its a shift of k positions and only k mod 26 matters.
* Affine: The multiplier a must satisfy gcd(a,26) =1 to ensure a modular inverse exists for decryption. There are 12 coprime values within the 26 letter alphabet (1, 3, 5, 7...). These shift parameter b can take any of the 26 possible alphabetical positions. Multiplying these independent variables yields a total key space of 12 * 26 = 312 distinct keys. 
* Monoalphabetic substitution: The key is a permutation of the 26-letter alphabet, therefore the keyspace is 26! = 4.0329 x 10^26
* Vigenere: for a fixed key length m, each of the m key positions is independently any of 26 letters, giving 26^m keys. A five letter key has 26^5 = 11881376 possibilities. If the key length is unknown, the total key space is the inifnite sum all over m. The attacker must determine m before anything else. 
## 3. Caesaer breaker, measured
(The measurment code is in measure.py)

Method: 200 random fragments ofa  reference text at each length, each encrypted with a random shift, then broken with break_caesar. Recovery rate = fraction of trials where the recovered shift matches the encryption key exactly.

## 4. Affine breaker, measure and compared with C1

## 5. Vigenere breaker, measured

## 6. Frequency assistant, run on the cryptogram

## 7. Why 26! is broken in minutes but AES-128 is not

## 8. Limitations