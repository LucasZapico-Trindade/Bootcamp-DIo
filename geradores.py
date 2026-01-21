# O que sao geradores?
# Sao tipos especiais de iteradores, ao contrario das listas ou outros iteraveis, nao armazenam todos os seus valores na memoria, sao definidos usando funcoes regulares, mas ao inves de retornar valores usando "return", utiizam "yield".

#Caracteristicas de geradores.
# uma vez que um item gerado e consumido, ele é esquecido e nao pode ser acessado novamente.
# O estado interno de um gerador é mantido entre as chamadas.
# A execucao de um gerador é pausada na declaracao "yield", e retomada dai na proxima vez que ele for chamado.

#quando usar iterador e gerador?= gerador = codigos simples, iterador = algo mais complexo.

def meu_gerador(numeros = list[int]):
    for numero in numeros:
        yield numero * 2
    

for i in meu_gerador(numeros = [1, 2, 3]):
    print(i)