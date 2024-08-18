def get_valid_input_file() -> list[str]:
    """
    Solicita ao usuário que insira o nome de um arquivo válido e retorna as linhas do arquivo.

    Parâmetros:
        None: A função não recebe parâmetros. Apenas solicita ao usuário o nome de um arquivo.

    Retorno:
        list[str]: Uma lista de strings, onde cada elemento representa uma linha do arquivo.
    """
    while True:
        input_file: str = input("Digite o nome do arquivo texto: ")
        try:
            with open(file=input_file, mode="rt") as file:
                lines: list[str] = file.readlines()
            return lines
        except FileNotFoundError:
            print(f"Arquivo '{input_file}' não encontrado. Por favor, tente novamente.\n")


def add_color_to_text(text: str, color: str) -> str:
    """
    Adiciona cor a um texto utilizando sequências de escape ANSI.

    Parâmetros:
        text (str): O texto ao qual a cor será aplicada.
        color (str): A cor desejada. Opções válidas: 'red', 'green', 'yellow', 'blue'.

    Retorno:
        str: O texto com a cor aplicada.
    """
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m"
    }
    return f"{colors[color]}{text}\033[0m"

