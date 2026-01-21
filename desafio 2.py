from datetime import datetime
# gerador que acessa historico e tipo
def gerar_relatorio(historico, tipo=None):
    for linha in historico.splitlines():
        # para cada linha em linhas do historico(splitlines transforma string em linhas)
        if tipo is None or tipo.lower() in linha.lower():
            # se o tipo da transacao for none, ou o tipo que eu escolher estiver na linha, ele vai mostrar essa linha.
            yield linha

    
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuario(usuarios):
    cpf = str(input("Digite o CPF(apenas numeros): "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("ja existe um usuario cadastrado com esse cpf.")
        return
    
    nome = input("Digite o nome do usuario: ").strip()
    data_nascimento = input("Digite o data de nascimento: ").strip()
    endereco = str(input("digite o endereco(logradouro, nro - bairro - cidade/UF):")).strip()

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("Cadastro realizado com sucesso.")

class iteradordecontas():
    def __init__(self, contas):
        self.contas = contas
        self.indice_atual = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice_atual < len(self.contas):
            conta = self.contas[self.indice_atual]
            self.indice_atual += 1

            return {
                "usuario": conta["usuario"] ,
                "agencia": conta["agencia"],
                "numero_conta": conta["numero_conta"]
            }
        raise StopIteration

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o CPF do usuário: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("Usuário não encontrado! Cadastro da conta cancelado.")
#definicao do decorador com parametro
def meu_decorador(tipo):
#funcao que recebe funcao original, recebe a funcao a ser decorada.
    def recebe_funcao(func):
#funcao wrapper, envolve a funcao original, substitui a funcao original e recebe os mesmos argumentos que ela.
        def wrapper(*args, **kwargs):
#executa a funcao original, e o retorno e guardado em resultado
            resultado = func(*args, **kwargs)
            saldo, historico, numero_saques, mensagem = resultado
#verificacao de sucesso da transacao
            if "sucesso" in mensagem.lower():
#gerando data e hora e convertendo para texto formatado.
                tempo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#anexacao ao historico, data e hora e o tipo de transacao.
                historico += f"[{tempo}] Transação: {tipo}\n"

            return saldo, historico, numero_saques, mensagem
        return wrapper
    return recebe_funcao

@meu_decorador("saque")
def saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, historico):

    if numero_saques >= LIMITE_SAQUES:
        return saldo, historico, numero_saques, "Limite diario de saques atingido."
    
    elif valor > saldo:
        return saldo, historico, numero_saques, "Seu saldo nao e suficiente para efetuar o saque!."
   
    elif valor <= 0:
        return saldo, historico, numero_saques, "Valor invalido para saque!."
    
    elif valor > limite:
        return saldo, historico, numero_saques,"O valor excede o limite permitido por saque!"

    saldo -= valor
    numero_saques += 1
    historico += f"Saque: R$ {valor:.2f}\n"
    return saldo, historico, numero_saques, "Saque realizado com sucesso!"

@meu_decorador("deposito")
def deposito(saldo, historico, valor, numero_saques):
    if valor <= 0:
        return saldo, historico, numero_saques, "Valor invalido para deposito!"

    saldo += valor
    historico += f"Deposito: R$ {valor:.2f}\n"
    return saldo, historico, numero_saques, "Deposito realizado com sucesso!"

def mostrar_extrato(saldo, limite, numero_saques, LIMITE_SAQUES, historico, tipo=None):
    print("\n======= EXTRATO =======")

    if not historico:
        print("Não foi realizada nenhuma movimentação.")
    else:
        for transacao in gerar_relatorio(historico, tipo):
            print(transacao)

    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print(f"Limite por saque: R$ {limite:.2f}")
    print(f"Número de saques realizados: {numero_saques}")
    print(f"Limite máximo de saques: {LIMITE_SAQUES}")
    print("========================\n")

print("=======SISTEMA BANCARIO========")
menu = """
[1] Criar usuario
[2] Criar conta corrente
[3] listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Sair
Digite aqui sua opcao:""" 


saldo = 0
limite = 500.0
historico = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
AGENCIA = "0001"
contas = []

while True:
    opcao = input(menu)

    if opcao == "5":
        valor = float(input("Informe o valor do saque: "))
        saldo, historico, numero_saques, mensagem = saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, historico)
        print(mensagem)

    elif opcao == "4":
        valor = float(input("Informe o valor do deposito: "))
        saldo, historico, numero_saques, mensagem = deposito(saldo, historico, valor, numero_saques)
        print(mensagem)

    elif opcao == "6":
        tipo = input("Filtrar por tipo (saque/deposito ou enter para todos): ").strip()

        if tipo == "":
            tipo = None

        mostrar_extrato(saldo, limite, numero_saques, LIMITE_SAQUES, historico, tipo)


    elif opcao == "1":
        criar_usuario(usuarios)

    elif opcao == "2":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    
    elif opcao == "3":
        if not contas:
            print("Nenhuma conta cadastrada.")
        else:
            iterador = iteradordecontas(contas)
            for info in iterador:
                    print(info)

    elif opcao == "7":
        break

print("Obrigado por utilizar nosso Sistema bancario!!")