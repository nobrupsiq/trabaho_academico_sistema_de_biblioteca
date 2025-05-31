import os
import json

livros = [
  {
    'titulo': 'Harry Potter e a Camara Secreta',
    'autor': 'J. K. Rowling',
    'genero': 'Fantasia',
    'livro': 'Livros/harry-potter-e-a-camara-secreta.pdf'
  },
  {
    'titulo': 'Entendendo Algoritmos',
    'autor': 'Aditya Y. Bhargava',
    'genero': 'Tecnologia',
    'livro': 'Livros/Entendendo_Algoritmos.pdf'
  },
  {
    'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
    'autor': 'J.R.R. Tolkien',
    'genero': 'Fantasia',
    'livro': 'Livros/sociedade_do_anel.pdf'
  }
]

arquivo_de_usuario_acervo = "acervos_usuarios.json"

def carregar_acervos_dos_usuarios():
  try:
    with open(arquivo_de_usuario_acervo, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return {} # AQUI VOU RETORNAR UM DICIONARIO VAZIO SE NÃO EXISTIR ARQUIVO
  except json.JSONDecodeError:
    return {} # Retorna dicionario vazio também se o arquivo estiver mal formatado

def salvar_acervos_dos_usuarios(dados_do_acervo):
  with open(arquivo_de_usuario_acervo, 'w') as f:
    json.dump(dados_do_acervo, f, indent = 2, ensure_ascii = False)

def abrir_pdf_do_livro(livro_selecionado):
  # Aqui vamos extrair a função pesquisar_livro
  caminho_do_pdf = livro_selecionado.get('livro')
  
  if not caminho_do_pdf:
    print('Caminho do PDF não especificado para este livro.')
    return
  
  base_dir = os.path.dirname(os.path.abspath(__file__))
  caminho_pdf_absoluto = os.path.join(base_dir, caminho_do_pdf)
  caminho_pdf_absoluto = os.path.normpath(caminho_pdf_absoluto)

  if os.path.exists(caminho_pdf_absoluto):
    print(f'Arquivo PDF: Disponível em {caminho_pdf_absoluto}')
    abrir_pdf = input('Deseja abrir o arquivo PDF? (S/N)').lower()
    if abrir_pdf == 's':
      try:
        if os.name == 'nt': #NT quer dizer que o sistema operacional é Windows
          os.startfile(caminho_pdf_absoluto)
        else:
          print('Abertura de PDF não suportada nesse OS!')
        print(f'Tentando abrir {livro_selecionado['titulo']}...')
      except Exception as e:
        print(f'Não foi possível abrir o PDF automaticamente: {e}')
        print(f'Verifique se você possui algum programa para abrir PDF!')
        print(f'Caminho do arquivo: {caminho_pdf_absoluto}')
    else:
      print('Ok, não abrindo o PDF.')
  else:
    print(f'Arquivo PDF: Não encontrado em {caminho_pdf_absoluto}')
    print(f'Verifique o caminho do arquivo no cadastro do livro e a estrutura das pastas.')
    
def pesquisar_livro(email_do_usuario_logado):
  termo_da_pesquisa = input('Digite o título ou autor do livro: ').lower()
  encontrados = []

  for livro_item in livros:
    if termo_da_pesquisa in livro_item['titulo'].lower() or \
      termo_da_pesquisa in livro_item['autor'].lower():
      encontrados.append(livro_item)

  if not encontrados:
    print("Nenhum livro encontrado com esse termo.")
    return
  
  print("\n--- Livros Encontrados ---")
  for idx, livro_item in enumerate(encontrados):
    print(f"{idx + 1}. Título: {livro_item['titulo']} | Autor: {livro_item['autor']}")
  
  while True:
    try:
      escolha_str = input("Digite o número do livro para ver mais detalhes ou abrir (0 para voltar): ")
      
      if not escolha_str: 
        print('Nenhuma entrada. Por favor, digite um número ou 0.')
        continue # Volta para o inicio do loop while
      escolha = int(escolha_str)
      if escolha == 0:
        break
      if 1 <= escolha <= len(encontrados):
        livro_selecionado = encontrados[escolha - 1]
        
        print(f"\n--- Detalhes do Livro ---")
        print(f"Título: {livro_selecionado['titulo']}")
        print(f"Autor: {livro_selecionado['autor']}")
        print(f"Gênero: {livro_selecionado['genero']}")
        
        abrir_pdf_do_livro(livro_selecionado) # Irá adicionar ao acervo pessoal diretamente da pesquisa de livro também

        if email_do_usuario_logado is not None: # Verifica se não é o admin
            adicionar_acervo = input('Deseja adicionar este livro ao seu acervo pessoal? (s/n): ').lower() # Corrigido para ter ':'
            if adicionar_acervo == 's':
              adicionar_livro_especifico_ao_acervo(email_do_usuario_logado, livro_selecionado)
        break # Sai do loop após processar a escolha do livro
      else:
        print('Escolha inválida. Digite um número da lista ou (0 para voltar).')
    except ValueError:
      print('Entrada inválida. Por favor, digite um número inteiro ou (0 para voltar).')
    except Exception as e:
      print(f'Erro inesperado: {e}')
        
def adicionar_livro_especifico_ao_acervo(email_do_usuario, livro_obj_original):
  dados_do_acervo = carregar_acervos_dos_usuarios()
  acervo_do_usuario = dados_do_acervo.get(email_do_usuario, [])
  
  
  # Comparar em minusculas para evitar duplicata
  titulo_original_lower = livro_obj_original['titulo'].lower()
  autor_original_lower = livro_obj_original['autor'].lower()
  # Aqui eu verifico se o livro já está no acervo do usuário pelo título e autor
  for livro_existente in acervo_do_usuario:
    if livro_existente['titulo'].lower() == titulo_original_lower and \
      livro_existente['autor'].lower() == autor_original_lower:
        print(f'O livro "{livro_obj_original['titulo']}" ja esta no seu acervo.')
        return
  # AQUI EU CRIEI UMA COPIA PARA NAO MODIFICAR A LISTA ORIGINAL
  livro_para_adicionar = livro_obj_original.copy()
  livro_para_adicionar['favorito'] = False
  
  acervo_do_usuario.append(livro_para_adicionar)
  dados_do_acervo[email_do_usuario] = acervo_do_usuario
  salvar_acervos_dos_usuarios(dados_do_acervo)
  print(f'Livro "{livro_para_adicionar['titulo']}" adicionado ao seu acervo com sucesso!')

def catalogo_de_livros(email_do_usuario_logado):
  if not livros:
    print('Nenhum livro no catálogo geral.')
    return
  
  print("\n--- Catálogo de livros ---\n")
  
  for indice, livro_item in enumerate(livros):
    print(f"{indice + 1}. Título: {livro_item['titulo']} | Autor: {livro_item['autor']}")
    
  if email_do_usuario_logado is None:
    return
  
  while True:
    try:
      escolher_livro_do_catalogo = input('Digite o número do livro para adicionar ao seu acervo (ou 0 para voltar): ')
      if not escolher_livro_do_catalogo: # se o input ficou vazio
        print('Nenhuma seleção feita.')
        continue
      
      escolha = int(escolher_livro_do_catalogo)
      if escolha == 0:
        break
      if 1 <= escolha <= len(livros):
        livro_para_adicionar = livros[escolha -1]
        adicionar_livro_especifico_ao_acervo(email_do_usuario_logado, livro_para_adicionar)
        
        # AQUI É IMPORTANTE POIS NÃO SAI DO LOOP, PERMITE ADICIONAR MAIS LIVROS
      else:
        print('Número de livro inválido.')
    except ValueError:
      print('Entrada inválida. Por favor, digite um número.')
    except Exception as e:
      print(f'Ocorreu um erro: {e}')
      
def adicionar_livro_ao_acervo(email_do_usuario_logado):
  if not livros:
    print('Nenhum livro disponível no catálogo para adicionar.')
    return

  print("\n--- Adicionar livro do catálogo ao seu acervo ---")
  for indice, livro_item in enumerate(livros):
    print(f'{indice + 1}. Título: {livro_item['titulo']} | Autor: {livro_item['autor']}')
    
  while True:
    try:
      escolha_str = input('Digite o número do livro que deseja adicionar ao seu acervo (0 para voltar): ')
      if not escolha_str:
        print('Nenuma seleção feita.')
        continue
      escolha = int(escolha_str)
      
      if escolha == 0:
        break
      if 1 <= escolha <= len(livros):
        livro_selecionado = livros[escolha -1]
        adicionar_livro_especifico_ao_acervo(email_do_usuario_logado, livro_selecionado)
        
      else:
        print('Escolha inválida. Digite um número da lista.')
    except ValueError:
      print('Entrada inválida. Digite um número.')
    except Exception as e:
      print(f'Ocorreu um erro: {e}')
      
def meu_acervo(email_do_usuario_logado):
  while True:
    acervo_dados = carregar_acervos_dos_usuarios()
    acervo_pessoal = acervo_dados.get(email_do_usuario_logado, [])
    
    if not acervo_pessoal:
      print('Seu acervo pessoal está vazio.')
      voltar = input('Pressione Enter para voltar ao menu anterior ou digite "s" para sair: ')
      if voltar.lower() == 's':
        return
      else:
        return
    
    print('\n---- Meu acervo ----')
    for indice, livro_item in enumerate(acervo_pessoal):
      status_favorito = "★" if livro_item.get('favorito', False) else "☆"
      print(f'{indice + 1}. {status_favorito} Titulo: {livro_item['titulo']} | Autor: {livro_item['autor']}')
    
    print("\nOpções do Acervo:")
    print(" -  Digite o número do livro para ver detalhes, abrir ou remover.")
    print(" - 'F' para listar seus livros favoritos.")
    print(" - 'M' para marcar/desmarcar um livro como favorito.")
    print(" - '0' para voltar ao menu anterior.")
    
    escolha_menu_acervo = input('Escolha uma opção: ').lower().strip()
    
    if escolha_menu_acervo == '0':
      break
    elif escolha_menu_acervo == 'f':
      listar_apenas_favoritos(email_do_usuario_logado)
    elif escolha_menu_acervo == 'm':
      alternar_status_favorito(email_do_usuario_logado)
      # quando desmarcar, o loop principal do meu_acervo vai continuar recarregando e mostrando a lista atualizada
    else:
      try:
        escolha_num = int(escolha_menu_acervo)  
        if 1 <= escolha_num <= len(acervo_pessoal):
          livro_selecionado = acervo_pessoal[escolha_num -1]
          
          print(f"\n--- Detalhes do Livro ---")
          print(f"Título: {livro_selecionado['titulo']}")
          print(f"Autor: {livro_selecionado['autor']}")
          print(f"Gênero: {livro_selecionado['genero']}")
          status_favorito_detalhe = "Sim" if livro_selecionado.get('favorito', False) else "Não"
          print(f"Favorito: {status_favorito_detalhe}")
          
          abrir_pdf_do_livro(livro_selecionado)
          
          remover = input(f'Deseja remover "{livro_selecionado['titulo']}" do seu acervo? (s/n): ').lower()
          if remover == 's':
            livro_removido = acervo_pessoal.pop(escolha_num -1)
            acervo_dados[email_do_usuario_logado] = acervo_pessoal
            salvar_acervos_dos_usuarios(acervo_dados) # Salva no JSON
            print(f'Livro "{livro_removido['titulo']}" removido do seu acervo.')
        else:
          print('Número de livro inválido. Escolha um número da lista.')
      except ValueError:
        print('Entrada inválida. Digite um número, "F", "M" ou "0"')
      except Exception as e:
        print(f'Erro: {e}')
      
def alternar_status_favorito(email_do_usuario_logado):
  dados_do_acervo = carregar_acervos_dos_usuarios()
  acervo_pessoal = dados_do_acervo.get(email_do_usuario_logado, [])
  
  if not acervo_pessoal:
    print('Seu acervo pessoal está vazio. Adicione livros primeiro.')
    return
  
  print('\n ---- Marcar/Desmarcar livro como favorito ----')
  for indice, livro_item in enumerate(acervo_pessoal):
    status_favorito = "★" if livro_item.get('favorito', False) else "☆"
    print(f'{indice + 1}. {status_favorito} Título: {livro_item['titulo']} | Autor: {livro_item['autor']}')
    
  while True:
    try:
      escolha_str = input('Digite o número do livro para alterar o status de favorito (0 para voltar): ')
      if not escolha_str: continue
      escolha_index = int(escolha_str)
      
      if escolha_index == 0:
        break
      if 1 <= escolha_index <= len(acervo_pessoal):
        livro_selecionado = acervo_pessoal[escolha_index -1]
        # AQUI ALTERNA O STATUS DE FAVORITO. USEI .GET PARA CASO O CAMPO NÃO EXISTA
        livro_selecionado['favorito'] = not livro_selecionado.get('favorito', False)
        status_atual = 'favorito' if livro_selecionado['favorito'] else 'não favorito'
        print(f'"{livro_selecionado['titulo']}" foi marcado como {status_atual}.')
        
        salvar_acervos_dos_usuarios(dados_do_acervo)
        
        print('\n---- Status Atualizado ----')
        for indice, livro_item in enumerate(acervo_pessoal):
          status_favorito = "★" if livro_item.get('favorito', False) else "☆"
          print(f'{indice + 1}. {status_favorito} Titulo: {livro_item['titulo']} | Autor: {livro_item['autor']}')
      else:
        print('Escolha inválida.')
    except ValueError:
      print('Entrada inválida. Digite um número.')
    except Exception as e:
      print(f'Erro: {e}')
      
def listar_apenas_favoritos(email_do_usuario_logado):
  dados_do_acervo = carregar_acervos_dos_usuarios()
  acervo_pessoal = dados_do_acervo.get(email_do_usuario_logado, [])
  
  livros_favoritos = [livro for livro in acervo_pessoal if livro.get('favorito', False)]
  
  if not livros_favoritos:
    print('Você ainda não marcou nennhum livro como favorito.')
    return
  
  print('\n---- Seus livros favoritos ★ ----')
  for indice, livro_item in enumerate(livros_favoritos):
    print(f'{indice + 1}. ★ Titulo: {livro_item['titulo']} | Autor: {livro_item['autor']}')
    
  while True:
    try:
      escolha_str = input('Digite o número do livro favorito para ver detalhes e abrir (0 para voltar)')
      if not escolha_str: continue
      escolha_index = int(escolha_str)
      
      if escolha_index == 0:
        break
      if 1 <= escolha_index <= len(livros_favoritos):
        livro_selecionado = livros_favoritos[escolha_index -1]
        print(f'\n---- Detalhes do livro favorito ----')
        print(f'Titulo: {livro_selecionado['titulo']}')
        print(f'Autor: {livro_selecionado['autor']}')
        print(f'Gênero: {livro_selecionado['genero']}')
        abrir_pdf_do_livro(livro_selecionado)
        break
      else:
        print('Escolha inválida.')
    except ValueError:
      print('Entrada inválida. Digite um número.')
    except Exception as e:
      print(f'Erro: {e}')
      
catalogo_de_livros_arq = 'catalogo_livros.json'

def carregar_catalogo_global():
    global livros # Para modificar a lista global 'livros'
    try:
        with open(catalogo_de_livros_arq, 'r') as f:
            livros = json.load(f) # Lendo os dados de um arquivo JSON
    except FileNotFoundError:
        # Se o arquivo não existe, usa a lista 'livros' hardcoded como padrão
        # e a salva para futuras execuções.
        # Demorei a entender mas é basicamente isso
        # Quando o sistema não encontra o arquivo, ele:
        #  - Avisa o usuário.
        #  - Usa um catálogo padrão que está no código.
        #  - Cria um novo arquivo com esse catálogo.
        print(f"Arquivo '{catalogo_de_livros_arq}' não encontrado. Usando catálogo padrão e criando arquivo.")
        salvar_catalogo_global()
    except json.JSONDecodeError:
        print(f"Erro ao decodificar '{catalogo_de_livros_arq}'. Usando catálogo padrão.")
    #    é basicamente isso
    #     - Arquivo não existe → usa o catálogo padrão e cria o arquivo novo.
    #     - Arquivo existe mas está corrompido (JSON inválido) → usa o catálogo padrão, mas sem sobrescrever o arquivo automaticamente.
    
def salvar_catalogo_global():
    # Aqui salva o catalogo global de livros no arquivo JSON
    with open(catalogo_de_livros_arq, 'w') as f:
        json.dump(livros, f, indent=2, ensure_ascii=False)
        # A função json.dump() do módulo json escreve dados em formato JSON diretamente em um arquivo.
        # livros: é o objeto Python que será salvo — normalmente uma lista de dicionários com dados dos livros.
        # f: é o arquivo aberto (por exemplo, com open('livros.json', 'w', encoding='utf-8')) onde os dados serão escritos.
        #Indent=2: Formata o JSON com identação de 2 espaços, tornando o arquivo mais legível
        
def deletar_livro_catalogo():
    print("\n--- Deletar Livro do Catálogo ---")
    if not livros:
      print("O catálogo está vazio. Nenhum livro para deletar.")
      return

    for idx, livro_item in enumerate(livros):
      print(f"{idx + 1}. Título: {livro_item['titulo']} | Autor: {livro_item['autor']}")
    
    try:
      escolha_str = input("Digite o número do livro que deseja deletar (0 para cancelar): ").strip()
      if not escolha_str:
        print("Nenhuma seleção. Deleção cancelada.")
        return
        
      escolha_index = int(escolha_str)

      if escolha_index == 0:
        print("Deleção cancelada.")
        return
      
      if 1 <= escolha_index <= len(livros):
        livro_deletado = livros.pop(escolha_index - 1) # Remove o livro da lista e o retorna
        print(f"Livro '{livro_deletado['titulo']}' por '{livro_deletado['autor']}' foi deletado do catálogo.")
        
        salvar_catalogo_global()
      else:
        print("Número de livro inválido.")
    except ValueError:
      print("Entrada inválida. Por favor, digite um número.")
    except Exception as e:
      print(f"Ocorreu um erro: {e}")