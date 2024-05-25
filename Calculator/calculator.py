from tkinter import Tk, Entry, Button, StringVar

# Configurações da calculadora
class Calculator:
    def __init__(self, master):
        # Janela principal {master}
        master.title("Calculator")
        master.geometry('357x430+0+0')  # Tamanho da interface
        master.config(bg='gray')
        master.resizable(False, False)

        # Armazena a expressão inserida
        self.equation = StringVar()
        self.entry_value = ''

        # Campo de entrada
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Configurações dos botões e suas coordenadas
        buttons = [
            ('C', 0, 50, 'lightyellow', self.clear),
            ('(', 90, 50, 'white', lambda: self.show('(')),
            (')', 180, 50, 'white', lambda: self.show(')')),
            ('x', 270, 50, 'white', lambda: self.show('*')),
            ('7', 0, 125, 'white', lambda: self.show(7)),
            ('8', 90, 125, 'white', lambda: self.show(8)),
            ('9', 180, 125, 'white', lambda: self.show(9)),
            ('÷', 270, 125, 'white', lambda: self.show('/')),
            ('4', 0, 200, 'white', lambda: self.show(4)),
            ('5', 90, 200, 'white', lambda: self.show(5)),
            ('6', 180, 200, 'white', lambda: self.show(6)),
            ('-', 270, 200, 'white', lambda: self.show('-')),
            ('1', 0, 275, 'white', lambda: self.show(1)),
            ('2', 90, 275, 'white', lambda: self.show(2)),
            ('3', 180, 275, 'white', lambda: self.show(3)),
            ('+', 270, 275, 'white', lambda: self.show('+')),
            ('%', 0, 350, 'white', lambda: self.show('%')),
            ('0', 90, 350, 'white', lambda: self.show(0)),
            ('.', 180, 350, 'white', lambda: self.show('.')),
            ('⌫', 270, 350, 'white', self.backspace),
            ('=', 270, 395, 'lightblue', self.solve),
        ]

        for (text, x, y, color, command) in buttons:
            Button(width=10, height=4 if text != '=' else 2, text=text, relief='flat', bg=color, command=command).place(x=x, y=y)

    # Atualiza os valores com a nova entrada
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    # Método backspace (apagar)
    def backspace(self):
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    # Método clear
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    # Atualiza o campo com o resultado
    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

# Inicia a aplicação tkinter
root = Tk()
calculator = Calculator(root)
root.mainloop()
