# Aluno: Renato Pestana de Gouveia


def prompt_for_valid_file() -> list[str]:
    """
    Solicita ao usuário que insira o nome de um arquivo válido e retorna as linhas do arquivo.

    Parâmetros:
        None: A função não recebe parâmetros. Apenas solicita ao usuário o nome de um arquivo.

    Retorno:
        list[str]: Uma lista de strings, onde cada elemento representa uma linha do arquivo.
    """
    while True:
        file_name: str = input("Digite o nome do arquivo texto: ")
        try:
            with open(file=file_name, mode="rt") as file:
                lines: list[str] = file.readlines()
            return lines
        except FileNotFoundError:
            print(f"Arquivo '{file_name}' não encontrado. Por favor, tente novamente.\n")


def is_input_file_empty(input_file: list[str]) -> None:
    """
    Verifica se o arquivo de entrada está vazio. Se estiver, exibe uma mensagem e encerra o programa.

    Parâmetros:
        input_file (list[str]): Uma lista de strings, onde cada elemento representa uma linha do arquivo de entrada.

    Retorno:
        None: A função não retorna valor, mas encerra o programa se o arquivo estiver vazio.
    """
    if len(input_file) == 0:
        print("Arquivo de entrada está vazio. Encerrando o programa.")
        exit()


def validate_operations_number(input: str) -> None:
    """
    Verifica se o número de operações é um número inteiro válido. Se não for, exibe uma mensagem e encerra o programa.

    Parâmetros:
        input (str): A string que representa o número de operações a ser validado.

    Retorno:
        None: A função não retorna valor, mas encerra o programa se a string não for um número inteiro válido.
    """
    if not input.isdigit():
        print("O número de operações deve ser um número inteiro. Encerrando o programa.")
        exit()

