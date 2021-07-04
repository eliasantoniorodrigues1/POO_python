"""
Uma classe vai se relacionar com a outra, mas elas continuam sendo independentes.
Exemplo: Um escritor e uma caneta e uma máquina de escrever
Relacionar essas três classes.

"""
from classe import Escritor
from classe import Caneta
from classe import MaquinaDeEscrever
escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(escritor.nome)
print(caneta.marca)
maquina.escrever()
# Criando uma associacao
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

