from tkinter import *

CalculadorDeMédiasRoot = Tk()

def MédiaGeométrica():
    textoX = Label(CalculadorDeMédiasRoot, text='Insira o valor 1')
    entryx = Entry(CalculadorDeMédiasRoot)
    textoX.pack()
    entryx.pack()
    textoY = Label(CalculadorDeMédiasRoot, text='Insira o valor 2')
    entryy = Entry(CalculadorDeMédiasRoot)
    textoY.pack()
    entryy.pack()
    textoZ = Label(CalculadorDeMédiasRoot, text='Insira o valor 3')
    entryz = Entry(CalculadorDeMédiasRoot)
    textoZ.pack()
    entryz.pack()
    def MédiaGeométricaCalcular():
        x = float(entryx.get())
        y = float(entryy.get())
        z = float(entryz.get())
        média = ((x*y*z)**(1/3))
        média_label = Label(CalculadorDeMédiasRoot, fg='Red', text=f'O valor da média geométrica é {média}')
    
    botãoCalcular = Button(CalculadorDeMédiasRoot, text='Calcular média geométrica', command=MédiaGeométricaCalcular)
    botãoCalcular.pack()

def MédiaPonderada():
    textoX = Label(CalculadorDeMédiasRoot, text='Insira o valor 1')
    entryx = Entry(CalculadorDeMédiasRoot)
    textoX.pack()
    entryx.pack()
    textoY = Label(CalculadorDeMédiasRoot, text='Insira o valor 2')
    entryy = Entry(CalculadorDeMédiasRoot)
    textoY.pack()
    entryy.pack()
    textoZ = Label(CalculadorDeMédiasRoot, text='Insira o valor 3')
    entryz = Entry(CalculadorDeMédiasRoot)
    textoZ.pack()
    entryz.pack()
    def MédiaPonderadaCalcular():
        x = float(entryx.get())
        y = float(entryy.get())
        z = float(entryz.get())
        média = ((x+(2*y)+(3*z))/6)
        média_label = Label(CalculadorDeMédiasRoot, fg='Red', text=f'O valor da média ponderada é {média}')
        média_label.pack()
    
    botãoCalcular = Button(CalculadorDeMédiasRoot, text='Calcular média ponderada', command=MédiaPonderadaCalcular)
    botãoCalcular.pack()

def MédiaHarmônica():
    textoX = Label(CalculadorDeMédiasRoot, text='Insira o valor 1')
    entryx = Entry(CalculadorDeMédiasRoot)
    textoX.pack()
    entryx.pack()
    textoY = Label(CalculadorDeMédiasRoot, text='Insira o valor 2')
    entryy = Entry(CalculadorDeMédiasRoot)
    textoY.pack()
    entryy.pack()
    textoZ = Label(CalculadorDeMédiasRoot, text='Insira o valor 3')
    entryz = Entry(CalculadorDeMédiasRoot)
    textoZ.pack()
    entryz.pack()
    def MédiaHarmônicaCalcular():
        x = float(entryx.get())
        y = float(entryy.get())
        z = float(entryz.get())
        média = (1/((1/x)+(1/y)+(1/z)))
        média_label = Label(CalculadorDeMédiasRoot, fg='Red', text=(f'A média harmônica é {média}'))
        média_label.pack()
    
    botãoCalcular = Button(CalculadorDeMédiasRoot, text='Calcular média harmônica', command=MédiaHarmônicaCalcular)
    botãoCalcular.pack()

def MédiaAritmética():
    textoX = Label(CalculadorDeMédiasRoot, text='Insira o valor 1')
    entryx = Entry(CalculadorDeMédiasRoot)
    textoX.pack()
    entryx.pack()
    textoY = Label(CalculadorDeMédiasRoot, text='Insira o valor 2')
    entryy = Entry(CalculadorDeMédiasRoot)
    textoY.pack()
    entryy.pack()
    textoZ = Label(CalculadorDeMédiasRoot, text='Insira o valor 3')
    entryz = Entry(CalculadorDeMédiasRoot)
    textoZ.pack()
    entryz.pack()
    def Média(): 
        x = float(entryx.get())
        y = float(entryy.get())
        z = float(entryz.get())
        média = ((x+y+z)/3)
        média_label = Label(CalculadorDeMédiasRoot, fg='Red', text=(f'A média é Aritmética é {média}'))
        média_label.pack()

    botãoCalcular = Button(CalculadorDeMédiasRoot, text='Calcular média Aritmética', command=Média)
    botãoCalcular.pack()

Título = Label(CalculadorDeMédiasRoot, bg='Grey', text='CALCULADOR DE MÉDIAS por Pedro S Santos')
Espaço = Label(CalculadorDeMédiasRoot, text=' ')
BotãoMédiaGeo = Button(CalculadorDeMédiasRoot, text='Média Geométrica', bg='Grey', command=MédiaGeométrica)
BotãoMédiaPonderada = Button(CalculadorDeMédiasRoot, text='Média Ponderada', bg='Grey', command=MédiaPonderada)
BotãoMédiaHarmônica = Button(CalculadorDeMédiasRoot, text='Média Harmônica', bg='Grey', command=MédiaHarmônica)
BotãoMédiaAritmética = Button(CalculadorDeMédiasRoot, text='Média Aritmética', bg='Grey', command=MédiaAritmética)

Título.pack()
Espaço.pack()
BotãoMédiaGeo.pack()
BotãoMédiaPonderada.pack()
BotãoMédiaHarmônica.pack()
BotãoMédiaAritmética.pack()

CalculadorDeMédiasRoot.mainloop()
