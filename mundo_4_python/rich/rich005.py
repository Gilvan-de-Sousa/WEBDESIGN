from rich import print
from rich.table import Table
from rich.panel import Panel
from rich import inspect
from rich.traceback import install

def divisao(x, y):
    return x / y


d = divisao(10, 0)

install()