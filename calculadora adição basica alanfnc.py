def calculadora():
    print("Calculadora de Adicao")

    while True:
        num1 = input("Digite o primeiro numero (ou 'sair' para encerrar): ")
        if num1.lower() == 'sair':
            print("Encerrando a calculadora.")
            break

        num2 = input("Digite o segundo numero (ou 'sair' para encerrar): ")
        if num2.lower() == 'sair':
            print("Encerrando a calculadora.")
            break

        try:
            resultado = float(num1) + float(num2)
            print("Resultado:", resultado)
        except ValueError:
            print("Por favor, insira números válidos.")

calculadora()


