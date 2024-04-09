menu = """
[u] Cadastrar Usuário
[c] Criar Conta Bancária
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = {}  # Dicionário para armazenar informações dos usuários
contas_bancarias = {}  # Dicionário para armazenar informações das contas bancárias

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def cadastrar_usuario(nome, cpf, email):
    """
    Cadastra um novo usuário no sistema.

    Args:
    - nome (str): Nome do usuário.
    - cpf (str): CPF do usuário.
    - email (str): E-mail do usuário.
    """
    usuarios[cpf] = {'nome': nome, 'email': email}
    print(f"Usuário {nome} cadastrado com sucesso.")

def criar_conta_bancaria(cpf, saldo_inicial=0, limite=500):
    """
    Cria uma nova conta bancária para um usuário.

    Args:
    - cpf (str): CPF do usuário.
    - saldo_inicial (float, optional): Saldo inicial da conta. Padrão é 0.
    - limite (float, optional): Limite da conta. Padrão é 500.
    """
    if cpf in usuarios:
        contas_bancarias[cpf] = {'saldo': saldo_inicial, 'limite': limite}
        print("Conta bancária criada com sucesso.")
    else:
        print("CPF não cadastrado. Por favor, cadastre o usuário primeiro.")

def depositar(valor):
    global saldo, extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"

def sacar(valor):
    global saldo, extrato, numero_saques
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1

while True:
    opcao = input(menu)

    if opcao == "u":
        nome = input("Nome do usuário: ")
        cpf = input("CPF do usuário: ")
        email = input("E-mail do usuário: ")
        cadastrar_usuario(nome, cpf, email)

    elif opcao == "c":
        cpf = input("CPF do usuário para criar conta bancária: ")
        saldo_inicial = float(input("Saldo inicial da conta: "))
        limite_conta = float(input("Limite da conta: "))
        criar_conta_bancaria(cpf, saldo_inicial, limite_conta)

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            depositar(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > 0:
            if valor <= saldo:
                if valor <= limite:
                    if numero_saques < LIMITE_SAQUES:
                        sacar(valor)
                    else:
                        print("Operação falhou! Número máximo de saques excedido.")
                else:
                    print("Operação falhou! O valor do saque excede o limite.")
            else:
                print("Operação falhou! Você não tem saldo suficiente.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

