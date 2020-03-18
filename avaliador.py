from tabela import *
from tkinter import *
from random import choice
from functools import partial

class Janela(Mainfunctions):
    #construtor da interface para avaliadores
    def __init__(self):
        super().__init__()
        self.qntacertos = 0
        self.create_tabela_aluno()
        self.campo()
        self.iniciado = False

#construir a interface:
    #método para iniciar introduzir a quantidade de alunos que irão fazer a chamada
    def create_tabela_aluno(self):
        self.lblaluno = Label(text="Insira o último número da chamada")
        self.lblaluno.place(x=320, y=50)
        self.numerodealunos = Entry()
        self.numerodealunos.place(x=350, y=80)
        self.iniciar_chamada = Button(text="Iniciar chamada oral", fg ='red')
        self.iniciar_chamada.place(x=350, y = 110)
        self.iniciar_chamada["command"] = self.comecar_avaliacao
        self.chamado = Label(text="Para iniciar a chamada:\nDigite a quantidade de alunos clique no botão", fg='red')
        self.chamado.place(x=325, y=140)

    #campo objetos para avaliação
    def campo(self):
        self.nome = Entry()
        self.lblnome = Label(text="Nome")
        self.lblnome.place(x=320, y=180)
        self.nome.place(x=360, y=180)
        self.acertos = Label(text="0 Acertos")
        self.acertos.place(x=370, y=210)
        self.create_avaliador()
        self.alunos = []
        self.acertoalunos = []
        self.submeter = Button(text="Submeter", command=self.submit)
        self.submeter.place(x=320, y=240)
        self.reseta = Button(text="Retornar", command= self.retornar)
        self.reseta.place(x=400, y=240)
        self.salvar = Button(text="Salvar em .txt", command=self.save)
        self.salvar.place(x=360, y=300)
        self.lblsave = Label(text="Não salvo", fg='red')
        self.lblsave.place(x=360, y=340)

    #opções para realizar a chamada oral
    def create_avaliador(self):
        self.quantidade = Entry(width=10)
        self.quantidade.place(x= 700, y= 50)
        self.lblqnt = Label(text="Quantidade de elementos")
        self.lblqnt.place(x=560, y=50)
        self.starter = Button(text="comecar", command=self.startav)
        self.starter.place(x=580, y= 80)
        self.lblelemento = Label(text="X")
        self.lblelemento.place(x=630, y= 120)
        self.resetelementos()
        self.botaoanterior = Button(text="<-", command=self.anterior)
        self.botaoanterior.place(x=610, y= 140)
        self.botaoavancar = Button(text="->", command=self.avancar)
        self.botaoavancar.place(x=640, y= 140)
        self.acertou = Button(text="Acertou", command=self.acertou)
        self.errou = Button(text="Errou", command=self.avancar)
        self.acertou.place(x=580, y=180)
        self.errou.place(x=640, y=180)

#métodos:
    #seleciona o primeiro aluno para a avaliação
    def comecar_avaliacao(self):
        if not self.iniciado:
            tamanho = int(self.numerodealunos.get())
            self.chamada = []
            for i in range(tamanho):
                self.chamada.append(i+1)
            escolhido = choice(self.chamada)
            self.remover(escolhido)
            self.chamado["text"] = "Chamada iniciada!\no primeiro escolhido é o número " + str(escolhido)

    #salva alunos e notas em um arquivo de texto
    def save(self):
        #salva em arquivo .txt
        if len(self.alunos) == 0:
            return
        file = open("resultados.txt", "w+")
        file.write("Resultados:\n")
        for i in range(len(self.alunos)):
            file.write("{}  =  {}%\n".format(self.alunos[i], round(self.acertoalunos[i], 2)))
        file.close()
        self.lblsave["text"] = "Salvo com " + str(len(self.alunos)) + (" alunos" if len(self.alunos)>1 else " aluno")
        self.lblsave["fg"] = 'green'

    #redefine o número de acertos e a pessoa que está fazendo o teste
    def retornar(self):
        self.nome.delete(0, END)
        self.qntacertos = 0
        self.acertos["text"] = "0 Acertos"
        self.reset_tabela()

    #armazena o nome e a pontuação da pessoa e sorteia um novo número
    def submit(self):
        if len(str(self.nome.get())) == 0:
            return
        self.alunos.append(str(self.nome.get()))
        x = 100 *(self.qntacertos/(int(self.quantidade.get())))
        self.acertoalunos.append(x)
        self.retornar()
        self.reset_tabela()
        if len(self.chamada) == 0:
            self.chamado["text"] = "todos os alunos foram avaliados!"
        else:
            escolhido = choice(self.chamada)
            self.chamado["text"]= "Número " + str(escolhido) + " Foi selecionado!"
            self.remover(escolhido)

#métodos da avaliação:       
    #inicia o teste de um aluno
    def startav(self):
        self.resetelementos()
        self.getelementos()
        self.reset_tabela()
        self.qntacertos = 0
        self.acertos["text"] = "0 Acertos"
        
    #mostra um acerto a mais para o aluno
    def atualiza_acertos(self):
        self.qntacertos += 1
        self.acertos["text"] = str(self.qntacertos) + " Acertos"

    #remove o aluno da lista de espera para avaliação
    def remover(self, valor):
        for i in range(len(self.chamada)):
            if self.chamada[i] == valor:
                del self.chamada[i]
                return

    #adiciona um acerto no teste de um aluno e mostra o próximo elemento
    def acertou(self):
        if self.qntacertos == int(self.quantidade.get()):
            pass
        else:
            if self.tabela_acertos[self.posicao] == 0:
                self.atualiza_acertos()
                self.tabela_acertos[self.posicao] = 1
            self.avancar()

    #marca o erro e mostra o próximo elemento
    def errou(self):
        if self.qntacertos == int(self.quantidade.get()):
            pass
        else:
            if self.tabela_acertos[self.posicao] == 0:
                self.tabela_acertos[self.posicao] = 1
            self.avancar()
            
#métodos da avaliação
    #adquire os elementos que irão ser mostrados na avaliação, de forma aleatória
    def getelementos(self):
        numeroderepeticoes = int(self.quantidade.get())
        for i in range(numeroderepeticoes):
            self.elementos.append(choice(self.sorteio))
        self.lblelemento["text"] = str(self.elementos[0])
        self.posicao = 0
        self.reset_tabela()

    #avança para o próximo elemento da avaliação
    def avancar(self):
        if self.posicao == len(self.elementos) - 1:
            return
        self.posicao += 1
        self.lblelemento["text"] = str(self.elementos[self.posicao])

    #regressa um elemento da avaliação
    def anterior(self):
        if (self.posicao > 0):
            self.posicao -= 1
            self.lblelemento["text"] = str(self.elementos[self.posicao])
            
    #zera o número de acertos e erros de alguém, para que o mesmo possa tentar o elemento depois
    def reset_tabela(self):
        self.tabela_acertos = []
        numeroderepeticoes = int(self.quantidade.get())
        for i in range(numeroderepeticoes):
            self.tabela_acertos.append(0)

    #remove todos os elementos que estão sendo usados em avaliação
    def resetelementos(self):
        self.elementos = []

