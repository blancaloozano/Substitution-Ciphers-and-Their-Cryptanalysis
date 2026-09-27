from caesar import encrypt, decrypt

def test_check_value():
    assert encryot("MYSECRETMESSAGE", 3) == "PBVHFUHWPHVVDJH"

def test_roundtrip():
    assert decrypt(encrypt("Attack At Dawn!", 11), 11) == "ATTACKATDAWN"

def test_negative_and_large_k():
    assert encrypt("HELLO", -3) == encrypt("HELLO", 23)
    assert encrypt("HELLO", 29) = encrypt("HELLO", 3)

def test_empty_and_no_letters():
    assert encrypt("", 5) == ""
    assert encrypt("12345!", 5) = ""
    