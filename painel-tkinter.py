import requests
import tkinter as tk
from tkinter import *

cor_dark = '#12141f'
cor_fundo = '#12141f'
cor_fundo2 = '#17192b'
cor_branco = '#ffffff'
cor_laranja = '#ff6647'
cor_azul = '#2C94F5'

def limpar():
    texto_resultado.config(text='')
    texto_meuip.config(text='')
    texto_ip.config(text='')
    texto_cnpj.config(text='')

def requisicao_ip():
    ip = ip_var.get()
    requisicaoip = requests.get('http://ip-api.com/json/{}'.format(ip))
    requisicaoip2 = requisicaoip.json()

    ip = requisicaoip2 ['query']
    pais1 = requisicaoip2['country']
    regiao = requisicaoip2['regionName']
    cidade = requisicaoip2['city']
    provedor = requisicaoip2['isp']
    latitude = requisicaoip2['lat']
    longitude = requisicaoip2['lon']

    texto = f'''
    ❖ IP: {ip}

    ❖ País: {pais1}

    ❖ Regiao: {regiao}

    ❖ Cidade: {cidade}

    ❖ Provedor: {provedor}

    ❖ Latitude: {latitude}

    ❖ Longitude: {longitude}
    '''
    texto_ip['text'] = texto

def requisicao_meuip():
    requisicaomeuip = requests.get('http://ip-api.com/json/')
    requisicaomeuip2 = requisicaomeuip.json()
    
    ip = requisicaomeuip2 ['query']
    pais = requisicaomeuip2['country']
    regiao = requisicaomeuip2['regionName']
    cidade = requisicaomeuip2['city']
    provedor = requisicaomeuip2['isp']
    latitude = requisicaomeuip2['lat']
    longitude = requisicaomeuip2['lon']

    texto = f'''
    ❖ IP: {ip}

    ❖ País: {pais}

    ❖ Regiao: {regiao}

    ❖ Cidade: {cidade}

    ❖ Provedor: {provedor}

    ❖ Latitude: {latitude}

    ❖ Longitude: {longitude}
    '''
    texto_meuip['text'] = texto

def requisicao_cep():
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
    ❖ CEP: {cep}

    ❖ Endereço: {endereco}

    ❖ Bairro: {bairro}

    ❖ Cidade: {cidade}

    ❖ Estado: {estado}

    ❖ DDD: {ddd}

    ❖ Latitude: {latitude}
    
    ❖Longitude: {longitude}'''
    texto_resultado['text'] = texto

def requisicao_cnpj():
    cnpj = cnpj_var.get()
    requisicao_cnpj = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj))
    requisicaocnpj2 = requisicao_cnpj.json()

    cnpj = requisicaocnpj2['cnpj']
    abertura = requisicaocnpj2['abertura']
    situacao = requisicaocnpj2['tipo']
    tipo = requisicaocnpj2['nome']
    nome_fantasia = requisicaocnpj2['fantasia']
    porte = requisicaocnpj2['porte']
    atividade_principal = requisicaocnpj2['atividade_principal'][0]
    atividade_secundaria = requisicaocnpj2['atividades_secundarias'][0]['text']
    logradouro = requisicaocnpj2['logradouro']
    numero = requisicaocnpj2['numero']
    complemento = requisicaocnpj2['complemento']
    municipio = requisicaocnpj2['municipio']
    bairro = requisicaocnpj2['bairro']
    uf = requisicaocnpj2['uf']
    cep = requisicaocnpj2['cep']
    email = requisicaocnpj2['email']
    telefone = requisicaocnpj2['telefone']
    ultima_atualizaçao = requisicaocnpj2['ultima_atualizacao']
    status = requisicaocnpj2['status']
    capital_social = requisicaocnpj2['capital_social']
    
    texto = f'''    ❖ CNPJ: {cnpj}
    ❖ Abertura: {abertura}
    ❖ Situação: {situacao}
    ❖ Tipo: {tipo}
    ❖ Nome Fantasia: {nome_fantasia}
    ❖ Atividade Principal: {atividade_principal}
    ❖ Atividade Secundária: {atividade_secundaria}
    ❖ Logradouro: {logradouro}
    ❖ Número: {numero}
    ❖ Complemento: {complemento}
    ❖ Município: {municipio}
    ❖ Bairro: {bairro}
    ❖ UF: {uf}
    ❖ Cep: {cep}
    ❖ E-mail: {email}
    ❖ Telefone: {telefone}
    ❖ Última atualização: {ultima_atualizaçao}
    ❖ Status: {status}
    ❖ Capital Social: {capital_social}
    '''
    texto_cnpj['text'] = texto


# Criar a janela principal
janela = tk.Tk()
janela.title("Painel")
janela.geometry("700x460")
janela.config(bg=cor_dark)

#titulo
tela = Frame(janela, width=700, height=50, bg=cor_fundo2)
tela.place(x=0, y=0)
titulo = tk.Label(janela, text="PAINEL DE CONSULTA", font='ivy 17 bold', bg=cor_fundo, fg=cor_laranja, relief=RIDGE,)
titulo.place(x=230, y=10)

#tela de print
tela_print = Frame(janela, width=465, height=365, bg=cor_fundo2)
tela_print.place(x=220, y=70)

#aviso
obs = tk.Label(janela, text="*OBS: Caso não retorne nenhum dado na consulta, entrada inválida ou não encontrada na base de dados.", font='ivy 10', bg=cor_fundo, fg=cor_laranja)
obs.place(x=1, y=438)

# Função para armazenar o valor digitado no campo de entrada
def save_input_value(entry, variable):
    value = entry.get()
    if value:
        variable.set(value)

# Variáveis para armazenar os valores digitados
cnpj_var = tk.StringVar()
ip_var = tk.StringVar()
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
meuip_label.place(x=3, y=404)

cep_label = tk.Label(janela, text="CEP:", bg=cor_fundo2, fg=cor_branco, font='ivy 10 bold', relief=RAISED)
cep_label.place(x=3, y=278)
cep_entry = tk.Entry(janela, width=20, relief=SUNKEN)
cep_entry.place(x=3, y=301)

# Botões
cnpj_button = tk.Button(janela, text="OK", bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(cnpj_entry, cnpj_var))
cnpj_button.place(x=130, y=80)

ip_button = tk.Button(janela, text="OK",bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(ip_entry, ip_var))
ip_button.place(x=130, y=178)


cep_button = tk.Button(janela, text="OK", bg=cor_laranja, fg=cor_branco, font=('ivy 8 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: save_input_value(cep_entry, cep_var))
cep_button.place(x=130, y=298)

#PRINT CEP
print_button = tk.Button(janela, text="Print", bg=cor_azul,font=' ivy 8 bold', relief=RAISED, overrelief=RIDGE, command=requisicao_cep)
print_button.place(x=160, y=298)
texto_resultado = Label(janela, text='', bg=cor_fundo2, fg=cor_branco, justify= LEFT, font=('ivy 14')) #Resultado da consulta
texto_resultado.place(x=220, y=70)

#PRINT MEU IP
print_button = tk.Button(janela, text="Print", font=' ivy 8 bold', bg=cor_azul, fg=cor_fundo2 , relief=RAISED, overrelief=RIDGE, command=requisicao_meuip)
print_button.place(x=60, y=403)
texto_meuip = Label(janela, text='', bg=cor_fundo2, fg=cor_branco, justify= LEFT, font=('ivy 15')) #Resultado da consulta
texto_meuip.place(x=220, y=80)

#PRINT IP
print_button = tk.Button(janela, text="Print", font=' ivy 8 bold', bg=cor_azul, fg=cor_fundo2 , relief=RAISED, overrelief=RIDGE, command=requisicao_ip)
print_button.place(x=160, y=178)
texto_ip = Label(janela, text='', bg=cor_fundo2, fg=cor_branco, justify= LEFT, font=('ivy 15')) #Resultado da consulta
texto_ip.place(x=220, y=80)

#PRINT CNPJ
print_button = tk.Button(janela, text="Print", font=' ivy 8 bold', bg=cor_azul, fg=cor_fundo2 , relief=RAISED, overrelief=RIDGE, command=requisicao_cnpj)
print_button.place(x=160, y=80)
texto_cnpj = Label(janela, text='', bg=cor_fundo2, fg=cor_branco, justify= LEFT, font=('ivy 13')) #Resultado da consulta
texto_cnpj.place(x=220, y=70)

#bbotao limpar
b1 = Button(janela, command= limpar, text="Limpar", bg=cor_azul, fg=cor_fundo2, relief=RAISED, overrelief=RIDGE)
b1.place(x=160, y=402)

# Iniciar a interface gráfica
janela.mainloop()
