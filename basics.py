
def to_numbers(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = []
    
    for character in text.upper():
        if character in alphabet:
            nums.append(alphabet.index(character))
    return nums

def to_letters(nums):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = []
    for i in nums:
        text.append(alphabet[i])

    return text

def egcd(a, b): 
    
    # Base case
    if a == 0:
        return (b, 0, 1)

    g, x1, y1 = egcd(a % b, a)
    x = y1 - (b // a) * x1
    y = x1

    return (g,x,y)

def modinv(a, m):
    g, x, y = egcd(a, m)

    if g != 1:
        raise ValueError(f"The modular inverse doesn't exist becase the GCD of {a} & {m} is not 1")

    return x % m