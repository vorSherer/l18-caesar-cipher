import pytest

from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import (
    encrypt,
    decrypt,
    # shifted,
)


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt_exists():
    assert encrypt


def test_decrypt_exists():
    assert decrypt


@pytest.mark.skip
def test_shifted_exists():
    assert shifted


