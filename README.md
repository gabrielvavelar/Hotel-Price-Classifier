# Hotel Price Classifier

<p align="center">
 <a href="#-descrição">Descrição</a>  •
 <a href="#-funcionalidades">Funcionalidades</a>  • 
 <a href="#-acesso-a-aplicação">Acesso a aplicação</a>  • 
 <a href="#-desenvolvimento">Desenvolvimento</a>  • 
 <a href="#-execução-local">Execução</a>  • 
 <a href="#-arquitetura-aws">Arquitetura AWS</a>  •
 <a href="#-autor">Autor</a> 
</p>

## 📜 Descrição

Projeto tem como objetivo classificar reservas de hotel com base na faixa de preço por quarto utilizando AWS SageMaker para treinamento de modelo, AWS RDS para armazenamento de dados, e FastAPI para exposição de uma API de predição. O projeto é containerizado utilizando Docker.

## ✅ Funcionalidades

Este projeto possui diversas funcionalidades importantes, que permitem a classificação de reservas de hotel com base em faixas de preço por quarto, utilizando um modelo de machine learning treinado no AWS SageMaker. Aqui estão as principais funcionalidades:

**1. Carregamento e Preparação dos Dados**

- Notebooks Jupyter: Utilizamos notebooks para carregar, explorar e preparar os dados. Isso inclui limpeza dos dados, criação de novas features e armazenamento dos dados processados no AWS S3 e AWS RDS.
- Interação com RDS: Conexão ao banco de dados relacional (RDS) da AWS para executar consultas SQL e manipular os dados diretamente.

**2. Treinamento do Modelo**

- AWS SageMaker: Utilizamos o AWS SageMaker para treinar um modelo de machine learning. O modelo é treinado utilizando dados armazenados no S3 e a configuração do treinamento é feita nos notebooks.
- Modelo Random Forest: Escolha do algoritmo Random Forest devido à sua robustez e alta performance em tarefas de classificação.

**3. Desenvolvimento da API**

**FastAPI**
- Desenvolvemos uma API utilizando o framework FastAPI, que oferece uma interface RESTful para realizar predições. A API é configurada para carregar o modelo treinado a partir do S3.

**4. Containerização**

- Docker: Utilização do Docker para containerizar a aplicação, garantindo que o ambiente de execução seja consistente em diferentes máquinas.

**5. Deploy na AWS**
- EC2: A aplicação pode ser implantada na AWS usando Amazon ECS, EKS ou instâncias EC2. O uso de containers Docker facilita o deploy e a escalabilidade da aplicação.
- AWS S3: O modelo treinado e os dados são armazenados no Amazon S3, permitindo fácil acesso e gerenciamento.

**Endpoint**
- /api/v1/predict: Endpoint POST que recebe um JSON com os dados da reserva e retorna a classificação (faixa de preço).
- /: Endpoint GET que retorna uma mensagem de boas-vindas.


## 🧑‍💻 Acesso a Aplicação

**1. Para acesso a aplicação, copie e cole no navegador:**
- Página inicial:
```
http://34.225.156.10
```
- Página para fazer predições:
```
http://34.225.156.10/docs
```

## 🚀 Desenvolvimento
**📂 Estrutura de pastas**

 ```
├── src
│   ├── Api
│   │   ├── Controllers                         
│   │   │   ├── home_controller.py                # Controlador para a rota principal da API, respondendo com uma mensagem de boas-vindas.
│   │   │   └── prediction_controller.py          # Controlador para a rota de predição, gerenciando a lógica de receber dados de entrada e retornar a predição.
│   │   ├── Models
│   │   │   └── prediction_model.py               # Modelo de dados utilizado na API, definindo a estrutura dos dados de entrada para a predição.
│   │   ├── Service                                
│   │   │   └── prediction_service                # Serviço para carregar o modelo treinado do S3 e realizar predições.
│   │   ├── main.py                               # Ponto de entrada da aplicação FastAPI
│   │   ├── requeriments.txt                      # Lista de dependências do Python
│   │   ├── .env                                  # Exemplo de como colocar variáveis que serão usadas para fazer conexão com a AWS
│   │   ├── docker-compose.yml                    # Configuração do Docker Compose para orquestrar a aplicação.
│   │   └── Dockerfile                            # Configuração do Docker
│   ├── data_processing
│   │   ├── ml_training                             
│   │   │   └── .env                              # Exemplo de como colocar variáveis que serão usadas para fazer conexão com a AWS
│   │   │   └── train_model.ipynb                 # Notebooks Jupyter para desenvolvimento e treinamento dos dados
│   │   │   └── requeriments.txt                  # Lista de dependências do Python.
│   │   ├── database_interaction
│   │   │   └── .env                              # Exemplo de como colocar variáveis que serão usadas para fazer conexão com a AWS
│   │   │   └── data-processing_rds-upload.ipynb  # Notebook para interação com RDS, incluindo conexão ao banco de dados, busca de arquivo e preparação inicial dos dados
│   │   │   └── requeriments.txt                  # Lista de dependências do Python.
└───────────────────────────────────────────────────────────────────────────────────────────────────────────


 ```
**⚙️ Tecnologias Utilizadas**
- Python: Linguagem de programação principal.
- FastAPI: Framework para desenvolvimento da API.
- AWS SageMaker: Serviço da AWS para treinamento e deploy de modelos de machine learning.
- AWS S3: Armazenamento de dados e modelos.
- AWS RDS: Banco de dados relacional para armazenamento dos dados.
- Amazon EC2: Instâncias de computação na nuvem.
- Amazon ECR: Repositório de imagens Docker.
- Docker: Ferramenta de containerização.
- Docker Compose: Orquestração de containers.


## 💻 Execução local

**Pré-requisitos** : 
- `Conta na AWS com permissões para SageMaker, S3, EC2, ECR e RDS`
- `Docker`
- `Python 3.9 ou superior`
- `Jupyter Notebook`

- **Clone o repositório:**
```
git clone https://github.com/gabrielvavelar/Hotel-Price-Classifier.git
 ```

- **Não esqueça de preencher os arquivos .env com o que é solicitado.**

- **Passos para executar o treinamento:**

- **Entre com suas credenciais utilizando o AWS Configure.**

- **Entre na pasta data_processing:**

```
cd data_processing  
```
- **Crie o ambiente virtual para o gerenciamento de pacotes e ative, exemplo utilizando conda:**

```
conda create -p env python=3.10
conda activate env/\
```
-  **Entre na pasta database_interaction:**

```
cd database_interaction
```
- **Instale todos os pacotes listados para uso das bibliotecas:**

```
pip install -r requirements.txt 
```
- **Execute o notebook data-processing_rds-upload.ipynb**

-  **Após a execução do notebook, vá para a pasta ml_training e Instale todos os pacotes listados para uso das bibliotecas:**
```
ml_training
pip install -r requirements.txt 
```
- **Execute o train_model.ipynb**

**Passos para executar a API**
- **Entre na pasta api:**

```
cd api  
```
- **Crie o ambiente virtual para o gerenciamento de pacotes e ative, exemplo utilizando conda:**

```
conda create -p env python=3.10
conda activate env/\
```
- **Instale todos os pacotes listados para uso das bibliotecas:**

```
pip install -r requirements.txt 
```
- **Excute a api:**

```
python main.py 
```
- **Ou caso prefira executar pelo docker:**
 ```
docker-compose up
 ```

- **Acesse a aplicação localmente:**
Abra o navegador e vá para http://localhost:8000/docs


## 🌐 Arquitetura AWS
A arquitetura AWS deste projeto integra vários serviços da AWS para criar uma solução de machine learning e predição. A utilização de SageMaker, S3, RDS, FastAPI, Docker e EC2 permite que a aplicação seja escalável, eficiente e fácil de gerenciar. Cada componente foi escolhido para otimizar o desempenho e a escalabilidade, garantindo que o sistema possa lidar com grandes volumes de dados e fornecer predições em tempo real.

<img src="assets/Architecture.jpg" height="400" >

## 👤 Autor
- [Gabriel Venancio de Avelar](https://github.com/gabrielvavelar)

