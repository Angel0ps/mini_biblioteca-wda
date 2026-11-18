from src.mini_biblioteca.livros import Livro
from src.mini_biblioteca.usuarios import Usuario

class Emprestimo(Livro, Usuario):
    
    def __init__(self, livro: Livro, usuario: Usuario, ativo = True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo

        @property
        def livro(self):
            return self._livro

        @livro.setter
        def livro(self, mlivro:Livro):
            if not mlivro.disponivel:
                raise ValueError
            
            mlivro.disponivel = False
            self._livro = mlivro

        def devolver(self):
            self.ativo = False
            livro.disponivel = True
                
        
