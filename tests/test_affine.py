import pytest
from affine import encrypt, decrypt, valid_keys

def test_check_value():
    assert encrypt("attack", 5,8) == "IZZISG"

def test_roundtrip():
    assert decrypt(encrypt("HELLO WORLD", 7,3), 7,3) == "HELLOWORLD"

def test_invalid_a_raises():
    with pytest.raises(ValueError):
        encrypt("HELLO", 13,8)
    with pytest.raises(ValueError):
        decrypt("HELLO", 2,8)

def test_valid_keys_count():
    assert len(valid_keys()) == 312