# datajud-cli

A command-line tool to query Brazilian judicial process data 
from the [CNJ DataJud public API](https://datajud-wiki.cnj.jus.br/api-publica/).

## Features

- [x] Query a process by its CNJ number (with or without formatting mask)
- [x] Output as table, JSON, or CSV
- [x] Local cache (24h TTL) to avoid repeated API calls
- [x] Supports multiple tribunals (TJBA, TJSP, TRF1, TJMG, STJ)
- [ ] Retry with backoff on rate limits
- [ ] Bulk query from file
- [ ] Installable via `pipx install datajud-cli`

## Installation

```bash
git clone https://github.com/cleisabino/datajud-cli.git
cd datajud-cli
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Copy `.env.example` to `.env` and add your DataJud API key:

```bash
cp .env.example .env
# edit .env and set DATAJUD_API_KEY
```

Get the public API key at: https://datajud-wiki.cnj.jus.br/api-publica/acesso/

## Usage

### Query a process

```bash
# with formatting mask (auto-normalized)
datajud query 8050490-37.2021.8.05.0001

# raw 20-digit number
datajud query 80504903720218050001

# different tribunal
datajud query 8050490-37.2021.8.05.0001 --tribunal tjsp
```

### Output formats

```bash
# default: formatted table
datajud query 8050490-37.2021.8.05.0001

# JSON
datajud query 8050490-37.2021.8.05.0001 --json

# CSV (pipeable)
datajud query 8050490-37.2021.8.05.0001 --csv >> processos.csv
```

### Cache

```bash
# skip cache and hit the API directly
datajud query 8050490-37.2021.8.05.0001 --no-cache

# clear local cache
datajud limpar-cache
```

### Supported tribunals

| Sigla | Tribunal |
|-------|----------|
| tjba  | Tribunal de Justiça da Bahia |
| tjsp  | Tribunal de Justiça de São Paulo |
| trf1  | Tribunal Regional Federal da 1ª Região |
| tjmg  | Tribunal de Justiça de Minas Gerais |
| stj   | Superior Tribunal de Justiça |

## Tech stack

- Python 3.12
- [Typer](https://typer.tiangolo.com/) — CLI framework
- [httpx](https://www.python-httpx.org/) — HTTP client
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [Rich](https://rich.readthedocs.io/) — terminal formatting
- [diskcache](https://grantjenks.com/docs/diskcache/) — local cache

## Running tests

```bash
pytest tests/ -v
```

## License

MIT — see [LICENSE](LICENSE).

---

Built by [Clei Sabino](https://github.com/cleisabino) · 
Senior Backend Engineer · 7+ years building legal systems 
for Brazilian public sector.