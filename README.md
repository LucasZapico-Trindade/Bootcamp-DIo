# Bootcamp-DIo

📌 Sistema Bancário em Python

Este projeto implementa um Sistema Bancário simples, utilizando apenas recursos básicos de Python (sem orientação a objetos).
O sistema permite criar usuários, criar contas, realizar depósitos, saques e emitir extratos — tudo via terminal.

🚀 Funcionalidades

👤 1. Criar Usuário
Cadastro feito por CPF (somente números)
O sistema impede a criação de usuários duplicados
Armazena:
Nome completo
Data de nascimento
Endereço completo

🏦 2. Criar Conta Corrente

Uma conta só pode ser criada para um usuário já cadastrado
Cada conta possui:
Número da conta (sequencial)
Agência (padrão: 0001)
Referência ao usuário dono da conta

💰 3. Depósito

Permite depositar valores positivos
Registra a movimentação no histórico (extrato)

🏧 4. Saque

Regras aplicadas:
Máximo de 3 saques por dia
Valor máximo por saque: R$ 500,00
Não permite saque maior que o saldo
Não aceita valores negativos ou zero
Cada saque é registrado no extrato

📄 5. Extrato

Mostra:
Todas as movimentações (saques e depósitos)
Saldo atual
Limite de saque
Número de saques já realizados

🧠 Como o Sistema Funciona

O sistema roda em loop contínuo apresentando o menu:

[1] Criar usuário
[2] Criar conta corrente
[3] Depositar
[4] Sacar
[5] Extrato
[6] Sair


O usuário escolhe a operação e o programa executa a função correspondente.

📂 Estrutura do Código
🔍 Funções principais
✔ filtrar_usuario(cpf, usuarios)

Verifica se um usuário já está cadastrado através do CPF.

✔ criar_usuario(usuarios)

Cadastra um novo usuário caso o CPF ainda não exista.

✔ criar_conta(agencia, numero_conta, usuarios)

Cria uma conta bancária somente se o usuário existir.

✔ deposito(saldo, historico, valor)

Realiza depósitos válidos e adiciona ao extrato.

✔ saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, historico)

Executa saques seguindo todas as regras do sistema.

✔ mostrar_extrato(...)

Exibe as movimentações e saldos da conta.

💾 Variáveis do Sistema
Variável	Função
saldo	Saldo inicial da conta
limite	Limite máximo por saque
historico	Extrato de transações
numero_saques	Quantidade de saques feitos
LIMITE_SAQUES	Limite diário de saques
usuarios	Lista de usuários cadastrados
contas	Lista de contas criadas
AGENCIA	Agência padrão
▶️ Como Executar

Certifique-se de ter o Python instalado.
Salve o código em um arquivo, por exemplo:
sistema_bancario.py


Execute pelo terminal:

python sistema_bancario.py

🛠 Tecnologias Utilizadas

Python 3.x
Programação procedural
Entrada e saída via terminal (input / print)
Vscode
git

📌 Possíveis Melhorias Futuras

Migrar para Programação Orientada a Objetos (POO)
Persistência dos dados (salvar usuários e contas em arquivo)
Interface gráfica (Tkinter, PyQt ou Web)
Validação de CPF
Histórico separado por conta
Senhas e autenticação de usuário

📝 Autor

Lucas Trindade
