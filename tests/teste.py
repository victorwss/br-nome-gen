import sys
from br_nome_gen import pessoa_random, Pessoa

qtd: int = 1 if len(sys.argv) < 2 else int(sys.argv[1])
for i in range(0, qtd):
    p: Pessoa = pessoa_random()
    print(f"{'Homem' if p.masc else 'Mulher'}: {p.nome}")