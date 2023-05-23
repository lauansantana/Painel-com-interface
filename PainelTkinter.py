import tkinter as tk
import tkinter as Button
import tkinter as Entry
from tkinter import *
import requests

cor_dark = '#12141f'
cor_fundo = '#12141f'
cor_fundo2 = '#17192b'
cor_branco = '#ffffff'
cor_laranja = '#ff6647'

def opcao1():
    print("Opção 1 selecionada")

def opcao2():
    print("Opção 2 selecionada")

def opcao3():
    print("Opção 3 selecionada")

def entrada():
    input('Insira')


# Criar uma janela principal
janela = tk.Tk()
janela.title("Painel de Consulta")
janela.geometry("700x500")
janela.config(bg=cor_dark)


# Criar o menu Opções
menu_opcoes = tk.Menu(menu, tearoff=0)
menu_opcoes.add_command(label="IP", command=opcao1)
menu_opcoes.add_command(label="Meu IP", command=opcao2)
menu_opcoes.add_command(label="Cep", command=opcao3)

menu.add_cascade(label="Opções", menu=menu_opcoes)

# Configurar o menu principal da janela
janela.config(menu=menu)

# Iniciar o loop principal da janela
janela.mainloop()