# TDE-Project1-Sets
TDE - Projeto 1: Programa de Operações com Conjuntos

# Visão Geral
Este projeto é um programa para efetuar operações de conjuntos com base em arquivos de texto como dados de entrada, e como dados de saída é impresso no terminal os resultados das operações.

# Primeiros passos
Siga estas etapas simples abaixo para utilizar este programa.

## Pré-requisitos
- Python (versão 3.12.3 ou superior): [Download Python](https://www.python.org/downloads/)

## Instalação
1. Clone o repositório para o seu ambiente local:

    ```bash
    git clone https://github.com/rpnd-tde-projects/tde-project1-sets.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd tde-project1-sets
    ```

## Uso Básico em ambiente local
1. **Inspecione os Dados:**
    - Foi preparado 3 arquivos textos na raíz do projeto nos quais possuem as intruções para realizar as operações para avaliação
    - Estes arquivos são: input_1.txt, input_2.txt e input_3.txt

2. **Execute o Script Principal:**
    ```bash
    python main.py
    ```

3. **Informe o arquivo texto como dado de entrada:**
    ```bash
    Programa de Operações com Conjuntos
    Digite o nome do arquivo texto: input_1.txt
    ```

    Se não informar corretamente o nome do arquivo texto irá gerar um erro que está tratado da seguinte forma:

    ```bash
    Programa de Operações com Conjuntos
    Digite o nome do arquivo texto: abacaxi
    Arquivo 'abacaxi' não encontrado. Por favor, tente novamente.

    Digite o nome do arquivo texto: 
    ```

## Resultados
Ao executar o programa os resultados serão impressos na tela conforme exemplo abaixo:
```bash
    União: conjunto 1 {'3', '67', '7', '5'}, conjunto 2 {'2', '4', '3', '1'}, Resultado: {'2', '67', '3', '5', '7', '4', '1'}
    Interseção: conjunto 1 {'10', '6', '8', '4', '2'}, conjunto 2 {'7', '5', '9', '3', '1'}, Resultado: Disjunção
    Diferença: conjunto 1 {'E', 'B', 'D', 'C', 'A'}, conjunto 2 {'B', 'X', 'C', 'Y'}, Resultado: {'E', 'D', 'A'}

    Número total de operações realizadas: 3/4
```

# Desenvolvimento
Este programa foi desenvolvido seguindo as boas práticas de programação em Python.
Para efetuar o desenvolvimento utilizei dos tutoriais disponíveis abaixo:

https://www.tutorialspoint.com/python/python_file_handling.htm
https://www.tutorialspoint.com/python/python_sets.htm
https://www.tutorialspoint.com/python/python_set_methods.htm
https://www.tutorialspoint.com/python/python_set_operators.htm

