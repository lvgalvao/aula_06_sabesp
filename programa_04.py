tentativas = 5

while tentativas > 0:
    try:
        numero_1 = int(input("digite o numero que será dividido"))
        numero_2 = int(input("digite o numero que você quer dividir"))
        operacao = numero_1 / numero_2
        print(operacao)
        break
    except ZeroDivisionError as e:
        print(e)
    except:
        print("Erro")
    
    tentativas = tentativas - 1
    print(f"Algo deu errado e você tem esse número de tentativas: {tentativas}")