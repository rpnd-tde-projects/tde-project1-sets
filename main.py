# Aluno: Renato Pestana de Gouveia


"""
ENUNCIADO:
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações.
Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa:

1) a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro;

2) as linhas seguintes seguirão sempre o mesmo padrão de três linhas:
    2.1) a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano);
    2.2) a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas.

Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.

A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação.
No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir:

    União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}

Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos.
Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saída acima.
Observe as letras maiúsculas e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.

Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de operações, operações com dados diferentes, 
e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github.

Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor.
"""


from core.validation import prompt_for_valid_file, validate_operations_number, is_input_file_empty
from core.functions import union, intersection, difference, cartesian_product
from typing import Union


print("Programa de Operações com Conjuntos")

lines: list[str] = prompt_for_valid_file()
is_input_file_empty(lines)

operations_number: str = lines[0].strip()
validate_operations_number(operations_number)

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
        result: Union[set, str] = intersection(set1, set2)
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
