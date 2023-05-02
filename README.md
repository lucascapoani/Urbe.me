# 💻 Urbe.me - Case Técnico 2023

<h2>📝 Desafio </h2>

O desafio proposto consiste em desenvolver uma aplicação web usando o framework Django do Python, seguindo as seguintes premissas:
- Realizar ao menos uma operação de consulta a uma base de dados de sua escolha, seja externa, por meio de API, ou de uma instância provisionada por você mesmo;
- Apresentar ao menos 2 endpoints diferentes (2 páginas/urls);
- Publicar o código em um repositório no GitHub;
- Documentar os processos de tomada de decisão e do desenvolvimento como um todo;
- No arquivo read.me do repositório, documentar como rodar/fazer o setup do projeto localmente (para podermos testar sem subirem num serviço externo). 
EXTRA: se conseguirem fazer algo interessante com os dados disponibilizados no seguinte endpoint, ganha uma ceva: https://urbe.me/administracao/api/lista-projetos/
<hr>

<h2> 📁 Instruções </h2>

<p>Para testar a aplicação desenvolvida, serão necessários alguns passos.</p> 

- Abra um terminal cmd e clone o repositório na sua máquina, digitando:
```
$ git clone https://github.com/lucascapoani/Urbe.me.git
```

- Instalar a biblioteca Requests do Python, necessária para fazer a requisição para a API:
```
pip install requests
```

- Instalar o framework para utilização do mapa:
```
pip install folium
```

- Para rodar a aplicação, basta digitar o seguinte comando:
```
python manage.py runserver
```
- Ou então ir no arquivo manage.py, copiar o "caminho" clicando com o botão direito e indo em "Copy Path" e digitar no cmd o caminho + runserver

<p>- Após rodar a aplicação, abrir o navegador e digitar o seguinte endereço:</p>
http://127.0.0.1:8000/home - Leva para a página principal

![image](https://user-images.githubusercontent.com/97242525/235673931-36698d39-3790-4cbf-810e-c43a53933c35.png)
<hr>

<p>- Clicando no botão "Projetos" ou digitando o endereço http://127.0.0.1:8000/projects/ , você terá acesso a lista de projetos da API fornecida.</p>

![image](https://user-images.githubusercontent.com/97242525/235674895-63ca6b81-d965-44db-8010-d5aee407b859.png)
<hr>

<p>- Clicando no botão "Localização" ou digitando o endereço http://127.0.0.1:8000/location/ , a aplicação exibirá um mapa com as localizações dos projetos. Clicando nos "pins" pode-se verificar qual o projeto está naquele local. </p>

![image](https://user-images.githubusercontent.com/97242525/235677030-73469062-f862-4046-9725-36bfa64095eb.png)

<p> PS: Para localizações que não possuiam latitude e longitude na API, foram considerados latitude e longitude 0. </p>
<hr>

<h2>✔️ Dúvidas</h2>

<p>Para esclarecimentos e quaisquer dúvidas, não hesite em me contatar aqui pelo github, pelo Linkedin ou por email.</p>


