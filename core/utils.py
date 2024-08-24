# Aluno: Renato Pestana de Gouveia


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

