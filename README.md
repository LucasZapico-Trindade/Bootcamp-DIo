💰 Sistema Bancário em Python

Projeto desenvolvido como parte de desafio educacional, com o objetivo de aplicar na prática conceitos fundamentais e intermediários da linguagem Python, simulando um sistema bancário simples via terminal.

📌 Descrição do Desafio

Criar um sistema bancário capaz de realizar operações básicas como depósito, saque e extrato, aplicando regras de negócio e utilizando recursos avançados da linguagem Python, como decoradores, geradores e iteradores personalizados.

🎯 Objetivos de Aprendizado

Aplicar lógica de programação em Python
Trabalhar com funções e controle de fluxo
Utilizar decoradores para registrar transações
Implementar geradores para relatórios de extrato
Criar iteradores personalizados
Manipular estruturas de dados (listas e dicionários)
Simular regras de negócio de um sistema bancário

⚙️ Funcionalidades Implementadas

✅ Criar usuário
✅ Criar conta corrente vinculada a um usuário
✅ Listar contas cadastradas
✅ Realizar depósitos
✅ Realizar saques com limite diário
✅ Visualizar extrato bancário
✅ Filtrar extrato por tipo de transação (saque ou depósito)

📜 Regras de Negócio
💸 Saque

Limite de 3 saques diários
Valor máximo de R$ 500,00 por saque
Não permite saque maior que o saldo disponível
Não permite valores negativos ou iguais a zero

💰 Depósito

Valor deve ser maior que zero
Não há limite diário de depósitos

🧠 Conceitos Utilizados
🔁 Geradores

Utilizados para gerar o relatório do extrato de forma eficiente, permitindo filtrar transações por tipo.

def gerar_relatorio(historico, tipo=None):

🎯 Decoradores

Responsáveis por registrar automaticamente a data, hora e tipo da transação no histórico quando a operação é concluída com sucesso.

@meu_decorador("saque")
@meu_decorador("deposito")

🔄 Iteradores Personalizados

Implementados para percorrer e listar as contas bancárias cadastradas.

class iteradordecontas:

📋 Menu do Sistema
[1] Criar usuário
[2] Criar conta corrente
[3] Listar contas
[4] Depositar
[5] Sacar
[6] Extrato
[7] Sair

▶️ Como Executar o Projeto

Pré-requisitos

Python 3.10 ou superior

Execução

No terminal, execute:

python nome_do_arquivo.py

📂 Estrutura de Dados

Usuários: lista de dicionários
Contas: lista de contas vinculadas a usuários
Histórico: string contendo o registro das transações

📚 Tecnologias Utilizadas

Python 3
VS Code
Git e GitHub

👨‍💻 Autor

Lucas Oliveira Zapico Trindade
Estudante de Análise e Desenvolvimento de Sistemas

Projeto desenvolvido para fins educacionais na plataforma Digital Innovation One (DIO).
