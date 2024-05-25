```markdown
# Calculadora Simples em Python

Este repositório contém o código-fonte de uma calculadora simples desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. A calculadora permite realizar operações básicas como adição, subtração, multiplicação e divisão.

## Funcionalidades

- **Adição**: Permite somar dois números.
- **Subtração**: Permite subtrair um número de outro.
- **Multiplicação**: Permite multiplicar dois números.
- **Divisão**: Permite dividir um número por outro.

## Requisitos

- Python 3.x
- Tkinter (geralmente incluída na instalação padrão do Python)

## Como Executar

1. **Clone o repositório**:
    ```bash
    git clone 
    cd calculator
    ```

2. **Execute o script**:
    ```bash
    python calculator.py
    ```

## Estrutura do Projeto

```
.
├── README.md
├── calculator.py
└── screenshot.png
```

- **calculator.py**: Contém o código-fonte da calculadora.
- **calculadoraImage.png**: Uma imagem mostrando a interface da calculadora.

## Código de Exemplo

Aqui está um trecho do código principal da calculadora (`calculator.py`):

```python
import tkinter as tk

class Calculadora:
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

   ...
```

## Captura de Tela

Captura de Tela da Calculadora => .[Calculadora Imagem](calculadoraImage.png).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um Pull Request ou relatar problemas na seção de Issues.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE/Python).

## Contato

Para dúvidas ou sugestões, entre em contato com [eloisamartins.trabalho@gmail.com](eloisamartins.trabalho@gmail.com).

---

Aproveite e experimente a calculadora! Se você tiver alguma ideia para melhorias, não hesite em contribuir.
```

