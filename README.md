# 📦 Catálogo de Produtos e Categorias - Django API

Este projeto consiste em uma API REST desenvolvida em Django para a gestão de um catálogo de produtos. A aplicação foi estruturada com relacionamentos entre tabelas e configurada para deploy automatizado na nuvem utilizando o **AWS Elastic Beanstalk**.

---

## 💻 1. Configuração e Execução Local

Para rodar este projeto em ambiente de desenvolvimento, siga os passos:

1.  **Ambiente Virtual (venv):**
    * Certifique-se de utilizar o Python 3.12.
    * Crie o ambiente: `python -m venv venv`
    * Ative o ambiente: `.\venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac).

2.  **Instalação de Dependências:**
    * Instale os pacotes necessários: `pip install -r requirements.txt`

3.  **Banco de Dados (SQLite):**
    * Gere os arquivos de migração: `python manage.py makemigrations`
    * Aplique as migrações ao banco local: `python manage.py migrate`

4.  **Execução:**
    * Inicie o servidor de desenvolvimento: `python manage.py runserver`
    * Acesse a API em: `http://127.0.0.1:8000/api/produtos/`

---

## 🛠️ 2. Alterações Realizadas e Modelagem

O projeto foi evoluído para suportar uma estrutura de dados relacional e requisitos de produção exigidos no cenário:

* **Entidade Categoria:** Implementada a classe `Categoria` para permitir a organização dos produtos.
* **Relacionamento:** Utilização de `ForeignKey` na classe `Produto`, estabelecendo um relacionamento de Muitos-para-Um (Many-to-One) com a classe `Categoria`.
* **Ajustes de Segurança:** Configuração dinâmica do `ALLOWED_HOSTS` no arquivo `settings.py` para ler variáveis de ambiente da AWS via `os.getenv`.
* **Serialização:** O `ProdutoSerializer` foi configurado para retornar os detalhes da categoria associada, facilitando o consumo por aplicações frontend.
* **Mídia e Estáticos:** Configuração de `STATIC_ROOT` e `MEDIA_ROOT` para o gerenciamento de imagens de produtos (como o Omni-Man) e do CSS do painel administrativo.

---

## ☁️ 3. Implementação e Deploy (AWS Elastic Beanstalk)

O deploy foi realizado seguindo as melhores práticas de automação de infraestrutura:

1.  **Pacote de Deploy:** Criação de arquivo `.zip` otimizado, excluindo pastas de cache, ambiente virtual e banco de dados local.
2.  **Configurações de Software (.ebextensions):**
    * Criação do arquivo `db.config` para automação de tarefas.
    * **Migrações Automáticas:** Comando configurado para atualizar o banco de dados da AWS a cada deploy.
    * **Superusuário Automático:** Script shell para garantir a criação do usuário `admin` caso ele não exista, permitindo acesso imediato ao painel.
3.  **Variáveis de Ambiente:** Cadastro da chave `DJANGO_ALLOWED_HOSTS` no painel da AWS com o domínio oficial do ambiente.
4.  **Proxy de Arquivos:** Mapeamento dos caminhos `/static/` e `/media/` no console do Elastic Beanstalk para entrega correta de arquivos estáticos.

---

## 🔑 Acesso ao Projeto (Produção)

* **URL da API:** [COLE_AQUI_O_LINK_DA_AWS]/api/produtos/
* **Painel Administrativo:** [COLE_AQUI_O_LINK_DA_AWS]/admin/
* **Credenciais de Acesso:**
    * **Usuário:** `admin`
    * **Senha:** `senha123`

---
*Projeto desenvolvido para a disciplina de Big Data e Cloud Computing.*
