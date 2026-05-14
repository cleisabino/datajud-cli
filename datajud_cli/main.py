import typer
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from datajud_cli.client import consultar_processo
from datajud_cli.models import Tribunal

app = typer.Typer(help="CLI para consulta de processos judiciais via API DataJud/CNJ")
console = Console()

def normalizar_numero(numero: str) -> str:
    """Remove máscara do número CNJ, mantendo apenas dígitos."""
    return "".join(c for c in numero if c.isdigit())

def formatar_data(data: str | None) -> str:
    if not data:
        return "—"
    if len(data) == 14 and data.isdigit():
        return f"{data[6:8]}/{data[4:6]}/{data[:4]}"
    if "T" in data:
        partes = data[:10].split("-")
        return f"{partes[2]}/{partes[1]}/{partes[0]}"
    return data

@app.command()
def query(
    numero: str = typer.Argument(..., help="Número do processo (20 dígitos, sem pontos e traços)"),
    tribunal: str = typer.Option("tjba", "--tribunal", "-t", help="Sigla do tribunal: tjba, tjsp, trf1, tjmg, stj"),
    json_output: bool = typer.Option(False, "--json", help="Retorna output em JSON puro"),
):
    """Consulta um processo judicial pelo número CNJ."""

    numero_normalizado = normalizar_numero(numero)

    with console.status(f"Consultando processo {numero} no {tribunal.upper()}..."):
        try:
            processo = consultar_processo(numero_normalizado, tribunal)
        except ValueError as e:
            rprint(f"[red]Erro:[/red] {e}")
            raise typer.Exit(1)
        except Exception as e:
            rprint(f"[red]Erro na consulta:[/red] {e}")
            raise typer.Exit(1)

    if not processo:
        rprint(f"[yellow]Processo {numero} não encontrado no {tribunal.upper()}.[/yellow]")
        raise typer.Exit(0)

    if json_output:
        import json
        rprint(json.dumps(processo.model_dump(), indent=2, ensure_ascii=False))
        return

    # Output formatado em tabela
    table = Table(title=f"Processo {processo.numeroProcesso}", show_header=False)
    table.add_column("Campo", style="cyan", width=20)
    table.add_column("Valor")

    table.add_row("Número", processo.numeroProcesso or "—")
    table.add_row("Classe", processo.classe.nome if processo.classe else "—")
    tribunal_nome = (
        processo.tribunal.nome
        if isinstance(processo.tribunal, Tribunal)
        else processo.tribunal or "—"
    )
    table.add_row("Tribunal", tribunal_nome)
    table.add_row("Ajuizamento", formatar_data(processo.dataAjuizamento))
    table.add_row("Última atualização", formatar_data(processo.ultimaAtualizacao))

    console.print(table)

    if processo.movimentos:
        rprint(f"\n[bold]Últimas movimentações:[/bold]")
        for mov in processo.movimentos[:5]:
            rprint(f"  [dim]{formatar_data(mov.dataHora)}[/dim] — {mov.nome}")

if __name__ == "__main__":
    app()