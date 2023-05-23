import requests
import tkinter as tk
from tkinter import *

cor_dark = '#12141f'
cor_fundo = '#12141f'
cor_fundo2 = '#17192b'
cor_branco = '#ffffff'
cor_laranja = '#ff6647'

'''def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'
    DÓLAR: {cotacao_dolar}
    EURO: {cotacao_euro}
    BTC: {cotacao_btc}'
   
    texto_resultado['text'] = texto
'''
def pegar_cotacoes():
    cep = cep_var.get()
    requisicao = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep))
    requisicao_cep = requisicao.json()
    cep = requisicao_cep['cep']
    endereco = requisicao_cep['address']
    bairro = requisicao_cep['district']
    cidade = requisicao_cep['city']
    estado = requisicao_cep['state']
    ddd = requisicao_cep['ddd']
    latitude = requisicao_cep['lat']
    longitude = requisicao_cep['lng']
    texto = f'''
    CEP: {cep}
    Endereço: {endereco}
    Bairro: {bairro}
    Cidade: {cidade}
    Estado: {estado}
    DDD: {ddd}
    Latitude: {'lat'}
    
    '''
    texto_resultado['text'] = texto

# Criar a janela principal
janela = tk.Tk()
janela.title("Painel")
janela.geometry("700x450")
janela.config(bg=cor_dark)

#titulo
tela = Frame(janela, width=700, height=50, bg=cor_fundo2)
tela.place(x=0, y=0)
titulo = tk.Label(janela, text="PAINEL DE CONSULTA", font='ivy 17 bold', bg=cor_fundo, fg=cor_laranja, relief=RIDGE)
titulo.place(x=230, y=10)

#tela de print
tela_print = Frame(janela, width=465, height=365, bg=cor_fundo2)
tela_print.place(x=220, y=70)

# Função para armazenar o valor digitado no campo de entrada
def save_input_value(entry, variable):
    value = entry.get()
    if value:
        variable.set(value)

# Variáveis para armazenar os valores digitados
cnpj_var = tk.StringVar()
ip_var = tk.StringVar()
meuip_var = tk.StringVar()
cep_var = tk.StringVar()

# Campos de entrada
cnpj_label = tk.Label(janela, text="CNPJ:", bg=cor_fundo2, fg=cor_branco, font='ivy 10 bold', relief=RAISED)
cnpj_label.place(x=3, y=57)
cnpj_entry = tk.Entry(janela, width=20, relief=SUNKEN)
cnpj_entry.place(x=3, y=82)

ip_label = tk.Label(janela, text="IP", bg=cor_fundo2, fg=cor_branco, font='ivy 10 bold', relief=RAISED)
ip_label.place(x=3, y=157)
ip_entry = tk.Entry(janela, width=20, relief=SUNKEN)
ip_entry.place(x=3, y=181)

meuip_label = tk.Label(janela, text="MEU IP:", bg=cor_fundo2, fg=cor_branco, font='ivy 10 bold', relief=RAISED)
meuip_label.place(x=3, y=277)
meuip_entry = tk.Entry(janela, width=20, relief=SUNKEN)
meuip_entry.place(x=3, y=301)

cep_label = tk.Label(janela, text="CEP:", bg=cor_fundo2, fg=cor_branco, font='ivy 10 bold', relief=RAISED)
cep_label.place(x=3, y=380)
cep_entry = tk.Entry(janela, width=20, relief=SUNKEN)
cep_entry.place(x=3, y=404)

# Botões
cnpj_button = tk.Button(janela, text="OK", bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(cnpj_entry, cnpj_var))
cnpj_button.place(x=130, y=80)

print_button = tk.Button(janela, text="print", command=pegar_cotacoes)
print_button.place(x=160, y=80)
texto_resultado = Label(janela, text='', bg=cor_fundo, fg=cor_branco,font=('ivy 10')) #Resultado da consulta
texto_resultado.grid(column=0, row=2) #grid redimensiona texto


ip_button = tk.Button(janela, text="OK",bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(ip_entry, ip_var))
ip_button.place(x=130, y=178)

meuip_button = tk.Button(janela, text="OK", bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(meuip_entry, meuip_var))
meuip_button.place(x=130, y=298)

cep_button = tk.Button(janela, text="OK", bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(cep_entry, cep_var))
cep_button.place(x=130, y=401)

# Iniciar a interface gráfica
janela.mainloop()
