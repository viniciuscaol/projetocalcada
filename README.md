# Calculadora Simples em Python

Este projeto é uma calculadora simples em Python que realiza operações básicas de adição, subtração, multiplicação e divisão. As funções estão organizadas em arquivos separados para modularidade e reutilização.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `soma.py`: Contém a função de adição.
- `subtracao.py`: Contém a função de subtração.
- `multiplicacao.py`: Contém a função de multiplicação.
- `divisao.py`: Contém a função de divisão, incluindo tratamento para divisão por zero.
- `main.py`: Arquivo principal que interage com o usuário e utiliza as funções dos outros arquivos.

## Funcionalidades

- **Adição**: Soma dois números.
- **Subtração**: Subtrai um número do outro.
- **Multiplicação**: Multiplica dois números.
- **Divisão**: Divide um número por outro, com tratamento para divisão por zero.

## Arquivos do Projeto

### `soma.py`
```python
def soma(x, y):
    return x + y
```
### `subtracao.py`

```python
def subtracao(x, y):
    return x - y
```
### `multiplicacao.py`

```python
def multiplicacao(x, y):
    return x * y
```
### `divisao.py`

```python
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return f"Erro! O número {x} não pode ser dividido por 0."
```

### `app.py`

```python
import soma
import subtracao
import multiplicacao
import divisao

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    escolha = input("Digite sua escolha (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1} + {num2} = {soma.soma(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {num1} - {num2} = {subtracao.subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {num1} X {num2} = {multiplicacao.multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {num1} ÷ {num2} = {divisao.divisao(num1, num2)}")
        
        continuar = input("Deseja fazer outra operação? (s/n): ")
        if continuar.lower() != 's':
            break
    else:
        print("Entrada inválida.")
```
## Como Executar
1. Clone o repositório:
```bash
git clone https://github.com/viniciuscaol/projetocalcada.git
```
2. Entre na pasta do repositório recém clonado.
```bash
cd projetocalcada
```
3. Execute o arquivo app.py usando o Python:
```bash
python app.py
```
4. Siga as instruções na tela para realizar cálculos.