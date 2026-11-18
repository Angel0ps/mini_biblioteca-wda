from mini_biblioteca.src.mini_biblioteca.livros import Livro
from mini_biblioteca.src.mini_biblioteca.usuarios import Usuario

class Emprestimo(Livro, Usuario):
    
    def __init__(self, livro: Livro, usuario: Usuario, ativo = True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo

        @property
        def livro(self):
            return self.livro

        @livro.setter
        def livro(self):
            if isinstance(livro, Livro):
                if livro.disponivel == False:
                    raise ValueError
                else:
                    livro.disponivel = False
                    return self.livro
            else:
                raise TypeError

        def devolver(self):
            self.ativo = False
            livro.disponivel = True
                
        
