from tkinter import *
from random import choice
from functools import partial

class Mainfunctions(Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.createtabela()
        self.create_familias()

    #cria as opções para selecionar as famílias
    def create_familias(self):
        self.titulo = Label(text="Tabela Periódica")
        self.titulo.place(x=350, y=10)
        self.subtitulo = Label(text="Famílias")
        self.subtitulo.place(x=80, y= 50)
        self.alabel = Label(text="A")
        self.alabel.place(x=80, y=65)
        self.blabel = Label(text="B")
        self.blabel.place(x=120, y=65)
        self.blista = []
        self.alista = []
        i = 0
        cx = 120
        cy = 85
        while i<11:
            if i == 10:
                aux = Button(text='Especial', bg='red')
            else:
                aux = Button(text=str(i+1), bg='red')
            self.blista.append(aux)
            self.blista[i]['command'] = partial(self.adicionar_remover, (i+1) * -1)
            self.blista[i].place(x = cx, y= cy)
            i += 1
            cy += 20
        i = 0
        cx = 80
        cy = 85
        while i<8:
            aux = Button(text=str(i+1), bg='red')
            self.alista.append(aux)
            self.alista[i]['command'] = partial(self.adicionar_remover, i)
            self.alista[i].place(x = cx, y=cy)
            i += 1
            cy += 20
        self.lblsorteio = Label()
        self.lblsorteio.place(x=50, y=380)
        self.astatus = ['red', 'red', 'red', 'red', 'red', 'red', 'red','red']
        self.bstatus = ['red','red','red','red','red','red','red','red','red','red', 'red']
        self.escritor = Button(text="Mostrar", command= self.escreve_na_tela)
        self.apagador = Button(text="Apagar", command= self.apaga)
        self.escritor.place(x=50, y=340)
        self.apagador.place(x=130, y=340)

    #adiciona os elementos da família para uma lista
    def adicionar_remover(self, i):
        max = len(self.sorteio)
        if 0>i:
            i = -(i+1)
            tipo = 'b'
            if self.bstatus[i] == 'red':
                for elementos in self.bfamilias[i]:
                    self.sorteio.append(elementos)
            else:
                for elementos in self.bfamilias[i]:
                    j = 0
                    while j<=max:
                        if self.sorteio[j] == elementos:
                            del self.sorteio[j]
                            j -=1
                            max-=1
                            break
                        else:
                            j+= 1      
        else:
            tipo = 'a'
            if self.astatus[i] == 'red':
                for elementos in self.afamilias[i]:
                    self.sorteio.append(elementos)
            else:
                for elementos in self.afamilias[i]:
                    j = 0
                    while j<=len(self.sorteio):
                        if self.sorteio[j] == elementos:
                            del self.sorteio[j]
                            j -=1
                            max-=1
                            break
                        else:
                            j+= 1
        self.mudarcor(tipo, i)

    #mostra quais elementos estão na lista
    def escreve_na_tela(self):
        self.lblsorteio["text"] = ""
        i = 0
        for item in self.sorteio:
            self.lblsorteio["text"] += str(item) + " | "
            i+=1
            if i > 10:
                self.lblsorteio["text"] += "\n"
                i = 0
        
    #muda a cor do botão. Vermelho se estiver sem os elementos e azul se tiver adicionado
    def mudarcor(self, tipo, i):
        if tipo == 'a':
            if self.astatus[i] == 'red':
                self.astatus[i] = 'blue'
                self.alista[i]['bg'] = 'blue'
            else:
                self.astatus[i] = 'red'
                self.alista[i]['bg'] = 'red'
        else:
            if self.bstatus[i] == 'red':
                self.bstatus[i] = 'blue'
                self.blista[i]['bg'] = 'blue'
            else:
                self.bstatus[i] = 'red'
                self.blista[i]['bg'] = 'red'

    #apaga o texto mostrado      
    def apaga(self):
        self.lblsorteio["text"] = ""

    #lista com elementos da tabela periódica
    def createtabela(self):
        self.sorteio = []
        self.afamilias = [['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'], ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra'], ['B', 'Al', 'Ga', 'In', 'Ti', 'Nh'],
                          ['C', 'Si', 'Ge', 'Sn', 'Pb', 'Fl'], ['N', 'P', 'As', 'Sb', 'Bi', 'Mc'], ['O', 'S', 'Se', 'Te', 'Po', 'Lv'],
                          ['F', 'Cl', 'Br', 'I', 'At', 'Ts'], ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']]
        self.bfamilias = [['Sc', 'Y'], ['Ti', 'Zr', 'Hf', 'Rf'], ['V', 'Nb', 'Ta', 'Db'], ['Cr', 'Mo', 'W', 'Sg'],
                          ['Mn', 'Tc', 'Re', 'Bh'], ['Fe', 'Ru', 'Os', 'Hs'], ['Co', 'Rh', 'Ir', 'Mt'], ['Ni', 'Pd', 'Pt', 'Ds']
                          , ['Cu', 'Ag', 'Au', 'Rg'], ['Zn', 'Cd', 'Hg', 'Cn'], ["La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"]]