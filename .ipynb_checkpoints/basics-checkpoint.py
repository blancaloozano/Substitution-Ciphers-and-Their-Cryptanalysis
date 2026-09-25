
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_numbers(text: str) -> list[int]:
    nums = []
    
    for character in text.upper():
        if character in alphabet:
            nums.append(alphabet.index(character))
    return nums

def to_letters(nums: list[int]) -> str:
    text = []
    for i in nums:
        text.append(alphabet[i])

    return "".join(text)

def egcd(a: int, b: int) -> tuple[int, int, int]: 
    
    # Base case
    if a == 0:
        return (b, 0, 1)

    g, x1, y1 = egcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return (g,x,y)

def modinv(a: int, m: int) -> int:
    g, x, y = egcd(a, m)

    if g != 1:
        raise ValueError(f"The modular inverse doesn't exist becase the GCD of {a} & {m} is not 1")

    return x % m

def xor_bytes(data: bytes, key: bytes) -> bytes:
    key_length = length(key)
    result = bytearray()

    for i in range(len(data)):
        d = data[i]
        k = key[ i % key_length] # The module makes the index of key go back to 0 when it reaches the end

        result.append(d ^ k)

    return result
        