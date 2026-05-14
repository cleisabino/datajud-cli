import httpx
import os
from dotenv import load_dotenv
from datajud_cli.models import Processo
from datajud_cli.cache import get_cached, set_cached

load_dotenv()

BASE_URL = "https://api-publica.datajud.cnj.jus.br"

TRIBUNAIS = {
    "tjba": "api_publica_tjba",
    "tjsp": "api_publica_tjsp",
    "trf1": "api_publica_trf1",
    "tjmg": "api_publica_tjmg",
    "stj":  "api_publica_stj",
}

def get_headers() -> dict:
    api_key = os.getenv("DATAJUD_API_KEY")
    if not api_key:
        raise ValueError("DATAJUD_API_KEY não encontrada. Verifique o arquivo .env")
    return {
        "Authorization": f"APIKey {api_key}",
        "Content-Type": "application/json",
    }

def consultar_processo(numero: str, tribunal: str, use_cache: bool = True) -> Processo | None:
    alias = TRIBUNAIS.get(tribunal.lower())
    if not alias:
        raise ValueError(f"Tribunal '{tribunal}' não suportado. Opções: {list(TRIBUNAIS.keys())}")

    if use_cache:
        cached = get_cached(numero, tribunal)
        if cached:
            return Processo(**cached)
    
    url = f"{BASE_URL}/{alias}/_search"
    body = {
        "query": {
            "match": {
                "numeroProcesso": numero
            }
        }
    }

    with httpx.Client(timeout=30.0) as client:
        response = client.post(url, headers=get_headers(), json=body)
        response.raise_for_status()

    data = response.json()
    hits = data.get("hits", {}).get("hits", [])

    if not hits:
        return None
    
    processo_data = hits[0]["_source"]

    if not processo_data:
        return None

    if use_cache:
        set_cached(numero, tribunal, processo_data)

    return Processo(**processo_data)