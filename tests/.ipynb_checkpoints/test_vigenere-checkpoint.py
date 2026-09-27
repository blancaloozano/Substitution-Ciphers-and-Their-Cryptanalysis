import pytest
from vigenere import encrypt, decrypt, cosets

def test_check_value():
    assert encrypt("MYSECRETMESSAGE", "KEY") == "WCQOGPOXKOWQKKC"
    assert encrypt("attackatdawn", "LEMON") == "LXFOPVEFRNHR"

def test_cosets_check_value():
    assert cosets("ABCDEF", 3) == ["AD", "BE", "CF"]

def test_roundtrip():
    assert decrypt(encrypt("A LONGER MESSAGE FOR TESTING", "SECRETKEY"), "SECRETKEY") == \
        "ALONGERMESSAGEFORTESTING"

def test_empty_key_raises():
    with pytest.raises(ValueError):
        encrypt("HELLO", "")

def test_shorter_than_key_input():
    assert decrypt(encrypt("HI", "SECRET"), "SECRET") == "HI"