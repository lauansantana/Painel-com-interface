import tkinter as tk
import requests

# Criar a janela principal
root = tk.Tk()

# Variável para armazenar o valor digitado no campo de entrada
cep_var = tk.StringVar()

# Função para fazer a solicitação da API e exibir os dados
def search_cep():
    cep = cep_var.get()
    if cep:
        url = "https://cep.awesomeapi.com.br/json/{}".format(cep)
        response = requests.get(url)
        data = response.json()
        display_data(data)

# Função para exibir os dados do CEP na interface
def display_data(data):
    result_label.config(text=data['address'])
    # Outros campos do CEP podem ser exibidos aqui

# Campo de entrada
cep_entry = tk.Entry(root, textvariable=cep_var)
cep_entry.pack()

# Botão
search_button = tk.Button(root, text="Buscar CEP", command=search_cep)
search_button.pack()

# Label para exibir os dados do CEP
result_label = tk.Label(root, text="")
result_label.pack()

# Iniciar a interface gráfica
root.mainloop()
