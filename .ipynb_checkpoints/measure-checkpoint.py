import random
 
from caesar import encrypt as caesar_encrypt
from affine import encrypt as affine_encrypt, valid_keys
from vigenere import encrypt as vigenere_encrypt
from break_caesar import break_caesar
from break_affine import break_affine
from break_vigenere import break_vigenere

reference_en = ("It is a truth universally acknowledged that a single man in "
    "possession of a good fortune must be in want of a wife However "
    "little known the feelings or views of such a man may be on his "
    "first entering a neighbourhood this truth is so well fixed in "
    "the minds of the surrounding families that he is considered as "
    "the rightful property of some one or other of their daughters "
    "My dear Mr Bennet said his lady to him one day have you heard "
    "that Netherfield Park is let at last Mr Bennet replied that he "
    "had not You want to tell me and I have no objection to hearing "
    "it This was invitation enough")

reference_es = ("En un lugar de la Mancha de cuyo nombre no quiero acordarme no "
    "ha mucho tiempo que vivia un hidalgo de los de lanza en astillero "
    "adarga antigua rocin flaco y galgo corredor Una olla de algo mas "
    "vaca que carnero salpicon las mas noches duelos y quebrantos los "
    "sabados lantejas los viernes algun palomino de anadidura los "
    "domingos consumian las tres partes de su hacienda El resto della "
    "concluian sayo de velarte calzas de velludo para las fiestas con "
    "sus pantuflos de lo mesmo")

def random_fragments(reference, length, count):
    fragments = []
    start = len(reference) - length
    
    for i in range(count):
        start = random.randint(0, start)
        fragments.append(reference[start.start + length])

    return fragments

def measure_caesar(reference, length, count, langauge):
    fragments = random_fragments(reference, length, count)
    successes = 0
    for fragment in fragments:
        k = random.randint(0, 25)
        ciphertext = caesar_encrypt(fragment, k)
        try:
            recovered_k, _ = break_caesar(ciphertext, language)
        except Exception:
            continue
        if recovered_k == k:
            successes = successes + 1
    return successes / count

def measure_affine(reference, length, count, language):
    keys = valid_keys()
    fragments = random_fragments(reference, length, count)
    successes = 0
    crashed = 0
    for fragment in fragments:
        a, b = random.choice(keys)
        ciphertext = affine_encrypt(fragment, a, b)
        try:
            recovered_key, _ = break_affine(ciphertext, language)
        except Exception:
            crashed = crashed + 1
            continue
        if recovered_key == (a, b):
            successes = successes + 1
    if crashed == count:
        return None
    return successes / count

def random_key(m):
    letters = []
    for i in range(m):
        letters.append(chr(ord("A") + random.randint(0, 25)))
    key = ""
    for letter in letters:
        key = key + letter
    return key

def measure_vigenere(reference, length, count, language):
    stripped = reference.replace(" ", "")
    fragments = random_fragments(stripped, total_length, count)
    successes = 0
    for fragment in fragments:
        key = random_key(m)
        ciphertext = vigenere_encrypt(fragment, key)
        try:
            recovered_key, _ = break_vigenere(ciphertext, m, language)
        except Exception:
            continue
        if recovered_key == key:
            successes = successes + 1
    return successes / count