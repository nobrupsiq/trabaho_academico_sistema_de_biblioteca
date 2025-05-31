import index
import usuario

def listar_usuarios():
    usuarios = index.carregar_dados_usuarios()
    print("\n--- Usuários Cadastrados ---\n")
    if not usuarios:
        print('Nenhum usuário cadastrado.')
        return
    for usuario in usuarios:
        seguranca_da_senha = '*' * len(usuario['senha'])
        print(f"Nome: {usuario['nome']} | Email: {usuario['email']} | Senha: {seguranca_da_senha}")
        
def deletar_usuario():
    print("\n---- Deletar Usuário ----")
    email_para_deletar = input('Digite o email do usuário que deseja deletar: ')

    if not email_para_deletar:
        print('Nenhum email fornecido.')
        return

    usuarios = index.carregar_dados_usuarios()
    usuario_encontrado = False
    novos_usuarios = []
    
    for usuario in usuarios:
        if usuario['email'] == email_para_deletar:
            usuario_encontrado = True
            print(f'Usuário encontrado: Nome: {usuario['nome']}, Email: {usuario['email']}')
            confirmacao = input(f'Tem certeza que deseja deletar o usuário {usuario['nome']} (s/n): ').lower()
            if confirmacao == 's':
                print(f'Usuário {usuario['nome']} deletado com sucesso.')
            else:
                print('Deleção cancelada.')
                novos_usuarios.append(usuario) # Aqui eu mantenho o usuário se a deleção for cancelada
        else:
            novos_usuarios.append(usuario)
    
    if not usuario_encontrado:
        print(f'Usuário com email "{email_para_deletar}" não encontrado.')
        return
    
    # Aqui abaixo eu vou reescrever o arquivo dados.txt com a lista atualizada de usuários
    if len(novos_usuarios) < len(usuarios) or (usuario_encontrado and not any(u['email'] == email_para_deletar for u in novos_usuarios)):
        with open("dados.txt", 'w') as arq:# w para sobrescrever igual eu expliquei ali em cima
            for usuario in novos_usuarios:
                arq.write(f'{usuario['nome']}:{usuario['email']}:{usuario['senha']}\n')
    elif not usuario_encontrado:
        print(f'Nenhum usuário com o email "{email_para_deletar}" foi encontrado')
        
def cadastrar_novo_livro():
    print("\n--- Cadastrar Novo Livro ao Catálogo ---")
    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    genero = input("Gênero do livro: ").strip()
    # Para o caminho do PDF, podemos pedir apenas o nome do arquivo
    # e assumir que ele estará na pasta "Livros"
    nome_arquivo_pdf = input("Nome do arquivo PDF (ex: meu_livro.pdf): ").strip()
    
    if not (titulo and autor and genero and nome_arquivo_pdf):
        print("Todos os campos são obrigatórios. Cadastro cancelado.")
        return
    
    caminho_do_livro = f'Livros/{nome_arquivo_pdf}' #caminho do livro não tao certo
    
    for livro_existente in usuario.livros:
        if livro_existente['titulo'].lower() == titulo.lower() and \
            livro_existente['autor'].lower() == autor.lower():
                print(f'Erro: O livro "{titulo}" já existe no catálogo')
                return
    
    novo_livro = {
    'titulo': titulo,
    'autor': autor,
    'genero': genero,
    'livro': caminho_do_livro
    }
    
    usuario.livros.append(novo_livro)
    print(f'Livro "{titulo}" cadastrado com sucesso no catálogo!')


def buscar_usuario():
    print("\n--- Buscar Usuário ---")
    termo_da_pesquisa = input("Digite o nome ou email do usuário para buscar: ").lower().strip()

    if not termo_da_pesquisa:
        print("Nenhum termo de pesquisa fornecido.")
        return

    usuarios = index.carregar_dados_usuarios()
    encontrados = []

    for usuario in usuarios:
        if termo_da_pesquisa in usuario['nome'].lower() or \
           termo_da_pesquisa in usuario['email'].lower():
            encontrados.append(usuario)
    
    if not encontrados:
        print(f"Nenhum usuário encontrado com o termo '{termo_da_pesquisa}'.")
        return
    
    print("\n--- Usuários Encontrados ---")
    for usuario in encontrados:
        # Exibe sem a senha, ou com máscara se preferir
        mascara_senha_busca = '*' * len(usuario['senha'])
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Senha: {mascara_senha_busca}")