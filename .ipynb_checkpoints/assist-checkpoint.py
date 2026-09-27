from collections import Counter
from break_caesar import english, spanish

def report(ciphertext: str, language: str = "en") -> str:

    if language == 'en':
        table = english
    else:
        table = spanish

    length = len(ciphertext)
    if length == 0:
        return "The ciphertext is empty"

    output = []

    output.append('1. Letter frequency')
    counts = Counter(ciphertext)
    ranked_cipher = counts.most_common()

    ranked_expected = sorted(table.items(), key = lambda x: x[1], reverse = True)
    output.append("-" * 47)

    for i in range(len(ranked_cipher)):
        c_char, c_count = ranked_cipher[i]
        c_pct = (c_count / length) * 100

        e_char, e_pct = ("", 0.0)
        if i < len(ranked_expected):
            e_char = ranked_expected[i][0]
            e_pct = ranked_expected[i][1]* 100

        output.append(f"   {c_char:<4} | {c_count:<5} | {c_pct:<5.2f}% ||    {e_char:<5} | {e_pct:<5.2f}%")
        
            
    output.append('2. Repeated Trigrams')
    trigrams = {}
    for i in range(length - 2):
        tri = ciphertext[i:i+3]
        if tri not in trigrams:
            trigrams[tri] = []
        trigrams[tri].append(i)

    repeated_trigrams = {k: v for k, v in trigrams.items() if len(v) > 1}
    sorted_tri = sorted(repeated_trigrams.items(), key=lambda x: len(x[1]), reverse=True)


    output.append("\3. Double Letters")
    doubles = set()
    for i in range(length - 1):
        if ciphertext[i] == ciphertext[i+1]:
            doubles.add(ciphertext[i:i+2])
                
    if doubles:
        output.append(", ".join(sorted(list(doubles))))
    else:
        output.append("No double letters found.")
    

    output.append("4. Initial suggested mapping")
    mapping = {}
    for i in range(len(ranked_cipher)):
        if i < len(ranked_expected):
            mapping[ranked_cipher[i][0]] = ranked_expected[i][0]
                
    found_letters = sorted(mapping.keys())
    output.append("Cipher Letter:    " + " ".join(found_letters))
    output.append("Suggested Letter: " + " ".join(mapping[letra] for letra in found_letters))
    
    return "\n".join(output)