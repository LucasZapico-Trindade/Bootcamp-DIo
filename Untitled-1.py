# Criando class chamada "MeuIterador", representa um iterador personalizado que pode ser usado em um laco For.
class MeuIterador:
# self = referencia ao proprio objeto
    def __init__ (self, numeros: list[int]):
# def init e o metodo construtor, chamado quando voce cria um objeto da classe.
        self.numeros = numeros
# aqui voce guarda a lista passada como parametro dentro do objeto.
        self.contador = 0
# esse atributo sera usado pra controlar a posicao atual da iteracao(qual indice da lista esta sendo acessado)

    def __iter__(self):
        return self
# metodo iter, ele diz ao python que o objeto e um iterador. por retornar "self", o proprio objeto sera usado para iterar.

    def __next__(self):
# esse metodo define o que acontece a cada repeticao do for, toda vez que for pedir o proximo valor, o python chama next.
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration
        


for i in MeuIterador(numeros = [10, 20, 30]):
    print(i)