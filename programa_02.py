while True:
    try:
        nome = input("digite o seu nome :")
        idade = int(input("digite a sua idade: "))
        if not nome.isalpha():
            raise ValueError("Você não digitou um nome valido")
        
        if isinstance(idade, int):
            print("voce digitou uma idade valida")
        else:
            print("voce digitou uma idade invalida")
        nome_maiusculo = nome.upper()
        proxima_idade = idade + 1
        print(nome_maiusculo)
        print(proxima_idade)
        break
    except ValueError as e:
        print(e)