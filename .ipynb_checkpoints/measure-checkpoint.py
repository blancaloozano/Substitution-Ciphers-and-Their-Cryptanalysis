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

if __name__ == "__main__":
    lengths = [20, 30, 40, 60, 100]
    trials = 200

    print("C1 -- Caesar breaker recovery rate")
    print(f"{'length':>8} | {'EN text/EN table':>18} | {'ES text/ES table':>18} | {'ES text/EN table':>18}")
    for length in lengths:
        r1 = measure_caesar(REFERENCE_EN, length, trials, "en")
        r2 = measure_caesar(REFERENCE_ES, length, trials, "es")
        r3 = measure_caesar(REFERENCE_ES, length, trials, "en")
        print(f"{length:>8} | {r1:>18.2f} | {r2:>18.2f} | {r3:>18.2f}")

    print()
    print("C2 -- Affine breaker recovery rate (English)")
    print(f"{'length':>8} | {'recovery rate':>15}")
    for length in lengths:
        r = measure_affine(REFERENCE_EN, length, trials, "en")
        label = f"{r:.2f}" if r is not None else "CRASHES"
        print(f"{length:>8} | {label:>15}")

    print()
    print("C2b -- Affine breaker, Spanish language table")
    r_es = measure_affine(REFERENCE_ES, 100, 20, "es")
    if r_es is None:
        print("  language='es' crashes on every trial (break_affine.py bug: 'table = \\'spanish\\'' is a string, not the dict)")
    else:
        print(f"  recovery rate at length 100: {r_es:.2f}")

    print()
    print("C3 -- Vigenere breaker recovery rate")
    key_lengths = [3, 5, 7]
    total_lengths = [60, 120, 200, 300]
    trials3 = 100
    header = f"{'m':>4} |"
    for total_length in total_lengths:
        header = header + f" len={total_length:>4} |"
    print(header)
    for m in key_lengths:
        row = f"{m:>4} |"
        for total_length in total_lengths:
            rate = measure_vigenere(REFERENCE_EN, m, total_length, trials3, "en")
            row = row + f"{rate:>9.2f} |"
        print(row)
