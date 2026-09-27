import pytest

from basics import to_numbers, to_letters, egcd, moding, xor_bytes

def test_to_numbers_to_letters_roundtrip():
    assert to_letters(to_numbers("Hello, World 123")) == "HELLOWORLD"

def test_mod_inv_check_values():
    assert modinv(5, 26) == 21
    assert modinv(7, 26) == 15
    assert modinv(17, 26) == 23

def test_modinv_raises_when_not_invertible():
    with pytest.raises(ValueError):
        modinv(13, 26)
    with pytest.raises(ValueError):
        modinv(2,26)

def test_egc_with_negatives():
    for a, b in [(-5, 26), (5, -26), (-17, -26), (0, 5), (5,0)]:
        g, x, y = egcd(a,b)
        assert g >= 0
        assert a * x + b * y == g

def test_xor_bytes_check_values():
    assert xor_bytes(b"HELLO", b"KEYKE").hex() == "030015070a"

def test_xor_bytes_involution():
    data = b"THE BROWN FOX"
    key = b"SECRET"
    assert xor_bytes(xor_bytes(data, key), key) == data

def test_xor_bytes_empty_key_raises():
    with pytest.raises(ValueError):
        xor_bytes(b"HELLO",b"")
        