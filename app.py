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