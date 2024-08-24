# Aluno: Renato Pestana de Gouveia


from core.utils import add_color_to_text
from typing import Union


def union(set1: set, set2: set) -> set:
    """
    Retorna a união de dois conjuntos.

    Parâmetros:
        set1 (set): O primeiro conjunto.
        set2 (set): O segundo conjunto.

    Retorno:
        set: Um novo conjunto contendo todos os elementos presentes em set1 ou set2.
    """
    return set1.union(set2)


def intersection(set1: set, set2: set) -> Union[set, str]:
    """
    Retorna a interseção de dois conjuntos. Caso os conjuntos sejam disjuntos, retorna "Disjunção".

    Parâmetros:
        set1 (set): O primeiro conjunto.
        set2 (set): O segundo conjunto.

    Retorno:
        Union[set, str]: Um novo conjunto contendo os elementos comuns a set1 e set2,
        ou uma string "Disjunção" se não houver elementos em comum.
    """
    if set1.isdisjoint(set2):
        return add_color_to_text("Disjunção", "red")
    else:
        return set1.intersection(set2)


def difference(set1: set, set2: set) -> Union[set, str]:
    """
    Retorna a diferença entre dois conjuntos. Caso os conjuntos sejam disjuntos, retorna "Disjunção".

    Parâmetros:
        set1 (set): O primeiro conjunto.
        set2 (set): O segundo conjunto.

    Retorno:
        set ou str: Um novo conjunto contendo os elementos presentes em set1, mas não em set2,
                    ou a string "Disjunção" se os conjuntos forem disjuntos.
    """
    if set1.isdisjoint(set2):
        return add_color_to_text("Disjunção", "red")
    else:
        return set1.difference(set2)


def cartesian_product(set1: set, set2: set) -> set:
    """
    Retorna o produto cartesiano de dois conjuntos.

    Parâmetros:
        set1 (set): O primeiro conjunto.
        set2 (set): O segundo conjunto.

    Retorno:
        set: Um novo conjunto contendo pares ordenados (tuplas), onde cada par é formado 
        por um elemento de set1 e um elemento de set2.
    """
    result = set()
    for i in set1:
        for j in set2:
            result.add((i, j))
    return result
