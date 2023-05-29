vertebrados = {
    "classe": {
        "ave": {
            "alimentacao": {
                "onivoro": "Pomba",
                "carnivoro": "Águia",
            },
        },
        "mamifero": {
            "alimentacao": {
                "onivoro": "Homem",
                "herbivoro": "Vaca",
            },
        },
    },
}

invertebrados = {
    "classe": {
        "inseto": {
            "alimentacao": {
                "hematofago": "Pulga",
                "herbivoro": "Lagarta",
            },
        },
        "anelideo": {
            "alimentacao": {
                "hematofago": "Sanguessuga",
                "onivoro": "Minhoca",
            },
        },
    },
}

def organizar_entradas(A, B, C):
    # A
    if A == "vertebrado" or A == "invertebrado":
        tipo = A
    elif A == "ave" or A == "mamifero" or A =="inseto" or A== "anelideo":
        classe = A
    elif A == "onivoro" or A == "carnivoro" or A == "herbivoro" or A== "hematofago":
        alimentacao = A
    # B
    if B == "vertebrado" or B == "invertebrado":
        tipo = B
    elif B == "ave" or B == "mamifero" or B =="inseto" or B == "anelideo":
        classe = B
    elif B == "onivoro" or B == "carnivoro" or B == "herbivoro" or B == "hematofago":
        alimentacao = B
    # C
    if C == "vertebrado" or C == "invertebrado":
        tipo = C
    elif C == "ave" or C == "mamifero" or C =="inseto" or C == "anelideo":
        classe = C
    elif C == "onivoro" or C == "carnivoro" or C == "herbivoro" or C == "hematofago":
        alimentacao = C

    return tipo, classe, alimentacao


def buscar_animal(tipo, classe, alimentacao):
    if tipo == "vertebrado":
        if classe in vertebrados["classe"]:
            if alimentacao in vertebrados["classe"][classe]["alimentacao"]:
                return vertebrados["classe"][classe]["alimentacao"][alimentacao]
    elif tipo == "invertebrado":
        if classe in invertebrados["classe"]:
            if alimentacao in invertebrados["classe"][classe]["alimentacao"]:
                return invertebrados["classe"][classe]["alimentacao"][alimentacao]

print("Digite informações sobre o Animal desejado: \n")

A = input("Informação 1 => ").lower()
B = input("Informação 2 => ").lower()
C = input("Informação 3 => ").lower()

entradas = organizar_entradas(A, B, C)

tipo = entradas[0]
classe = entradas[1]
alimentacao = entradas[2]

resultado = buscar_animal(tipo, classe, alimentacao)

print(f"O animal que voce buscou é um(a): {resultado}" )
