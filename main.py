from core.functions import union, intersection, difference, cartesian_product
from core.utils import get_valid_input_file


print("Programa de Operações com Conjuntos")

lines: list[str] = get_valid_input_file()
operations_number: str = lines[0].strip()
operations_counter: int = 0

print("")

i = 1
while i < len(lines):
    operation: str = lines[i].strip()

    set1: set[str] = set(lines[i + 1].strip().split(', '))
    set2: set[str] = set(lines[i + 2].strip().split(', '))

    if operation == "U":
        result: set = union(set1, set2)
        text: str = f"União: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}"
        print(text)
        operations_counter += 1
    
    elif operation == "I":
        result: set = intersection(set1, set2)
        text: str = f"Interseção: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}"
        print(text)
        operations_counter += 1

    elif operation == "D":
        result: set = difference(set1, set2)
        text: str = f"Diferença: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}"
        print(text)
        operations_counter += 1

    elif operation == "C":
        result: set = cartesian_product(set1, set2)
        text: str = f"Produto Cartesiano: conjunto 1 {set1}, conjunto 2 {set2}, Resultado: {result}"
        print(text)
        operations_counter += 1

    i += 3

print(f"\nNúmero total de operações realizadas: {operations_counter}/{operations_number}")
