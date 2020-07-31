import pytest

from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import (
    encrypt,
    decrypt,
    caesar_cracker,
)


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_exists():
    assert encrypt


def test_decrypt_exists():
    assert decrypt


def test_caesar_cracker_exists():
    assert caesar_cracker


def test_encrypt_passes():
    expected = "Udymts nx xsjfpd"
    actual = encrypt("Python is sneaky", 5)
    assert actual == expected


def test_decrypt_passes():
    expected = "Python is sneaky"
    actual = decrypt("Udymts nx xsjfpd", 5)
    assert actual == expected


# @pytest.mark.skip
def test_caesar_cracker_passes():
    expected = "It was the best of times, it was the worst of times."
    actual = caesar_cracker('Xi lph iwt q...ghi du ixbth.')

