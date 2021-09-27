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

* <a href=“https://docs.docker.com/get-docker/“>Docker</a>
* <a href=“https://kubernetes.io/releases/download/“>Kubernetes</a> 
* <a href=“https://minikube.sigs.k8s.io/docs/start/“>Minikube</a>


> Com o <a href=“https://docs.docker.com/get-docker/“>Docker</a> instalado e rodando em sua máquina forneça o seguinte comando:

    docker pull https://hub.docker.com/repository/docker/alinebellozo/python-crud


> Em seguida, rode a aplicação em sua máquina:

    docker run -d -p 8000:8000 -it alinebellozo/python-crud

> Na pasta do projeto, inicie o <a href=“https://kubernetes.io/releases/download/“>Kubernetes</a> em sua máquina:

    minikube start

> Leia o arquivo _deployment.yaml_:

    kubectl apply -f deployment.yaml

> Adicione a imagem no <a href=“https://minikube.sigs.k8s.io/docs/start/“>Minikube</a>:

    docker save alinebellozo/python-crud | (eval $(minikube docker-env) && docker load)

> Abra o dashboard:

    minikube dashboard

> Selecione a opção _kube-system_


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


> <a href=“https://github.com/alinebellozo“>Aline Bellozo</a>,  <a href=“https://github.com/Kaueny-Alves“>Kaueny Alves</a>, <a href=“https://github.com/MClaudia-Correia“>Maria Claudia Correia</a> e <a href=“https://github.com/ShayaneGonzalez“>Shayane Gonzalez</a>
<img src="figs\devs.PNG" alt="create pacotes" width="2000"/>





