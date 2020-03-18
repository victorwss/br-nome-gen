# br_nome_gen
Gerador aleatório de nomes brasileiros.

## Exemplo de uso:

Uma forma simples de usar isso é assim:

```python
from br_nome_gen import pessoa_random

p = pessoa_random()
print(f"{'Homem' if p.masc else 'Mulher'}: {p.nome}")
```