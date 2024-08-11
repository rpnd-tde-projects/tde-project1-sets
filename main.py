from core.functions import union, intersection, difference
from core.utils import get_valid_input_file


print("Programa de Operações com Conjuntos")

lines: list[str] = get_valid_input_file()
operations_number: str = lines[0].strip()
operations_counter: int = 0

i = 1
while i < len(lines):
    operation = lines[i].strip()

    set1 = set(lines[i + 1].strip().split(', '))
    set2 = set(lines[i + 2].strip().split(', '))

    if operation == "U":
        result = union(set1, set2)
        print(f"\nUnião: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}")
        operations_counter += 1
    
    elif operation == "I":
        result = intersection(set1, set2)
        print(f"Interseção: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}")
        operations_counter += 1

    elif operation == "D":
        result = difference(set1, set2)
        print(f"Diferença: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}")
        operations_counter += 1

    """
    elif operation == "C":
        result = cartesian_product(set1, set2)
        print(f"Produto Cartesiano: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}")
        operations_counter += 1
    """

    i += 3

print(f"\nNúmero total de operações realizadas: {operations_counter}/{operations_number}")
