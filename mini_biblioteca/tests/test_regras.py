from src.mini_biblioteca.livros import Livro
from src.mini_biblioteca.usuarios import Usuario
from src.mini_biblioteca.emprestimos import Emprestimo

import pytest

usr = Usuario("angelo","1")

li = Livro("Senhor dos Anéis", "Tolkien", "10", True)
li.disponivel = False

obj = Emprestimo(li, usr, True)

def test_regra():
    li.disponivel = False
    with pytest.raises(ValueError):

        print(li.disponivel)
        Emprestimo(li, usr)

