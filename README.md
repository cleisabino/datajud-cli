# datajud-cli

A command-line tool to query Brazilian judicial process data from the [CNJ DataJud public API](https://www.cnj.jus.br/sistemas/datajud/api-publica/).

> **Status:** 🚧 Active development. First working version expected in ~5 days.

## What it does

Query judicial processes from Brazilian courts directly from the terminal, without browser, scraping or manual lookup. Returns structured data (JSON or table) that can be piped to other tools, saved, or analyzed.

## Why this exists

Brazilian judicial data is public but hard to consume programmatically. Lawyers, paralegals, legaltech engineers, and researchers regularly need to pull process data and end up doing manual lookups on tribunal websites. `datajud-cli` makes this scriptable.

## Planned features

- [ ] Query a process by its CNJ number (`NNNNNNN-DD.AAAA.J.TR.OOOO`)
- [ ] Output as JSON, CSV, or readable table
- [ ] Local cache to avoid repeated API calls
- [ ] Retry with backoff on rate limits
- [ ] Configurable tribunal targeting (TJBA, TJSP, TRF1, etc.)
- [ ] Installable via `pipx install datajud-cli`

## Tech stack

- Python 3.11+
- [Typer](https://typer.tiangolo.com/) — CLI framework
- [httpx](https://www.python-httpx.org/) — HTTP client with retry support
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [pytest](https://pytest.org/) — testing

## Installation

Not yet available. Once the first release is published:

```bash
pipx install datajud-cli
```

## Usage (planned)

```bash
# Query a single process
datajud query 0001234-56.2023.8.05.0001

# Save as JSON
datajud query 0001234-56.2023.8.05.0001 --format json > processo.json

# Bulk query from a file
datajud query --batch processos.txt --format csv
```

## Development

Setup instructions and contribution guide will be added once the first version lands.

## License

MIT — see [LICENSE](LICENSE).

---

Built by [Clei Sabino](https://github.com/cleisabino) — backend engineer with 7+ years building large-scale legal systems for Brazilian public sector.
