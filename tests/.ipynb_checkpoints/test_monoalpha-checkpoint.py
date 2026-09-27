import pytest
from monoalpha import encrypt, decrypt, key_from_keyword

key = "MNBVCXZASDFGHJKLPOIUYTREWQ"

def test_key_from_keyword():
    assert key_from_keyword("CRYPTO") == "CRYPTOABDEFGHIJKLMNQSUVWXZ"

def test_check_values():
    assert encrypt("HELLO", key) == "ACGGK"
    assert encrypt("BOB", key) == "NKN"

def test_roundtrip():
    assert decrypt(encrypt("ATTACK AT DAWN", key), key) == "ATTACKATDAWN"

def test_invalid_key_raises():
    with pytest.raises(ValueError):
        encrypt("HELLO", "NOTAPERMUTATION")
    with pytest.raises(ValueError):
        encrypt("HELLO", "AAAAAAAAAAAAAAAAAAAAAAAAAA")