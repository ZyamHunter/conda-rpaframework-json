[![Standard](https://github.com/ZyamHunter/conda-rpaframework-json/actions/workflows/standard.yaml/badge.svg)](https://github.com/ZyamHunter/conda-rpaframework-json/actions/workflows/standard.yaml)

# conda-rpaframework-json
Repositório de testes dedicados ao uso da biblioteca rpaframework com json utilizando conda no gerenciamento do projeto


# robot template
> Repositório de testes dedicados ao uso da bibliotecas rpaframework com json 

# Configuração do Ambiente

## 1. Instalar Python 3.10

Certifique-se de ter o Python 3.10 instalado em seu sistema. Você pode baixá-lo no [site oficial do Python](https://www.python.org/).

## 2. Instalar Ambiente Virtual

Instale a ferramenta `virtualenv` para criar ambientes virtuais de aprendizado:

- pip install virtualenv

## 3. Criar um ambiente virtual:
- python -m venv project-venv

## 4. Se você estiver usando o PowerShell e encontrar problemas para executar scripts, talvez precise alterar a política de execução temporariamente para permitir a execução de scripts:
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## 5. Ativar o ambiente virtual:
- .\project-venv\Scripts\activate

## 6. Remover cache do pip
- pip cache remove *

## 7. Rodar os testes
- robot -d logs ./src

## 8. Desativar ambiente virtual
- deactivate

## 9. Instalar Node.js:
- https://nodejs.org/en/download
 > Ao instalar, provavelmente vários pacotes adicionais serão instalados, como chocolatery, etc.

## 10. Instalar dependências do Python
> Primeiro ative o ambiente virtual para evitar erros de versão com outras bibliotecas instaladas
- pip install -r requirements.txt

<br/>

### ---- Diferenciais no projeto ----
<br/>

- Page Object
- RPA Framework
- Conda
- NPM
- Massa de Dados
- Geração de Report
- Report dos testes no Slack

<br/>

**Executar teste regressivo**
> npm run json
