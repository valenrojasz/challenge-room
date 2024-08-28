import pytest
from main import contar_caracteres

def test_lowercase():
  assert contar_caracteres("kakkerlak", "k") == 4

def test_uppercase():
  assert contar_caracteres("KAKKerlak", "K") == 3

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        contar_caracteres(9, 8)

