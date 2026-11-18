from src.mini_biblioteca.livros import Livro
from src.mini_biblioteca.usuarios import Usuario
from src.mini_biblioteca.emprestimos import Emprestimo

usr = Usuario("angelo","1")

li = Livro("Senhor dos Anéis", "Tolkien", "10", True)

obj = Emprestimo(li, usr, True)

def test_isntancia_Emprestimo():
    if not isinstance(obj.livro, Livro):
        raise TypeError

    if not isinstance(obj.usuario, Usuario):
        raise TypeError

