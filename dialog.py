import tkinter as tk
from tkinter import messagebox

def exibir_caixa_dialogo_info(mensagem, titulo="Informação"):
    tk.Tk().withdraw()
    messagebox.showinfo(titulo, mensagem)

def exibir_caixa_dialogo_erro(mensagem, titulo="Erro"):
    tk.Tk().withdraw()
    messagebox.showerror(titulo, mensagem)

def obter_input_caixa_dialogo(mensagem, titulo="Entrada"):
    tk.Tk().withdraw()
    return simpledialog.askstring(titulo, mensagem)
