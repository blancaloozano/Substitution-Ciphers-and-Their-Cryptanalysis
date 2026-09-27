import random
from caesar import encrypt as caesar_encrypt
from affine import encrypt as affine_encrypt, valid_keys
from vigenere import encrypt as vigenere_encrypt
from break_caesar import break_caesar, REFERENCE_EN
from break_affine import break_affine
from break_vigenere import break_vigenere


def test_break_caesar_recovers_key_at_reliable_length():
    successes = 0
    for i in range(20):
        start = random.randint(0, len(REFERENCE_EN) - 60)
        fragment = REFERENCE_EN[start:start + 60]
        k = random.randint(0, 25)
        ciphertext = caesar_encrypt(fragment, k)
        recovered_k, _ = break_caesar(ciphertext, "en")
        if recovered_k == k:
            successes += 1
    assert successes >= 18


def test_break_affine_recovers_key_at_reliable_length():
    keys = valid_keys()
    successes = 0
    for i in range(20):
        start = random.randint(0, len(REFERENCE_EN) - 100)
        fragment = REFERENCE_EN[start:start + 100]
        a, b = random.choice(keys)
        ciphertext = affine_encrypt(fragment, a, b)
        recovered_key, _ = break_affine(ciphertext, "en")
        if recovered_key == (a, b):
            successes += 1
    assert successes >= 18


def test_break_vigenere_recovers_key_at_reliable_length():
    successes = 0
    for i in range(20):
        start = random.randint(0, len(REFERENCE_EN) - 200)
        fragment = REFERENCE_EN.replace(" ", "")[start:start + 200]
        key = "SECRET"
        ciphertext = vigenere_encrypt(fragment, key)
        recovered_key, _ = break_vigenere(ciphertext, len(key), "en")
        if recovered_key == key:
            successes += 1
    assert successes >= 18