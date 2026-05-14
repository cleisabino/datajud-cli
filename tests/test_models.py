from datajud_cli.models import Processo, Classe, Tribunal, Movimento
from datajud_cli.main import normalizar_numero, formatar_data

def test_normalizar_numero_sem_mascara():
    assert normalizar_numero("80504903720218050001") == "80504903720218050001"

def test_normalizar_numero_com_mascara():
    assert normalizar_numero("8050490-37.2021.8.05.0001") == "80504903720218050001"

def test_normalizar_numero_com_espacos():
    assert normalizar_numero(" 8050490-37.2021.8.05.0001 ") == "80504903720218050001"

def test_formatar_data_formato_longo():
    assert formatar_data("20210518000000") == "18/05/2021"

def test_formatar_data_formato_iso():
    assert formatar_data("2021-05-18T00:00:00.000Z") == "18/05/2021"

def test_formatar_data_none():
    assert formatar_data(None) == "—"

def test_processo_tribunal_como_string():
    p = Processo(
        numeroProcesso="80504903720218050001",
        tribunal="TJBA",
    )
    assert p.tribunal == "TJBA"

def test_processo_tribunal_como_objeto():
    p = Processo(
        numeroProcesso="80504903720218050001",
        tribunal={"codigo": "8.05", "nome": "Tribunal de Justiça da Bahia"},
    )
    assert isinstance(p.tribunal, Tribunal)
    assert p.tribunal.nome == "Tribunal de Justiça da Bahia"

def test_processo_campos_opcionais_none():
    p = Processo(numeroProcesso="80504903720218050001")
    assert p.classe is None
    assert p.movimentos is None