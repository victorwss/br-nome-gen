import random
from dataclasses import dataclass
from typing import Any, Callable, cast, List, Sequence, TypeVar, Union

T = TypeVar('T')
c_str = Callable[[], str]
S = Union[str, c_str]

def is_function(x: Any) -> bool:
    return hasattr(x, '__call__')

def random_element(*itens: T) -> T:
    return random.sample(itens, 1)[0]

def resolve_s(i: S) -> str:
    if is_function(i):
        f: c_str = cast(c_str, i)
        return f()
    if isinstance(i, str):
        return i
    raise Exception(i)

def up(item: S) -> c_str:
    def inner() -> str:
        x: str = resolve_s(item)
        return x[0].upper() + x[1:]
    return inner

def choice_s(*itens: S) -> c_str:
    def inner() -> str:
        while True:
            x: str = resolve_s(random_element(*itens))
            if x != '': return x
    return inner

def choice_s_epsilon(*itens: S) -> c_str:
    def inner() -> str:
        return resolve_s(random_element(*itens))
    return inner

def seq_s(*itens: S) -> c_str:
    def inner() -> str:
        out: str = ""
        for item in itens:
            s: str = resolve_s(item)
            out += s
        return out
    return inner

nome_masculino: c_str = choice_s(
    "Abílio", "Ademar", "Adílson", "Adônis", "Adriano", "Aécio", "Alan", "Albano", "Alberto", "Albino", "Aldo", "Alessandre", "Alex", "Alexandre", "Alfredo", "Ali", "Alisson", "Aloísio", "Altair", "Altino", "Álvaro", "Amarildo", "Anakin", "Anderson", "André", "Ângelo", "Antônio", "Armando", "Arnaldo", "Artur", "Arthur", "Augusto", "Aurélio", "Áureo", "Avelino", "Ayrton",
    "Baltazar", "Barnabé", "Bartolomeu", "Batista", "Benedito", "Benjamin", "Bento", "Bernardo", "Beto", "Bóris", "Breno", "Bruno",
    "Caio", "Camilo", "Carlos", "Cauê", "Celso", "César", "Charles", "Chico", "Cícero", "Cirilo", "Ciro", "Cléber", "Cleberson", "Cristiano",
    "Damião", "Daniel", "Danilo", "Dante", "Dário", "Davi", "David", "Décio", "Demilson", "Denis", "Diego", "Diogo", "Dionísio", "Domingos",
    "Ederson", "Edinaldo", "Edivaldo", "Edson", "Edu", "Eduardo", "Elano", "Elias", "Eliel", "Elói", "Emanoel", "Emílio", "Eric", "Estevão", "Eugênio", "Eustáquio", "Everaldo", "Everton", "Ezequiel",
    "Fabiano", "Fábio", "Fabrício", "Fagner", "Felipe", "Félix", "Filipe", "Fernando", "Flávio", "Francisco", "Fred", "Frederico",
    "Gabriel", "Geraldo", "Gilberto", "Giovanni", "Giuseppe", "Gilmar", "Gilson", "Guilherme", "Gustavo",
    "Hamilton", "Heitor", "Helder", "Hélio", "Henrique", "Hércules", "Heron", "Hildebrando", "Hilton", "Hugo", "Humberto",
    "Iago", "Igor", "Inácio", "Isaías", "Isac", "Ismael", "Israel", "Itamar", "Ivan",
    "Jacinto", "Jack", "Jackson", "Jair", "Jairo", "Jânio", "Jason", "Jardel", "Jaziel", "Jean", "Jeferson", "Jesus", "João", "João", "João", "João", "Joaquim", "Joel", "Jonas", "Jonathan", "Jonathas", "Jorge", "José", "José", "José", "Josiel", "Juan", "Júlio", "Juliano", "Junior",
    "Karl", "Kauê", "Kevin", "Kim",
    "Laércio", "Laerte", "Leandro", "Leo", "Leonardo", "Leopoldo", "Lino", "Luan", "Lucas", "Lúcio", "Luciano", "Luigi", "Luís", "Luiz", "Luke",
    "Manoel", "Manuel", "Marcelo", "Marciano", "Márcio", "Marco", "Marcos", "Mariano", "Mário", "Marlon", "Martin", "Martinho", "Mateus", "Matheus", "Maurício", "Max", "Micael", "Michel", "Miguel", "Mike", "Milton", "Moacyr", "Moisés", "Murilo",
    "Nathan", "Nelson", "Ney", "Nicolas", "Nicolau", "Nilo", "Nilton", "Nivaldo",
    "Olavo", "Oliver", "Omar", "Orlando", "Oséas", "Osório", "Osvaldo", "Otaviano", "Otávio", "Otto",
    "Pablo", "Patrick", "Paulo", "Paulo", "Pedro", "Plínio",
    "Quico", "Quirino",
    "Rafael", "Raí", "Ramon", "Raul", "Reginaldo", "Reinaldo", "Renato", "Ricardo", "Ricardo", "Rivaldo", "Robert", "Roberto", "Roberval", "Robson", "Rodrigo", "Rodrigo", "Rodolfo", "Roger", "Rogério", "Romildo", "Ronaldo",
    "Samuel", "Sandro", "Saulo", "Sebastião", "Sérgio", "Severino", "Silvair", "Sílvio", "Simão",
    "Táles", "Tiago", "Thiago", "Tomáz", "Toninho", "Túlio",
    "Uribe",
    "Valter", "Victor", "Vinícius", "Vitor",
    "Wagner", "Wally", "Walter", "Washington", "Wellington", "Wesley", "Willian", "Wilson",
    "Xavier", "Xerxes",
    "Yuri",
    "Zeca"
)

nome_feminino: c_str = choice_s(
    "Abigail", "Adriana", "Adrielle", "Alana", "Albina", "Alessandra", "Aline", "Amália", "Amanda", "Amélia", "Ana", "Ana", "Ana", "Ana", "Ana", "Anna", "Anne", "Andréia", "Andressa", "Ângela", "Angélica", "Aparecida", "Ariana", "Ariel", "Arilda", "Arlete",
    "Bárbara", "Beatriz", "Bella", "Berenice", "Bernadete", "Bete", "Bianca", "Brenda", "Bruna",
    "Camila", "Carla", "Cármen", "Carolina", "Caroline", "Cássia", "Catarina", "Cecília", "Celeste", "Célia", "Celina", "Charlene", "Christie", "Cibele", "Cícera", "Cíntia", "Clara", "Clarice", "Cláudia", "Cleuza", "Clotilde", "Cristiane", "Cristina",
    "Damares", "Daiane", "Daniela", "Danielle", "Dara", "Denise", "Diana", "Dilma", "Dina",
    "Ediane", "Edilene", "Eduarda", "Elaine", "Eleonora", "Eleriane", "Eliane", "Elisa", "Elizabete", "Elisete", "Eliomar", "Elisângela", "Eloá", "Érica", "Eulália", "Eunice", "Eva", "Evelyn",
    "Fabiana", "Fabíola", "Fátima", "Fernanda", "Felícia", "Flávia", "Flaviana", "Francielle",
    "Gabriela", "Gabrielle", "Genir", "Gigi", "Gilmara", "Gisele", "Gislaine", "Graziele", "Guiomar",
    "Helena", "Hellen", "Heloísa", "Hilda",
    "Isabel", "Isabela", "Ingrid", "Isaiane", "Ísis", "Itamara", "Ivanete", "Ivete", "Ivone",
    "Janaína", "Jandira", "Janete", "Jaqueline", "Jeniffer", "Jenny", "Jéssica", "Joelma", "Josiane", "Josilda", "Joyce", "Júlia", "Juliana", "Jussara",
    "Karin", "Karina", "Kátia", "Kelly", "Keyla", "Kiara",
    "Laila", "Laís", "Lana", "Lara", "Larissa", "Laura", "Léia", "Leila", "Leonara", "Lena", "Leni", "Liane", "Lidiane", "Lígia", "Lili", "Lilian", "Lina", "Lisa", "Lívia", "Luara", "Lúcia", "Luciana", "Luiza", "Luzia", "Luzimara", "Luzinete",
    "Madalena", "Magali", "Maíra", "Maísa", "Manuela", "Mara", "Marcela", "Márcia", "Marciane", "Marcielle", "Margarete", "Margarida", "Maria", "Maria", "Maria", "Maria", "Maria", "Maria", "Mariana", "Marielle", "Marilúcia", "Marina", "Marlene", "Marli", "Marta", "Matilde", "Mayara", "Mayra", "Meire", "Mel", "Melanie", "Melissa", "Michele", "Mikaella", "Milene", "Mirela", "Mirian", "Mônica", "Monique",
    "Nádia", "Nair", "Natália", "Nayara", "Neila", "Nicole", "Núbia",
    "Olga", "Olímpia", "Olívia", "Otávia",
    "Patrícia", "Patrícia", "Paula", "Paula", "Paula", "Paulínia", "Priscila", "Poliana",
    "Quênia", "Quésia", "Quitéria",
    "Rafaela", "Raiane", "Raíssa", "Raquel", "Rebeca", "Regina", "Renata", "Rita", "Roberta", "Rosa", "Rosana", "Rosângela", "Rose", "Roseli", "Rosilda", "Rosimeire", "Rute",
    "Sabrina", "Samanta", "Samara", "Sâmia", "Samila", "Sandra", "Sara", "Selena", "Selma", "Sheila", "Shirley", "Simone", "Sílvia", "Solange", "Sônia", "Soraya", "Suellen", "Suely", "Susan", "Suzana", "Suzanne", "Suzy",
    "Tábata", "Tânia", "Taís", "Tainá", "Tainara", "Talita", "Tatiana", "Tatiane", "Telma", "Teresa", "Terezinha", "Thaís", "Thaíssa", "Tina",
    "Úrsula",
    "Valdirene", "Valéria", "Valeska", "Valquíria", "Vanda", "Vanessa", "Vânia", "Velma", "Vera", "Verônica", "Vitória", "Violeta", "Vívian", "Viviane",
    "Walderice", "Wanda", "Wendy", "Wilma",
    "Xilena",
    "Yasmin", "Yeda", "Yolanda",
    "Zara", "Zenaide", "Zilda", "Zuleide", "Zulmira"
)

sobrenome_comum: c_str = choice_s(
    "de Barbosa", "Gomes", "de Oliveira", "de Pereira", "dos Santos", "dos Santos", "de Souza", "de Souza", "da Silva", "da Silva", "da Silva", "da Silva"
)

sobrenome_incomum: c_str = choice_s(
    "de Abreu", "de Aguiar", "de Albuquerque", "de Alcântara", "de Alencar", "de Almeida", "de Alvarenga", "de Álvares", "de Alves", "de Alvim", "do Amaral", "do Amazonas", "de Amorim", "de Andrade", "de Angola", "de Antunes", "de Arantes", "de Araújo", "de Arruda", "de Assis", "de Assunção", "de Ayres", "de Azevedo",
    "Bahia", "Banhos", "de Barboza", "de Barros", "Barroso", "de Bezerra", "de Braga", "de Bragança", "de Brandão", "Brasil", "de Brito", "de Britto", "Borba", "de Borges", "Branco", "Buarque", "de Bueno",
    "de Cabral", "de Camargo", "Câmara", "de Campos", "de Cardoso", "de Cardozo", "de Carvalho", "Castelo", "Castelo Branco", "de Castro", "Cavalcante", "de Cerqueira", "de Chaves", "da Conceição", "da Costa", "Coutinho", "Couto", "da Cruz", "da Cunha",
    "d'Ávila", "Dias", "de Diniz", "de Drummond", "de Duarte", "Duque", "Dutra",
    "da Encarnação", "Espada", "de Espanha", "do Espírito Santo", "Estrada",
    "de Farias", "de Ferreira", "de Fernandes", "de Ferraz", "de Figueira", "de Figueiredo", "de Fonseca", "Fontes", "Fortes", "de Fraga", "Fragoso", "de França", "Franco", "Freire", "de Freitas", "Frias",
    "da Gama", "de Garcia", "de Gimenes", "de Godoy", "Góis", "de Gonçalves", "da Graça", "Guedes", "Guerra", "de Guimarães", "de Gusmão", "de Gusmões", "Gutierrez",
    "Herrera", "de Holanda",
    "de Iglesias", "Igreja",
    "Jangada", "Jardim", "de Jesus", "de Junqueira",
    "Klein",
    "de Lacerda", "de Leão", "de Leite", "de Lemes", "de Lemos", "de Lima", "de Linhares", "de Lins", "da Lira", "de Lisboa", "Lopes", "da Luz",
    "de Macedo", "de Machado", "Maciel", "de Madureira", "de Magalhães", "de Maia", "de Malta", "do Maranhão", "Marinho", "Marques", "de Martins", "Martinez", "da Mata", "de Matos", "de Medeiros", "de Meireles", "de Melo", "de Mello", "Mendes", "de Mendonça", "de Menezes", "Mercado", "Milani", "Mineiro", "de Miranda", "de Monteiro", "de Morais", "de Moreira", "Moreno", "de Moura", "Mourão", "de Munhoz", "de Muniz",
    "do Nascimento", "Naves", "Negrão", "das Neves", "da Nóbrega", "de Nogueira", "de Noronha", "de Novais", "Nunes",
    "de Oliva", "de Ortega", "de Ortiz", "de Osório",
    "de Pacheco", "de Padilha", "Paim", "da Paixão", "de Paiva", "de Palhares", "da Paraíba", "do Paraná", "de Paranhos", "de Parreira", "de Pascoal", "de Paula", "da Paz", "de Peixoto", "Penedo", "de Peres", "Pimenta", "de Pimentel", "Pinhão", "dos Pinhais", "de Pinheiro", "do Piauí", "Pinto", "Pires", "Portugal", "do Prado", "Prates", "Preto",
    "de Queiroz",
    "de Ramos", "Rangel", "dos Reis", "de Rezende", "Ribeiro", "do Rio", "da Rocha", "Rodrigues", "Rosa", "Rosatto", "Rossi",
    "de Sá", "de Sales", "de Salgado", "de Salvador", "de Sampaio", "Sanches", "de Santana", "de Santo Antônio", "de São Pedro", "Schmidt", "Schneider", "Seixas", "da Serra", "de Silveira", "de Simões", "de Siqueira", "de Soares", "de Sobral", "Souto",
    "de Tavares", "de Teixeira", "Teles", "de Torquato", "Trevisan", "de Trindade", "Tristão", "de Toledo", "Torres", "de Tozetto",
    "de Uchôa",
    "do Vale", "Valente", "Valverde", "de Vargas", "de Vasconcelos", "Vaz", "de Viana", "de Vieira",
    "Weber", "Weiss", "Werner",
    "Ximenes",
    #Y
    #Z
)

def remove_de(nome: str) -> str:
    i: int = nome.find(" ")
    return nome if i == -1 or nome[0:i] in ["de", "da", "do", "das", "dos"] else nome[i + 1:]

def sobrenome_normal() -> str:
    nome: str = choice_s(sobrenome_comum, sobrenome_incomum, sobrenome_incomum, sobrenome_incomum)()
    return choice_s(nome, remove_de(nome))()

def sobrenome_random_japones() -> str:
    silaba_japones: c_str = choice_s(
        "a", "i", "u", "e", "o",
        "ka", "ki", "ku", "ke", "ko",
        "sa", "shi", "su", "se", "so",
        "ta", "chi", "tsu", "te", "to",
        "na", "ni", "nu", "ne", "no",
        "ha", "hi", "fu", "he", "ho",
        "ma", "mi", "mu", "me", "mo",
        "ya", "yu", "yo",
        "ra", "ri", "ru", "re", "ro",
        "wa", "wo",
        "n",
        "ga", "gi", "gu", "ge", "go",
        "za", "ji", "zu", "ze", "zo",
        "da", "de", "do",
        "ba", "bi", "bu", "be", "bo",
        "pa", "pi", "pu", "pe", "po"
    )
    x: str = "a"
    while len(x) < 2:
        x = up(choice_s(seq_s(silaba_japones, silaba_japones), seq_s(silaba_japones, silaba_japones, silaba_japones), seq_s(silaba_japones, silaba_japones, silaba_japones, silaba_japones)))()
    return x

def contem_texto(palheiro: str, *agulhas: str) -> bool:
    for agulha in agulhas:
        if agulha in palheiro:
            return True
    return False

def sobrenome_random() -> str:
    vogal: c_str = choice_s("a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "y")
    consoante_comum: c_str = choice_s("b", "c", "d", "f", "g", "l", "m", "n", "p", "r", "s", "t", "v")
    consoante_incomum_inicio: c_str = choice_s("br", "ch", "cl", "cr", "dr", "fr", "gr", "h", "j", "k", "pr", "pl", "sh", "tr", "w", "z")
    consoante_incomum_meio  : c_str = choice_s("br", "ch", "cl", "cr", "dr", "fr", "gr", "h", "j", "k", "pr", "pl", "sh", "tr", "w", "z", "rr", "ss")
    consoante_rara_inicio: c_str = choice_s("bl", "dl", "fl", "gl", "gr", "kr", "kl", "tl", "th", "vr", "vl", "qu", "x", "ph")
    consoante_rara_meio  : c_str = choice_s("bl", "dl", "fl", "gl", "gr", "kr", "kl", "tl", "th", "vr", "vl", "qu", "x", "ph", "sc", "sk", "sz", "ck", "ç", "tt", "pp", "bb", "zz", "mm", "nn")
    consoante_inicio: c_str = choice_s(consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_incomum_inicio, consoante_incomum_inicio, consoante_rara_inicio)
    consoante_meio  : c_str = choice_s(consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_comum, consoante_incomum_meio  , consoante_incomum_meio  , consoante_rara_meio  )
    consoante_fim: c_str = choice_s_epsilon("l", "m", "n", "s", "z", "rn", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

    silaba_primeira_random: c_str = choice_s(seq_s(vogal, consoante_fim), seq_s(consoante_inicio, vogal, consoante_fim))
    silaba_meio_random: c_str = choice_s(seq_s(vogal, consoante_fim), seq_s(consoante_meio, vogal, consoante_fim))
    silaba_fim_random: c_str = choice_s_epsilon("man", "man", "vic", "ov", "son", "son", "er", "ão", "an", "ã", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")

    sobrenome_random_c: c_str = seq_s(
        silaba_primeira_random,
        choice_s(silaba_meio_random, silaba_meio_random, silaba_meio_random, silaba_meio_random, seq_s(silaba_meio_random, silaba_meio_random), seq_s(silaba_meio_random, silaba_meio_random), seq_s(silaba_meio_random, silaba_meio_random, silaba_meio_random)),
        silaba_fim_random
    )
    def triplicou(nome: str) -> bool:
        for x in 'abcdefghijklmnopqrstuvwxyzç':
            if (x + x + x) in nome:
                return True
        return False
    x: str = 'u'
    while len(x) < 4 or triplicou(x) or contem_texto(x, 'aa', 'ee', 'ii', 'oo', 'uu', 'yy', 'ãã', 'çe', 'çi', 'aã', 'ãa') or (contem_texto(x, 'k', 'y', 'w') and contem_texto(x, 'ã', 'ç')):
        x = sobrenome_random_c()
    return up(x)()

sobrenome: c_str = choice_s(
    sobrenome_normal, sobrenome_normal, sobrenome_normal, sobrenome_random,
    sobrenome_normal, sobrenome_normal, sobrenome_normal, sobrenome_random, 
    sobrenome_normal, sobrenome_normal, sobrenome_normal, sobrenome_random,
    sobrenome_random_japones
)

@dataclass(frozen = True)
class Pessoa:
    nome: str
    masc: bool

def colisao(a: str, b: str) -> bool:
    return len(set(a.strip().split(" ")) & set(b.strip().split(" "))) != 0

def sufixo(masc: bool, i: int) -> str:
    if masc and i < 10: return ' Júnior'
    if masc and i < 13: return ' Neto'
    if i == 13: return ' Terceiro'
    return ''

def pessoa_random(distribuicao: Sequence[bool] = (True, False)) -> Pessoa:
    masc: bool = random_element(*distribuicao)

    a1: str = (nome_masculino() if masc else nome_feminino())
    nome: str = a1

    a2: str = ''
    if random_element(True, False):
        a2 = a1
        while colisao(nome, remove_de(a2)): a2 = (nome_masculino() if masc else nome_feminino())
        nome += ' ' + a2

    s1: str = a1
    while colisao(nome, remove_de(s1)): s1 = sobrenome()
    nome += ' ' + s1

    if random_element(True, False):
        s2: str = s1
        while colisao(nome, remove_de(s2)): s2 = sobrenome()
        nome += ' ' + s2
        if random_element(True, False, False, False):
            s3: str = s1
            while colisao(nome, remove_de(s3)): s3 = sobrenome()
            nome += ' ' + s3

    s4: str = a1
    while colisao(nome, s4.strip()): s4 = sufixo(masc, random.randint(0, 100))
    nome += s4

    return Pessoa(nome, masc)