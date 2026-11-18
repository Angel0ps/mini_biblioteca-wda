from src.mini_biblioteca.livros import Livro
from src.mini_biblioteca.usuarios import Usuario
from src.mini_biblioteca.emprestimos import Emprestimo, devolver


Angelo = Usuario("angelo","1")
print(Angelo)

Senhor_dos_Aneis = Livro("Senhor dos Anéis", "Tolkien", "10", True)
print(Senhor_dos_Aneis)

res = Emprestimo(Senhor_dos_Aneis, Angelo, True)
print(res)

res.devolver()
print(res)

