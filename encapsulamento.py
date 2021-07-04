"""
public: Podem ser acessados dentro e fora da classe
protected: Apenas dentro da classe ou dentro das filhas
private: Só fica disponível dentro da classe

# Convensão do Python: Se um atributo possui um underline antes do nome, não é recomendado acessar ele.
_ é igual a protected/private: Mesmo utilizando dessa forma ainda é possível acessar e fazer alterações na variável. (public _)
__ é extramamente recomendado que não seja acessado essa variável (_NOMECLASSE__nomeatributo).

Serve para proteger a sua aplicação.
Exemplo:
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}  # recomenda-se utilizar dois underlines para que a variável não seja acessada.

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Elias')
bd.inserir_cliente(2, 'Otavio')
bd.inserir_cliente(3, 'Rose')

bd.__dados = 'Uma outra coisa'  # Quando você acessa a variavel dessa forma o Python cria outra e não altera a da classe.
# Para ver o atributo alterado:
print(bd.__dados)
print(bd._BaseDeDados__dados)

