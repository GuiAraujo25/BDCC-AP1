📦 Catálogo de Produtos e Categorias - Django API
Projeto desenvolvido para a disciplina de Big Data e Cloud Computing. Implementação de uma API REST com relacionamento entre entidades e deploy automatizado na AWS Elastic Beanstalk.

💻 1. Configuração e Execução Local
Para rodar este projeto em ambiente de desenvolvimento:

Ambiente Virtual (venv):

Utilize o Python 3.12.

Crie o ambiente: python -m venv venv

Ative o ambiente: .\venv\Scripts\activate (Windows) ou source venv/bin/activate (Linux/Mac).

Instalação de Dependências:

Instale os pacotes: pip install -r requirements.txt

Banco de Dados (SQLite):

Gere as migrações: python manage.py makemigrations

Aplique as migrações: python manage.py migrate

Execução:

Inicie o servidor: python manage.py runserver

Acesse a API em: http://127.0.0.1:8000/api/produtos/

🛠️ 2. Alterações Realizadas e Modelagem
O projeto foi evoluído para suportar uma estrutura de dados relacional e requisitos de produção:

Nova Classe Categoria: Implementada para organizar os produtos. Possui um relacionamento ForeignKey com a classe Produto (relacionamento de um-para-muitos).

Ajustes no settings.py: Configuração dinâmica do ALLOWED_HOSTS via variáveis de ambiente (os.getenv) para aceitar o domínio da AWS.

Serializers Avançados: O ProdutoSerializer foi atualizado para incluir detalhes da categoria pai (CategoriaSerializer), permitindo uma resposta JSON mais rica na API.

Arquivos Estáticos: Configuração de STATIC_ROOT e MEDIA_ROOT para garantir a persistência de imagens de produtos e estilos do painel administrativo.

☁️ 3. Documentação de Deploy (AWS Elastic Beanstalk)
O deploy foi realizado seguindo as etapas de automação de infraestrutura:

Preparação do Pacote (app.zip):

O arquivo de deploy foi gerado contendo apenas o código-fonte, excluindo arquivos de cache (__pycache__), banco de dados local (db.sqlite3) e ambiente virtual.

Automação via .ebextensions:

Foi criado um arquivo de configuração (db.config) para automatizar duas tarefas críticas durante o deploy:

Migrações Automáticas: O servidor executa o migrate assim que o código é descompactado.

Criação de Superusuário (Root): Implementação de um script shell que verifica a existência e cria automaticamente o usuário administrador para acesso ao painel /admin/ na nuvem.

Variáveis de Ambiente:

Cadastro da chave DJANGO_ALLOWED_HOSTS no console da AWS para validar o domínio do Elastic Beanstalk.

Serviço de Arquivos:

Configuração de caminhos de proxy no console da AWS para mapear /static/ e /media/ aos diretórios correspondentes na instância EC2.
