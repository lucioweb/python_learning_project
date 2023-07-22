# python_learning_project
Desmistificando o Python.
O aplicativo usará um banco de dados SQLite para armazenar usuários e postagens. 
Python vem com suporte embutido para SQLite no módulo sqlite3. 
O SQLite é conveniente porque não requer a configuração de um servidor de banco de dados separado e é integrado ao Python. 
No entanto, se as solicitações simultâneas tentarem gravar no banco de dados ao mesmo tempo, elas ficarão mais lentas à medida que cada gravação ocorrer sequencialmente. 
Aplicativos pequenos não perceberão isso. 
Depois de se tornar grande, você pode querer mudar para um banco de dados diferente.

## CRIANDO, IMPORTANDO E CONFIGURANDO O PROJETO
1 - Criação do repositório no github.
```
/home/user/Projects/flask-tutorial
├── flaskr/ (um pacote Python que contém o código e os arquivos do aplicativo.)
│   ├── __init__.py (contém a fábrica de aplicativos e informa ao Python que o diretório flaskr deve ser tratado como um pacote.)
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/ (um ambiente virtual Python onde o Flask e outras dependências são instalados.)
├── pyproject.toml
└── MANIFEST.in
```

2 - Importação do projeto com git clone
```
$ git clone https://github.com/lucioweb/python_learning_project.git
```

3 - Alternando para a pasta do projeto clonado
```
$ cd python_learning_project
```

4 - Abrindo a pasta do projeto com o VSCode
```
$ code .
```

5 - Criando o venv na pasta do projeto ✔️
```
$ python3 -m venv .venv
```

6 - Ativando o venv (Conforme https://flask.palletsprojects.com/en/2.3.x/installation/) 
Antes de trabalhar em seu projeto, ative o ambiente correspondente:
```
$ . .venv/bin/activate
```

7 - Dentro do ambiente ativado, use o seguinte comando para instalar o Flask:
```
$ pip install Flask
```

8 - Criando o arquivo de manifesto `requirements.txt`.
Em vez de instalar pacotes individualmente, pip permite que você declare todas as dependências em um Arquivo de Requisitos. 
Por exemplo, você pode criar um arquivo `requirements.txt` na raiz do projeto, contendo todas as bibliotecas que deseja instalar:
```
$ python3 -m pip install -r requirements.txt
```

9 - Com a lib do Flask instalada no projeto, o comando será: `$ flask --app flaskr run`
```
$ flask --app flaskr run --debugger (Faz o debug e o reload do código)
```

## BANCO DE DADOS
1 - Inicializando o Banco de dados sqlite: `$ flask --app flaskr run`. 
Após isso será criado um arquivo chamdo `flaskr.sqlite` na *instance* do projeto.  
```
$ flask --app flaskr init-db
```

## OUTROS COMANDOS ÚTEIS
1 - Verificando o caminho de instalaçõ do Python
```
$ sudo whereis python3
python3: /usr/bin/python3 /usr/lib/python3 /etc/python3 /usr/share/python3 /usr/share/man/man1/python3.1.gz
```

2 - Instalando o gerenciador de pacotes do Python
```
$ sudo apt-get install python-pip
```

3 - Verificando a versão do pip instalada
```
$ pip --version
```

4 - Criando o diretório de trabalho 
```
$ luciolemos@dev:~$ mkdir my_python_projects && cd $_
```

5 - CRIANDO A PASTA DO PROJETO
```
$ luciolemos@dev:~/my_python_projects$ mkdir python_project_1 && cd $_
```

6 - INSTALANDO O VENV
Use um ambiente virtual para gerenciar as dependências do seu projeto, tanto no desenvolvimento quanto na produção.
Qual problema um ambiente virtual resolve? Quanto mais projetos Python você tiver, maior a probabilidade de precisar trabalhar com diferentes versões de bibliotecas Python ou até mesmo o próprio Python. Versões mais recentes de bibliotecas para um projeto podem interromper a compatibilidade em outro projeto. Ambientes virtuais são grupos independentes de bibliotecas Python, uma para cada projeto. Os pacotes instalados para um projeto não afetarão outros projetos ou pacotes do sistema operacional.
```
$ sudo apt install python3.10-venv
```

#### CONSOLE EM MODO INTERATIVO
Quando os comandos são lidos a partir do console, diz-se que o interpretador está em modo interativo. Nesse modo ele solicita um próximo comando através do prompt primário, tipicamente três sinais de maior (>>>); para linhas de continuação do comando atual, o prompt secundário padrão é formado por três pontos (...). O interpretador exibe uma mensagem de boas vindas, informando seu número de versão e um aviso de copyright antes de exibir o primeiro prompt:
```
$ python
Python 3.10.6 (main, May 29 2023, 11:10:38) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
### Qual significado de GCC?
O GNU Compiler Collection (chamado usualmente por GCC) é um conjunto de compiladores de linguagens de programação produzido pelo projecto GNU para construir um sistema operativo semelhante ao Unix livre.


### Executando com o comando `$ python3 app.py`
```
$ python3 app.py
```

### Com a lib do Flask instalada no projeto, o comando será: `$ flask --app flaskr run`
```
$ flask --app flaskr run --debugger (Faz o debug e o reload do código)
```


Tutorial do projeto seguindo as recomendações do Flask em https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/
