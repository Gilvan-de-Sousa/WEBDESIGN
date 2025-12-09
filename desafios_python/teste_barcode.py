import time
import requests
from copy import deepcopy
import tkinter as tk
from tkinter import ttk, messagebox

# ========================= UTILITÁRIOS =========================

def medir_tempo(func, *args, **kwargs):
    inicio = time.time()
    resultado = func(*args, **kwargs)
    fim = time.time()
    return resultado, (fim - inicio)

def buscar_dados_open_library(isbn):
    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        dados = r.json()
        info = dados.get(f"ISBN:{isbn}")
        if not info:
            return None
        titulo = info.get("title", "Título desconhecido")
        autores = ", ".join(a["name"] for a in info.get("authors", [])) if info.get("authors") else "Autor desconhecido"
        data = info.get("publish_date", "Ano desconhecido")
        return {"titulo": titulo, "autor": autores, "data_publicacao": data}
    except:
        return None

# ========================= CLASSE LIVRO =========================

class Livro:
    def __init__(self, titulo, autor, data_publicacao, isbn=None):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = int(data_publicacao) if str(data_publicacao).isdigit() else data_publicacao
        self.isbn = isbn

    def __str__(self):
        isbn_str = f" | ISBN: {self.isbn}" if self.isbn else ""
        return f"{self.titulo} — {self.autor} ({self.data_publicacao}){isbn_str}"

# ========================= CLASSE BIBLIOTECA =========================

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.hash_isbn = {}
        self.criterios_validos = ["titulo", "autor", "data_publicacao"]

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        if livro.isbn:
            self.hash_isbn[livro.isbn] = livro

    def busca_linear(self, criterio, valor):
        valor = str(valor).lower()
        return [l for l in self.livros if valor in str(getattr(l, criterio)).lower()]

    def busca_binaria(self, criterio, valor):
        lista = sorted(self.livros, key=lambda l: getattr(l, criterio))
        valor = str(valor).lower()
        ini, fim = 0, len(lista) - 1
        resultados = []
        while ini <= fim:
            m = (ini + fim) // 2
            cmp = str(getattr(lista[m], criterio)).lower()
            if valor == cmp or valor in cmp:
                resultados.append(lista[m])
                break
            elif valor < cmp:
                fim = m - 1
            else:
                ini = m + 1
        return resultados

    # ------------ ORDENAÇÕES ------------

    def bubble_sort(self, lista, criterio):
        lista = deepcopy(lista)
        n = len(lista)
        for i in range(n):
            for j in range(n - 1 - i):
                if str(getattr(lista[j], criterio)).lower() > str(getattr(lista[j+1], criterio)).lower():
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def insertion_sort(self, lista, criterio):
        lista = deepcopy(lista)
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            while j >= 0 and str(getattr(lista[j], criterio)).lower() > str(getattr(chave, criterio)).lower():
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        return lista

    def timsort(self, lista, criterio):
        return sorted(lista, key=lambda l: getattr(l, criterio))

# ========================= GUI TKINTER =========================

biblioteca = Biblioteca()

def atualizar_lista(livros=None):
    tabela.delete(*tabela.get_children())
    livros = livros if livros is not None else biblioteca.livros
    for livro in livros:
        tabela.insert("", tk.END, values=(livro.titulo, livro.autor, livro.data_publicacao, livro.isbn))

def adicionar_manual():
    titulo = input_titulo.get()
    autor = input_autor.get()
    ano = input_ano.get()
    isbn = input_isbn.get() or None

    if not titulo or not autor or not ano:
        messagebox.showerror("Erro", "Preencha título, autor e ano.")
        return
    livro = Livro(titulo, autor, ano, isbn)
    biblioteca.adicionar_livro(livro)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

def adicionar_por_isbn():
    isbn = input_isbn.get()
    if not isbn:
        messagebox.showerror("Erro", "Digite um ISBN.")
        return
    dados = buscar_dados_open_library(isbn)
    if not dados:
        messagebox.showerror("Erro", "ISBN não encontrado na Open Library.")
        return
    livro = Livro(dados["titulo"], dados["autor"], dados["data_publicacao"], isbn)
    biblioteca.adicionar_livro(livro)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Livro importado via API!")

def buscar():
    criterio = combo_criterio.get()
    valor = input_busca.get()
    metodo = combo_busca.get()

    funcoes = {"Linear": biblioteca.busca_linear, "Binária": biblioteca.busca_binaria}
    resultados, tempo = medir_tempo(funcoes[metodo], criterio, valor)
    atualizar_lista(resultados)
    messagebox.showinfo("Busca concluída", f"Tempo: {tempo:.6f} s\n{len(resultados)} resultados.")

def ordenar():
    criterio = combo_criterio.get()
    metodo = combo_ordenacao.get()
    funcoes = {
        "Bubble Sort": biblioteca.bubble_sort,
        "Insertion Sort": biblioteca.insertion_sort,
        "Timsort": biblioteca.timsort
    }
    lista_ord, tempo = medir_tempo(funcoes[metodo], biblioteca.livros, criterio)
    atualizar_lista(lista_ord)
    messagebox.showinfo("Ordenação concluída", f"Tempo: {tempo:.6f} s")

# ========================= INTERFACE =========================

janela = tk.Tk()
janela.title("Sistema de Gerenciamento de Biblioteca")
janela.geometry("900x550")

frame_form = tk.LabelFrame(janela, text="Cadastro de Livros")
frame_form.pack(fill="x", padx=10, pady=5)

tk.Label(frame_form, text="Título:").grid(row=0, column=0)
input_titulo = tk.Entry(frame_form, width=30)
input_titulo.grid(row=0, column=1)

tk.Label(frame_form, text="Autor:").grid(row=1, column=0)
input_autor = tk.Entry(frame_form, width=30)
input_autor.grid(row=1, column=1)

tk.Label(frame_form, text="Ano:").grid(row=2, column=0)
input_ano = tk.Entry(frame_form, width=30)
input_ano.grid(row=2, column=1)

tk.Label(frame_form, text="ISBN:").grid(row=3, column=0)
input_isbn = tk.Entry(frame_form, width=30)
input_isbn.grid(row=3, column=1)

tk.Button(frame_form, text="Adicionar Manualmente", command=adicionar_manual).grid(row=4, column=0, pady=5)
tk.Button(frame_form, text="Importar via ISBN", command=adicionar_por_isbn).grid(row=4, column=1)

frame_busca = tk.LabelFrame(janela, text="Busca e Ordenação")
frame_busca.pack(fill="x", padx=10, pady=5)

tk.Label(frame_busca, text="Critério:").grid(row=0, column=0)
combo_criterio = ttk.Combobox(frame_busca, values=["titulo", "autor", "data_publicacao"])
combo_criterio.current(0)
combo_criterio.grid(row=0, column=1)

tk.Label(frame_busca, text="Buscar:").grid(row=0, column=2)
input_busca = tk.Entry(frame_busca)
input_busca.grid(row=0, column=3)

combo_busca = ttk.Combobox(frame_busca, values=["Linear", "Binária"], width=10)
combo_busca.current(0)
combo_busca.grid(row=0, column=4)
tk.Button(frame_busca, text="Buscar", command=buscar).grid(row=0, column=5, padx=10)

combo_ordenacao = ttk.Combobox(frame_busca, values=["Bubble Sort", "Insertion Sort", "Timsort"])
combo_ordenacao.current(2)
combo_ordenacao.grid(row=1, column=1, pady=5)
tk.Button(frame_busca, text="Ordenar", command=ordenar).grid(row=1, column=2, padx=10)

tabela = ttk.Treeview(janela, columns=("titulo", "autor", "ano", "isbn"), show="headings")
for col in ("titulo", "autor", "ano", "isbn"):
    tabela.heading(col, text=col.upper())
tabela.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()
