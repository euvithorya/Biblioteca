import sqlite3

def criar_tabela():
    conn = sqlite3.connect('livros.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def adicionar_livro(titulo, autor, ano_publicacao):
    conn = sqlite3.connect('livros.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    conn.commit()
    conn.close()
    print("Livro adicionado com sucesso!")

def listar_livros():
    conn = sqlite3.connect('livros.db')
    c = conn.cursor()

    c.execute('SELECT * FROM livros')
    livros = c.fetchall()

    if livros:
        print("Livros cadastrados:")
        for livro in livros:
            print(f"{livro[0]}. {livro[1]} - {livro[2]} ({livro[3]})")
    else:
        print("Nenhum livro encontrado.")
    
    conn.close()

def buscar_livro(titulo_busca):
    conn = sqlite3.connect('livros.db')
    c = conn.cursor()

    c.execute('SELECT * FROM livros WHERE titulo LIKE ?', ('%' + titulo_busca + '%',))
    livros = c.fetchall()

    if livros:
        print("Livros encontrados:")
        for livro in livros:
            print(f"{livro[0]}. {livro[1]} - {livro[2]} ({livro[3]})")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo_busca}'.")
    
    conn.close()

def menu():
    while True:
        print("\n1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano_publicacao = int(input("Ano de publicação: "))
            adicionar_livro(titulo, autor, ano_publicacao)
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            titulo_busca = input("Digite o título do livro que deseja buscar: ")
            buscar_livro(titulo_busca)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

criar_tabela()

if __name__ == "__main__":
    menu()

#:V