from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

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

# Configurando o frame de cima --------
imagem = Image.open('images/bitcoin_94576.png')
imagem = imagem.resize((30,30), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)




janela.mainloop()
