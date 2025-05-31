import admin
import usuario
import index

def painel_usuario(email_do_usuario_logado, nome_do_usuario_logado):
   while True:
      print(f"""
      ------Olá, {nome_do_usuario_logado}! ------
          
          1 - Pesquisar livro no catálogo
          2 - Meu acervo
          3 - Catalogo de livros
          4 - Adicionar livro
          0 - Logout

      """)

      opcao = input("Escolha uma opção: ")
      if opcao == '1':
        usuario.pesquisar_livro(email_do_usuario_logado)
      elif opcao == '2':
        usuario.meu_acervo(email_do_usuario_logado)
      elif opcao == '3':
        usuario.catalogo_de_livros(email_do_usuario_logado)
      elif opcao == '4':
        usuario.adicionar_livro_ao_acervo(email_do_usuario_logado)
      elif opcao == '0':
        print(f'Fazendo logout, {nome_do_usuario_logado}...')
        break
      else:
        print('Opção inválida!')
        
def painel_admin():
  while True:
    print(f"""
    ------ Painel do Administrador ------
          
          1 - Cadastrar usuário
          2 - Deletar usuário   
          3 - Cadastrar livro ao catálogo
          4 - Deletar livro
          5 - Pesquisar livro
          6 - Exibir o catálogo
          7 - Buscar usuário
          8 - Listar usuários
          0 - Sair
      """)
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
      nome = input('Nome do novo usuário: ')
      email = input('Email do novo usuário: ')
      senha = input('Senha para o novo usuário (min. 8 caracteres, 1 número): ')
      index.cadastrar_usuario(nome, email, senha)
    elif opcao == '2':
      admin.deletar_usuario()
    elif opcao == '3':
      admin.cadastrar_novo_livro()
      usuario.salvar_catalogo_global()
    elif opcao == '4':
      usuario.deletar_livro_catalogo()
      usuario.salvar_catalogo_global()
    elif opcao == '5':
      usuario.pesquisar_livro(None) # Coloquei none pq o admin busca no catalogo global, não vai precisar de um email
    elif opcao == '6':
      usuario.catalogo_de_livros(None) # aqui também não precisa de email
    elif opcao == '7':
      admin.buscar_usuario()
    elif opcao == '8':
      admin.listar_usuarios()
    elif opcao == '0':
      print('Saindo do painel de administrador...')
      break
    else:
      print('Opção inválida!')