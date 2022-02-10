from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



#funcoes de clicar no OK, e coletar o dado do campo (entry)
def onclick_letra():
    global letra
    letra = entrada.get()
    letra = letra.lower()
    compara_letra()

def onclick_numero():
    global numero
    numero =int(num.get())
    compara_numero()


##função para exibir imagens dos números
def compara_numero(): 
    if numero == 0:
        alf = mpimg.imread('img/numeros/0.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    elif numero == 1:
        alf = mpimg.imread('img/numeros/1.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 2:
        alf = mpimg.imread('img/numeros/2.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 3:
        alf = mpimg.imread('img/numeros/3.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
    elif numero == 4:
        alf = mpimg.imread('img/numeros/4.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 5:
        alf = mpimg.imread('img/numeros/5.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 6:
        alf = mpimg.imread('img/numeros/6.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 7:
        alf = mpimg.imread('img/numeros/7.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 8:
        alf = mpimg.imread('img/numeros/8.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 9:
        alf = mpimg.imread('img/numeros/9.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif numero == 10:
        alf = mpimg.imread('img/numeros/10.jpg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    else:
        messagebox.showinfo("ERROR - Dado Inválido", "Insira apenas um número!!!")


##função para exibir imagens das letras do alfabeto
def compara_letra(): 
    if letra == 'a':
        alf = mpimg.imread('img/alfabeto/a.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
    elif letra== "b":
        alf = mpimg.imread('img/alfabeto/b.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    elif letra=="c":
        alf = mpimg.imread('img/alfabeto/c.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    elif letra=="d":
        alf = mpimg.imread('img/alfabeto/d.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    elif letra=="e":
        alf = mpimg.imread('img/alfabeto/e.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="f":
        alf = mpimg.imread('img/alfabeto/f.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="g":
        alf = mpimg.imread('img/alfabeto/g.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="h":
        alf = mpimg.imread('img/alfabeto/h.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="i":
        alf = mpimg.imread('img/alfabeto/i.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="j":
        alf = mpimg.imread('img/alfabeto/j.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="l":
        alf = mpimg.imread('img/alfabeto/l.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="m":
        alf = mpimg.imread('img/alfabeto/m.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok                

    elif letra=="n":
        alf = mpimg.imread('img/alfabeto/n.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
        
    elif letra=="o":
        alf = mpimg.imread('img/alfabeto/o.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok
    elif letra=="p":
        alf = mpimg.imread('img/alfabeto/p.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="q":
        alf = mpimg.imread('img/alfabeto/q.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="r":
        alf = mpimg.imread('img/alfabeto/r.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="s":
        alf = mpimg.imread('img/alfabeto/s.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()#ok

    elif letra=="t":
        alf = mpimg.imread('img/alfabeto/t.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="u":
        alf = mpimg.imread('img/alfabeto/u.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="v":
        alf = mpimg.imread('img/alfabeto/v.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="x":
        alf = mpimg.imread('img/alfabeto/x.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="z":
        alf = mpimg.imread('img/alfabeto/z.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="k":
        alf = mpimg.imread('img/alfabeto/k.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="y":
        alf = mpimg.imread('img/alfabeto/y.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    elif letra=="w":
        alf = mpimg.imread('img/alfabeto/w.jpeg')
        plt.imshow(alf)
        imgplot = plt.imshow(alf)
        plt.show()

    else:
        messagebox.showinfo("ERROR - Dado Inválido", "Insira apenas uma letra do alfabeto!!!")


##funcoes para exibir as imagens dos dias da semana
     
def domingo():
    semana = mpimg.imread("img/semana/8.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()  

def segunda():
    semana = mpimg.imread("img/semana/2.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()   

def terca():
    semana = mpimg.imread("img/semana/3.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()

def quarta():
    semana = mpimg.imread("img/semana/4.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()

def quinta():
    semana = mpimg.imread("img/semana/5.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()
    
def sexta():
    semana = mpimg.imread("img/semana/6.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()

def sabado():
    semana = mpimg.imread("img/semana/7.jpg")
    plt.imshow(semana)
    imgplot = plt.imshow(semana)
    plt.show()
    
##funcoes para exibir as imagens dos Meses
def jan():
    mes =mpimg.imread ("img/meses/01.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()
    
def fev():
    mes =mpimg.imread ("img/meses/02.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def mar():
    mes =mpimg.imread ("img/meses/03.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def abr():
    mes =mpimg.imread ("img/meses/04.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()
    
def mai():
    mes =mpimg.imread ("img/meses/05.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def jun():
    mes =mpimg.imread ("img/meses/06.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def jul():
    mes =mpimg.imread ("img/meses/07.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def ago():
    mes =mpimg.imread ("img/meses/08.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def setem():
    mes =mpimg.imread ("img/meses/09.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def out():
    mes =mpimg.imread ("img/meses/10.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def nov():
    mes =mpimg.imread ("img/meses/11.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()

def dez():
    mes =mpimg.imread ("img/meses/12.jpg")
    plt.imshow(mes)
    imgplot = plt.imshow(mes)
    plt.show()



##funcção que exibe os sinais uteis
def agua():
    sinal = mpimg.imread("img/uteis/agua.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def amigo():
    sinal = mpimg.imread("img/uteis/amigo.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def banheiro():
    sinal = mpimg.imread("img/uteis/banheiro.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def casa():
    sinal = mpimg.imread("img/uteis/casa.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def comer():
    sinal = mpimg.imread("img/uteis/comer.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def entender():
    sinal = mpimg.imread("img/uteis/entender.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def estudar():
    sinal = mpimg.imread("img/uteis/estudar.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def familia():
    sinal = mpimg.imread("img/uteis/familia.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def fome():
    sinal = mpimg.imread("img/uteis/fome.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def obrigado():
    sinal = mpimg.imread("img/uteis/obrigado.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def amo():
    sinal = mpimg.imread("img/uteis/te_amo.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def trabalhar():
    sinal = mpimg.imread("img/uteis/trabalhar.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

#Funcoes para abrir imagem das cores
def branco():
    sinal = mpimg.imread("img/cores/branco.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def amarelo():
    sinal = mpimg.imread("img/cores/amarelo.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def verde():
    sinal = mpimg.imread("img/cores/verde.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def azul():
    sinal = mpimg.imread("img/cores/azul.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def marrom():
    sinal = mpimg.imread("img/cores/marrom.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def vermelho():
    sinal = mpimg.imread("img/cores/vermelho.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def laranja():
    sinal = mpimg.imread("img/cores/laranja.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()

def preto():
    sinal = mpimg.imread("img/cores/preto.jpg")
    plt.imshow(sinal)
    imgplot = plt.imshow(sinal)
    plt.show()    
# Janela do Alfabeto
def menu_alfabeto():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Alfabeto")
    janela.config(bg="white")
    texto = Label(janela, text="Informe a letra que quer aprender:")
    texto.pack()
    global entrada
    entrada = Entry(janela)
    entrada.pack(pady=10)
    bt= Button(janela, text="OK", command=onclick_letra)
    bt.pack() 
    b0 = Button(janela, text='Voltar ao Menu', command=menu)
    b0.pack(pady=350, ipadx=10, ipady=4)    


##Janela dos números
def menu_numeros():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Numeros")
    janela.config(bg="white")
    texto = Label(janela, text="Informe a numero que quer aprender:")
    texto.pack()
    global num
    num = Entry(janela)
    num.pack()
    bt= Button(janela, text="OK", command=onclick_numero)
    bt.pack() 
    b0 = Button(janela, text='Voltar ao Menu', command=menu)
    b0.pack(pady=350, ipadx=10, ipady=4)
    


## Janelas dos Menus / Contruindo janelas para cada botão selecionado
def menu_dias():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Aprendendo Libras - Dias da semana")
    janela.config(bg="white")
    texto = Label(janela, text="Clique no dia que deseja aprender")
    texto.pack()

    b0 = Button (janela, text='Domingo' , background="orange", width="20", height="4", command=domingo)
    b0.place(x=880, y=250)

    b1 = Button (janela, text='Segunda', background="red", width="20", height="4", command=segunda)
    b1.place(x=680, y=150)

    b2 = Button (janela, text='Terça', background="yellow", width="20", height="4", command=terca)
    b2.place(x=880, y=150)

    b3 = Button (janela, text='Quarta', background="blue", width="20", height="4", command=quarta)
    b3.place(x=1080, y=150)

    b4 = Button (janela, text='Quinta', background="green", width="20", height="4", command=quinta)
    b4.place(x=680, y=350)

    b5 = Button (janela, text='Sexta', background="purple", width="20", height="4", command=sexta)
    b5.place(x=880, y=350)

    b6 = Button (janela, text='Sábado' , background="white", width="20", height="4", command=sabado)
    b6.place(x=1080, y=350)

    b7 = Button(janela, text='Voltar ao Menu', command=menu)
    b7.pack(pady=450, ipadx=10, ipady=4)

##Janela com as cores  
def menu_cor():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Aprendendo Libras - Cores")
    janela.config(bg="white")
    texto = Label(janela, text="Clique na cor que deseja aprender")
    texto.pack()

    b1 = Button (janela, text='Branco' , background="white", width="20", height="4", command=branco)
    b1.place(x=880, y=250)

    b2 = Button (janela, text='Amarelo', background="yellow", width="20", height="4", command=amarelo)
    b2.place(x=680, y=150)

    b3 = Button (janela, text='Vermelho', background="red", width="20", height="4", command=vermelho)
    b3.place(x=880, y=150)

    b4 = Button (janela, text='Azul', background="blue", width="20", height="4", command=azul)
    b4.place(x=1080, y=150)

    b5 = Button (janela, text='Verde', background="green", width="20", height="4", command=verde)
    b5.place(x=680, y=350)

    b6 = Button (janela, text='Preto', background="black", width="20", height="4", command=preto)
    b6.place(x=880, y=350)

    b7 = Button (janela, text='Marrom' , background="#8B4513", width="20", height="4", command=marrom)
    b7.place(x=1080, y=350)

    b0 = Button(janela, text='Voltar ao Menu', command=menu)
    b0.pack(pady=450, ipadx=10, ipady=4)


 ##Janela com sinais Úteis
def menu_sinais():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Aprendendo Libras - Sinais Úteis")
    janela.config(bg="white")
    texto = Label(janela, text="Aprendendo alguns Sinais Uteis!")
    texto.pack()

    b1 = Button (janela, text='Agua', background="white", width="20", height="4", command=agua)
    b1.place(x=680, y=150)

    b2 = Button (janela, text='Amigo', background="white", width="20", height="4", command=amigo)
    b2.place(x=880, y=150)

    b3 = Button (janela, text='Banheiro', background="white", width="20", height="4", command=banheiro)
    b3.place(x=1080, y=150)

    b4 = Button (janela, text='Casa', background="white", width="20", height="4", command=casa)
    b4.place(x=680, y=250)

    b5 = Button (janela, text='Comer', background="white", width="20", height="4", command=comer)
    b5.place(x=880, y=250)

    b6 = Button (janela, text='Entender' , background="white", width="20", height="4", command=entender)
    b6.place(x=1080, y=250)

    b7 = Button (janela, text='Estudar' , background="white", width="20", height="4", command=estudar)
    b7.place(x=680, y=350)

    b8 = Button (janela, text='Família' , background="white", width="20", height="4", command=familia)
    b8.place(x=880, y=350)

    b9 = Button (janela, text='Fome' , background="white", width="20", height="4", command=fome)
    b9.place(x=1080, y=350)

    b10 = Button (janela, text='Obrigado' , background="white", width="20", height="4", command=obrigado)
    b10.place(x=680, y=450)

    b11 = Button (janela, text='Te Amo' , background="white", width="20", height="4", command=amo)
    b11.place(x=880, y=450)

    b12 = Button (janela, text='Trabalhar' , background="white", width="20", height="4", command=trabalhar)
    b12.place(x=1080, y=450)

    b0 = Button(janela, text='Voltar ao Menu', command=menu)
    b0.place (x = 880, y = 550)
 ##Janela com os meses   
def menu_meses():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Aprendendo Libras - Meses")
    janela.config(bg="white")
    texto = Label(janela, text="Aprendendo os Meses!")
    texto.pack()

    

    b1 = Button (janela, text='Janeiro', background="red", width="20", height="4", command=jan)
    b1.place(x=680, y=150)

    b2 = Button (janela, text='Fevereiro', background="yellow", width="20", height="4", command=fev)
    b2.place(x=880, y=150)

    b3 = Button (janela, text='Março', background="blue", width="20", height="4", command=mar)
    b3.place(x=1080, y=150)

    b4 = Button (janela, text='Abril', background="green", width="20", height="4", command=abr)
    b4.place(x=680, y=250)

    b5 = Button (janela, text='Maio', background="purple", width="20", height="4", command=mai)
    b5.place(x=880, y=250)

    b6 = Button (janela, text='Junho' , background="white", width="20", height="4", command=jun)
    b6.place(x=1080, y=250)

    b7 = Button (janela, text='Juhlo' , background="white", width="20", height="4", command=jul)
    b7.place(x=680, y=350)

    b8 = Button (janela, text='Agosto' , background="white", width="20", height="4", command=ago)
    b8.place(x=880, y=350)

    b9 = Button (janela, text='Setembro' , background="white", width="20", height="4", command=setem)
    b9.place(x=1080, y=350)

    b10 = Button (janela, text='Outubro' , background="white", width="20", height="4", command=out)
    b10.place(x=680, y=450)

    b11 = Button (janela, text='Novembro' , background="white", width="20", height="4", command=nov)
    b11.place(x=880, y=450)

    b12 = Button (janela, text='Dezembro' , background="white", width="20", height="4", command=dez)
    b12.place(x=1080, y=450)

    b0 = Button(janela, text='Voltar ao Menu', command=menu)
    b0.place (x = 880, y = 550)

##Função do menu principal
def menu():
    global janela
    janela.destroy()
    janela = Tk()
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.title("Aprendendo Libras")
    janela.config(bg="white")
    texto = Label(janela, text="Selecione a categoria que deseja aprender!")
    texto.pack()
 

    b1 = Button (janela, text='Alfabeto', background="red", width="20", height="4", command=menu_alfabeto)#,image=photoimage,
    b1.place(x=680, y=150)

    b2 = Button (janela, text='Numeros', background="yellow", width="20", height="4", command=menu_numeros)
    b2.place(x=880, y=150)

    b3 = Button (janela, text='Meses', background="blue", width="20", height="4", command=menu_meses)
    b3.place(x=1080, y=150)

    b4 = Button (janela, text='Dias da semana', background="green", width="20", height="4", command=menu_dias)
    b4.place(x=680, y=350)

    b5 = Button (janela, text='Cores', background="purple", width="20", height="4", command=menu_cor)
    b5.place(x=880, y=350)

    b6 = Button (janela, text='Sinais Uteis' , background="white", width="20", height="4", command=menu_sinais)
    b6.place(x=1080, y=350)

    b0 = Button(janela, text='Fechar', command=ExitApp)
    b0.pack(pady=450, ipadx=10, ipady=4)

#Finalizando o programa
def ExitApp():
    MsgBox = messagebox.askquestion ('Fechar Programa','Deseja Encerrar?',icon = 'error')
    if MsgBox == 'yes':
       janela.destroy()
       exit()
    else:
        messagebox.showinfo('Que bom!!!','Vamos aprender Mais')
        menu()
        



##Incializando programa
   
janela = Tk()
janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
janela.title("Aprendendo Libras")
janela.config(bg="white")
texto = Label(janela, text="Selecione a categoria que deseja aprender!")
texto.pack()
#photo = PhotoImage (file = "alfa2.png")
#photoimage = photo.subsample(20, 4) 

b1 = Button (janela, text='Alfabeto', background="red", width="20", height="4", command=menu_alfabeto)#,image=photoimage,
b1.place(x=680, y=150)

b2 = Button (janela, text='Numeros', background="yellow", width="20", height="4", command=menu_numeros)
b2.place(x=880, y=150)

b3 = Button (janela, text='Meses', background="blue", width="20", height="4", command=menu_meses)
b3.place(x=1080, y=150)

b4 = Button (janela, text='Dias da semana', background="green", width="20", height="4", command=menu_dias)
b4.place(x=680, y=350)

b5 = Button (janela, text='Cores', background="purple", width="20", height="4" , command=menu_cor)
b5.place(x=880, y=350)

b6 = Button (janela, text='Sinais Uteis' , background="white", width="20", height="4", command=menu_sinais)
b6.place(x=1080, y=350)

b0 = Button(janela, text='Fechar', command=ExitApp)
b0.pack(pady=450, ipadx=10, ipady=4)



janela.mainloop()
