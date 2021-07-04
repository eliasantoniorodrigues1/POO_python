class Pessoa:
    from datetime import date

    ano_atual = date.today().year

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo

    # Atributos da minha class
    def nome(self):
        return self.nome

    def idade(self):
        return self.idade

    # Comportamentos da classe
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def comer(self, comida):
        print(f'{self.nome} está comendo {comida}')
        self.comendo = True
        return self.comendo


class Escritor:
    # Manter os atributos privado para proteger (Encapsulamento)
    # Um atributo privado não pode ser acessado fora da classe, nesse caso teremos que criar um getter e um setter
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    # Definindo um setter para poder acessar a o objeto ferramenta e utilizá-lo externamente fazendo
    # Associação das classes.
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina está escrevendo...')


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append((produto))

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
