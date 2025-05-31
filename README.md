# 📚 Sistema de Biblioteca Digital

## 🎯 Objetivo do Sistema

Gerenciar uma biblioteca digital, permitindo que usuários acessem, cadastrem e gerenciem livros em seus acervos, enquanto administradores mantêm o controle do catálogo e dos usuários.

---

## ✅ Requisitos Funcionais

### 👤 Usuário

- **[RF01] Escolher tipo de usuário:**  
  O sistema irá permitir que a pessoa escolha se vai acessar o sistema como usuário ou administrador.

- **[RF02] Fazer login:**  
  O sistema deve permitir o usuário fazer login com email e senha.

- **[RF03] Recuperar senha:**  
  O sistema deve permitir que o usuário recupere sua senha.

- **[RF04] Cadastrar:**  
  O sistema deve permitir o cadastro com nome completo, e-mail válido, senha e confirmação de senha.

- **[RF05] Pesquisar livro:**  
  O sistema deve permitir a pesquisa de livros pelo título.

- **[RF06] Adicionar livro no acervo:**  
  O sistema deve permitir o usuário adicionar livros ao seu acervo.

- **[RF07] Deletar livro do acervo:**  
  O sistema deve permitir que o usuário remova livros de seu acervo.

- **[RF08] Favoritar livro:**  
  O sistema deve permitir que o usuário adicione livros aos favoritos.

- **[RF09] Exibir catálogo de livros:**  
  O sistema deve permitir acesso ao catálogo de livros da biblioteca.

- **[RF10] Abrir livro:**  
  O sistema deve permitir que o usuário abra livros do catálogo ou de seu acervo.

---

### 🛠️ Administrador

- **[RF11] Cadastrar usuário:**  
  O sistema deve permitir o cadastro de usuários com email válido, senha, confirmação de senha e nome completo.

- **[RF12] Deletar usuário:**  
  O sistema deve permitir que o administrador exclua contas de usuários.

- **[RF13] Cadastrar livro ao catálogo:**  
  O sistema deve permitir o cadastro de livros com título, autor e gênero.

- **[RF14] Deletar livro:**  
  O sistema deve permitir a exclusão de livros pelo título.

- **[RF15] Pesquisar livro:**  
  O sistema deve permitir pesquisar livros.

- **[RF16] Exibir o catálogo:**  
  O sistema deve permitir exibir o catálogo completo.

- **[RF17] Buscar usuário:**  
  O sistema deve permitir a busca de usuários pelo e-mail.

- **[RF18] Listar usuários:**  
  O sistema deve permitir listar todos os usuários cadastrados.

---

## ⚙️ Requisitos Não Funcionais

- **[RNF01] Banco de Dados:**  
  Os dados dos usuários devem ser armazenados em arquivos `.txt`.

- **[RNF02] Segurança:**  
  As senhas devem ser criptografadas.

---

## 📏 Regras de Negócio

1. O usuário só poderá cadastrar uma conta por e-mail.
2. O limite do acervo do usuário é de até 5 livros.
3. A senha deve conter no mínimo 8 caracteres, sendo ao menos 7 letras e 1 número.

---

