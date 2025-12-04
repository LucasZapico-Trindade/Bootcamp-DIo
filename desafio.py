#Funcao para verificacao de usuario, para que o usuario so possa ter um cadastro por cpf.
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
#funcao de criar usuario, so sera criado o usuario, se o mesmo nao tiver o cpf ja cadastrado.
def criar_usuario(usuarios):
    cpf = int(input("Digite o CPF(apenas numeros): ")).strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("ja existe um usuario cadastrado com esse cpf.")
        return

    nome = input("Digite o nome do usuario: ").strip()
    data_nascimento = input("Digite o data de nascimento: ").strip
    endereco = str(input("digite o endereco(logradouro, nro - bairro - cidade/UF):")).strip

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("Cadastro realizado com sucesso.")
#funcao para criar conta, com verificacao de usuario, se o usuario nao tiver cadastro, ele nao pode ter uma conta!
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("Usuário não encontrado! Cadastro da conta cancelado.")

#funcao para o saque, onde a varias estruturas condicionais para o saque.
def saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, historico):
    # so faz o saque se o numero de saques nao tiver estourado o limite de 3
    if numero_saques >= LIMITE_SAQUES:
        return saldo, historico, numero_saques, "Limite diario de saques atingido."
    # o saque so e efetuado se nao ultrapassar o saldo da conta
    elif valor > saldo:
        return saldo, historico, numero_saques, "Seu saldo nao e suficiente para efetuar o saque!."
    #o saque so pode ser feito, se na costa tiver algum valor!
    elif valor <= 0:
        return saldo, historico, numero_saques, "Valor invalido para saque!."
    # e o saque so pode ser feito, se nao atingir o limite de valor do saque!
    elif valor > limite:
        return saldo, historico, numero_saques,"O valor excede o limite permitido por saque!"

    saldo -= valor
    numero_saques += 1
    historico += f"Saque: R$ {valor:.2f}\n"
    return saldo, historico, numero_saques, "Saque realizado com sucesso!"
# funcao para deposito
def deposito(saldo, historico, valor):
    if valor <= 0:
        return saldo, historico, "Nao e possivel depositar valores de 0 ou inferior!"

    saldo += valor
    historico += f"Deposito: R$ {valor:.2f}\n"
    return saldo, historico, "Deposito realizado com sucesso!!"

#funcao para o extrato
def mostrar_extrato(saldo, limite, numero_saques, LIMITE_SAQUES, historico):
    print("\n======= EXTRATO =======")

    if not historico:
        print("Não foi realizada nenhuma movimentação.")
    else:
        print(historico)

    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Limite por saque: R$ {limite:.2f}")
    print(f"Número de saques realizados: {numero_saques}")
    print(f"Limite máximo de saques: {LIMITE_SAQUES}")
    print("========================\n")
print("=======SISTEMA BANCARIO========")
menu = """
[1] Criar usuario
[2] Criar conta corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair
Digite aqui sua opcao:"""

#variaveis, contendo duas variaveis constantes.
saldo = 1000.0
limite = 500.0
historico = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
AGENCIA = "0001"
contas = []

#laco de repeticao infinito
while True:
    opcao = input(menu)

    if opcao == "4":
        valor = float(input("Informe o valor do saque: "))
        saldo, historico, numero_saques, mensagem = saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, historico)
        print(mensagem)

    elif opcao == "3":
        valor = float(input("Informe o valor do deposito: "))
        saldo, historico,  mensagem = deposito(saldo, historico, valor)
        print(mensagem)

    elif opcao == "5":
        mostrar_extrato(saldo, limite, numero_saques, LIMITE_SAQUES, historico)

    elif opcao == "1":
        criar_usuario(usuarios)

    elif opcao == "2":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == "6":
        break

print("Obrigado por utilizar nosso Sistema bancario!!")


    
    



    