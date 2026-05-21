from rich import print
from rich.panel import Panel
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("[yellow]Nome[/yellow]", justify="center")
tabela.add_column("[yellow]Preço[/yellow]", justify="center")
tabela.add_row("[blue]Lápis[/blue]", "[green]R$ 3, 00[/green]")
tabela.add_row("[blue]Borracha[/blue]", "[green]R$ 5, 00[/green]")
print(tabela)