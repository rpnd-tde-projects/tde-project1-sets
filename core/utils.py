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

