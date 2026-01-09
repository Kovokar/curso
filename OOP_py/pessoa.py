#aula 36
from typing import Self, ClassVar
from random import randint
class Pessoa:
    ano_atual: ClassVar[int] = 2026

    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    def get_ano_nascimento(self) -> int:
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome: str, ano_nascimento: int) -> Self:
        idade: int = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gerar_id():
        return randint(0,10**6)


p1 = Pessoa.por_ano_nascimento("Felipe", 2006)
print(p1.gerar_id())