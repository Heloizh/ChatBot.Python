from tkinter import Tk, Entry, Button, StringVar 


#configuraçãoes da calculadora
class Calculator:
    def __init__(self, master):
        #janela principal {master}
        master.title ("Calculator") 
        master.geometry('357x430+0+0') #tamanho da interface
        master.config(bg='gray')
        master.resizable(False, False)

        #armazena a expressão inserida
        self.equation=StringVar()
        self.entry_value=''

        #campo de entrada
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        #configurações dos botões e suas coordenadas
        Button(width=10,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=90 ,y=50)
        Button(width=10,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=180 ,y=50)
        Button(width=10,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=0 ,y=350) 
        Button(width=10,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0 ,y=125)
        Button(width=10,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90 ,y=125)
        Button(width=10,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180 ,y=125)
        Button(width=10,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0 ,y=200)
        Button(width=10,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=10,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180 ,y=200)
        Button(width=10,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0 ,y=275)
        Button(width=10,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=180 ,y=275)
        Button(width=10,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90 ,y=275)
        Button(width=10,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90 ,y=350)
        Button(width=10,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180 ,y=350)
        Button(width=10,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270 ,y=275)
        Button(width=10,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270 ,y=200)
        Button(width=10,height=4,text='÷',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270 ,y=125)
        Button(width=10,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=270 ,y=50)
        Button(width=10,height=2,text='⌫',relief='flat',bg='white',command=self.backspace).place(x=270 ,y=350)
        Button(width=10,height=1,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270 ,y=395)
        Button(width=10,height=4,text='C',relief='flat',bg='lightyellow',command=self.clear).place(x=0 ,y=50)
     

    #atualiza os valores com a nova entrada
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    #método backspace (apagar)
    def backspace(self):
        self.entry_value = self.entry_value[:-1]    
        self.equation.set(self.entry_value)

    #método clear
    def clear(self):
        self.entry_value =''
        self.equation.set(self.entry_value)

    #atualiza o campo com o resultado
    def solve(self):
      try: 
        result=eval(self.entry_value)    
        self.equation.set(result)
      except Exception as e:
        self.equation.set("Error")  



#inicia a aplicação tkinter
root = Tk()
calculator = Calculator(root)
root.mainloop()
