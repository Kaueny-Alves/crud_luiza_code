# Projeto Marketplace de Viagens

> Projeto final apresentado no curso de Google Cloud Plataform na terceira edição do Luiza Code. Uma parceria da Gama Academy e Magazine Luiza.


## 📌 Objetivo do projeto:

> Criar um marketplace de empresas que vendem pacote de viagens.

<img src="figs\logo.png" alt="logo" width="2000"/>




## 📚 O que fizemos:

> Projeto __CRUD__  (Create, Read, Update and Delete) para empresas de viagens.

## 🛠️ Como fizemos ?
> Front-end

* HTML
* CSS

> Back-end

* Python
* Django
* SQLite

## ⌛ Passo a passo para rodar o nosso projeto

🔧 Pré-requisitos:

* [Docker](https://docs.docker.com/get-docker/)

* [Kubernetes](https://kubernetes.io/releases/download/)

* [Minikube](https://minikube.sigs.k8s.io/docs/start/)

> Para acessar a aplicação, rode o comando:

    python3 manage.py runserver

> Caso não funcione, tente o comando:

    python manage.py runserver

> Vai aparecer o link: http://127.0.0.1:8000/, que é onde a aplicação está rodando. Segure a tecla Ctrl apertada e clique com o mouse em cima do link para abrir no navegador.

> Também é possível acessar diretamente do navegador, inserindo: localhost:8000


> Para obter acesso à imagem, siga os passos abaixo:

> Com o [Docker](https://docs.docker.com/get-docker/) instalado e rodando em sua máquina forneça o seguinte comando:

    docker pull alinebellozo/python-crud:v4


> Em seguida, rode a aplicação em sua máquina com o comando:

    docker run -d -p 8000:8000 -it alinebellozo/python-crud:v4

> Na mesma pasta do projeto, inicie o <a href=“https://kubernetes.io/releases/download/“>Kubernetes</a> em sua máquina:

    minikube start

> Ao finalizar a configuração, leia o arquivo _deployment.yaml_ por meio do comando:

    kubectl apply -f deployment.yaml

> Então, rode o seguinte comando para abrir o dashboard:

    minikube dashboard

> No Workload Status, você verá círculos verde, o que significa que o deploy no Kubernetes foi feito!
> Para visualizar mais detalhes sobre o deploy, role a tela para baixo e clique no nome do projeto.


## 💻 Navegando pelo site

> Cadastro de empresa

<img src="figs\create_empresa.PNG" alt="create" width="2000"/>

> Salvar empresa

<img src="figs\save_empresa.PNG" alt="save" width="2000"/>

> Ver, editar, atualizar e deletar e filtrar empresa

<img src="figs\changes_empresa.PNG" alt="changes" width="2000"/>

> Cadastrar pacotes de viagens associado a empresa 

<img src="figs\create_pacotes.PNG" alt="create pacotes" width="2000"/>


## 👩‍💻 Desenvolvido por


> <a href=https://github.com/alinebellozo>Aline Bellozo</a>,  <a href=https://github.com/Kaueny-Alves>Kaueny Alves</a>, <a href=https://github.com/MClaudia-Correia>Maria Claudia Correia</a> e <a href=https://github.com/ShayaneGonzalez>Shayane Gonzalez</a>
<img src="figs\devs.PNG" alt="create pacotes" width="2000"/>





