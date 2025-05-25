def criar_arquivo(nome_arquivo):
    """Cria um arquivo e grava 3 frases nele."""
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write("Hoje aprendi sobre manipulação de arquivos.\n")
        file.write("Python facilita muito o trabalho com arquivos.\n")
        file.write("Este é um exercício prático de escrita e leitura.\n")

def adicionar_frases(nome_arquivo):
    """Adiciona 2 frases ao arquivo existente."""
    with open(nome_arquivo, 'a', encoding='utf-8') as file:
        file.write("Adicionar conteúdo é simples com 'a'.\n")
        file.write("Agora o arquivo tem 5 frases.\n")

def ler_arquivo(nome_arquivo):
    """Lê e imprime o conteúdo do arquivo."""
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
        print(conteudo)

def main():
    """Função principal do script."""
    nome_arquivo = 'minhas_notas.txt'
    criar_arquivo(nome_arquivo)
    adicionar_frases(nome_arquivo)
    ler_arquivo(nome_arquivo)

if __name__ == "__main__":
    main()
