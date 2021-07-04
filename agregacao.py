"""
Agregação: Uma classe usa outra classe como parte de si e uma depende da outra.
Exemplo: carro e roda (ambos existem um sem o outro, porém o carro não funciona de maneira adequada sem as rodas).

"""
from classe import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1500)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

print(carrinho.soma_total())
