from datajud_cli.cache import cache_key, get_cached, set_cached
import pytest

def test_cache_key_formato():
    key = cache_key("80504903720218050001", "tjba")
    assert key == "tjba:80504903720218050001"

def test_cache_miss_retorna_none():
    resultado = get_cached("numero_inexistente_xyz", "tjba")
    assert resultado is None

def test_cache_set_e_get():
    dados = {"numeroProcesso": "80504903720218050001", "tribunal": "TJBA"}
    set_cached("80504903720218050001", "tjba_test", dados)
    resultado = get_cached("80504903720218050001", "tjba_test")
    assert resultado == dados