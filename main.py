from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# importando -------
import requests
import json

# cores -------

co0 = "#444466"  # preta / black
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul / blue

fundo = "#484f60" #background

# criando a janela do app
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)


# divivindo a jenela em 2 frames --------
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)



# função para pegar dados

def info():
	api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL'

	# -- Pegando os dados da API (HTTP REQUEST) --------
	response = requests.get(api_link)

	# -- Convertendo os dados para JSON --------
	dados = response.json()

	# -- Valor em USD
	valor_usd = float(dados['USD'])
	valor_formatado_usd = "$ {:,.3f}".format(valor_usd)
	l_p_usd['text'] = 'Em Dólares é: $ '+ valor_formatado_usd

 	# -- Valor em Euro
	valor_euro = float(dados['EUR'])
	valor_formatado_euro = "€ {:,.3f}".format(valor_euro)
	l_p_euro['text'] = 'Em Euros é: € '+ valor_formatado_euro


	# -- Valor em Reais
	valor_reais = float(dados['BRL'])
	valor_formatado_reais = "R$ {:,.3f}".format(valor_reais)
	l_p_reais['text'] = 'Em Reais é: R$ '+valor_formatado_reais


	# -- Valor em AOA
	valor_kz = float(dados['AOA'])
	valor_formatado_kz = "Kz {:,.3f}".format(valor_kz)
	l_p_kz['text'] = 'Em Kwanzas é: AOA '+ valor_formatado_kz


	frame_baixo.after(1000, info)


# Configurando o frame de cima --------
imagem = Image.open('images/bitcoin_94576.png')
imagem = imagem.resize((30,30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima,text='Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
l_nome.place(x=50, y=5)

# Configurando o frame de baixo --------
l_p_usd = Label(frame_baixo,text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_usd.place(x=10, y=50)

l_p_euro = Label(frame_baixo,text='',bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_euro.place(x=10, y=130)

l_p_reais = Label(frame_baixo,text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_reais.place(x=10, y=160)

l_p_kz = Label(frame_baixo,text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_p_kz.place(x=10, y=190)



info()

janela.mainloop()
