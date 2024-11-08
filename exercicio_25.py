'''
Esse codigo serve para como exercicio para calcularmos bonus


Instruções:
O programa deve começar solicitando ao usuário que insira seu nome.
Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
Exemplo de Saída:
Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

Olá Luciano, o seu bônus foi de 8500
Salve esse script python como kpi.py
Faça uma documentação simples de como executar esse programa, utilize o README
Salve no Git e no Github
'''

def pipeline_calculo_de_bonus():
    nome, salario, bonus = solicitar_dados_usuario()
    if nome is not None:
        valor_bonus = calcular_bonus(salario, bonus)
        devolutiva(nome, valor_bonus)

def solicitar_dados_usuario():
    print("********** Bem-vindo à sua calculadora de bônus *************")
    print()
    nome = input("Insira o seu nome: ")
    try:
        salario = float(input('Insira seu salário: '))
        bonus = float(input('Insira o percentual em decimal do bônus: '))
        return nome, salario, bonus
    except:
        print('Digite apenas números e o separador decimal precisa ser um ponto (".")')
        solicitar_dados_usuario()
        return nome, salario, bonus

def calcular_bonus(salario, bonus):
    valor = 1000 + salario * bonus
    return valor

def devolutiva(nome, valor_bonus):
    print(f"Olá {nome}, o seu valor bônus foi de {valor_bonus}")

if __name__ == "__main__":
    pipeline_calculo_de_bonus()