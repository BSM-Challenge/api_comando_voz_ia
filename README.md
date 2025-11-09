# 🧠 API de Navegação por Voz – Projeto HC

Esta API foi desenvolvida como parte do projeto **Centro de Treinamento do IMREA-HCFMUSP (Challenge FIAP 2025)**.  
Seu objetivo é permitir **navegação por voz acessível**, auxiliando pacientes e usuários com dificuldades cognitivas ou motoras a utilizarem o portal HC de forma simples e intuitiva.

---

## 🚀 Funcionalidade

A API utiliza **Machine Learning** para identificar **intenções de comando de voz** e direcionar o usuário para a rota correspondente do sistema.  

### Exemplo de funcionamento

| Comando de voz | Intenção detectada | Ação executada |
|----------------|--------------------|----------------|
| "abrir receitas" | `abrir_receitas` | `/hc/receitas` |
| "quero ver meus exames" | `abrir_resultados` | `/hc/resultados` |
| "preciso de ajuda" | `abrir_ajuda` | `/hc/ajuda` |
| "voltar para o início" | `voltar` | `/hc` |

---

## 🧠 Como foi criada

1. **Coleta de dados:** Criado um dataset (`comandos.csv`) com frases de voz comuns e suas respectivas intenções e ações.  
2. **Treinamento do modelo:** Utilizado o **TfidfVectorizer** + **MultinomialNB** (Naive Bayes) para classificar os comandos.  
3. **Implementação da API:** Criada com **Flask**, recebe um comando em JSON e retorna a intenção e a ação correspondente.  
4. **Integração:** A API é utilizada dentro do **portal web React (HC)** na página de **Mais Recursos**, onde a navegação por voz é ativada via Web Speech API e faz requisições à API.

---

## 🧪 Como testar a API

###  1. Clonar o repositório
```bash
git clone https://github.com/BSM-Challenge/api_comando_voz_ia.git
cd api_comando_voz_ia
```
###  2. Criar e ativar o ambiente virtual
Windows
```bash
python -m venv venv
venv\Scripts\activate
```
macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
###  3. Instalar as dependências
```bash
pip install -r requirements.txt
```
###  4. Executar a API localmente
```bash
python app.py
```
A API ficará disponível em:
```bash
http://localhost:5000
```
###  5. Testar no Insomnia ou Postman
Método: POST

URL: http://localhost:5000/voz

Body (JSON):
```bash
{
  "comando": "abrir receitas"
}
```
Resposta esperada:
```bash
{
  "comando": "abrir receitas",
  "intencao": "abrir_receitas",
  "acao": "/hc/receitas"
}
```

## 🌐 Onde está sendo utilizada

Esta API está ativa e hospedada no Render, e pode ser acessada publicamente pelos links abaixo:

🌍 Página inicial da API: https://api-comando-voz-ia.onrender.com

🔗 Endpoint principal (rota /voz): https://api-comando-voz-ia.onrender.com/voz

Ela está integrada ao Portal HC (Centro de Treinamento) — um sistema React desenvolvido pela equipe BSM-Challenge no Challenge FIAP 2025.
A API é utilizada na funcionalidade de Navegação por Voz, permitindo que o usuário controle o portal apenas utilizando comandos falados simples.


## 🛠 Tecnologias Utilizadas

Python 3.10+

Flask – criação da API REST

scikit-learn – modelo de classificação de intenções

pandas – manipulação de dados

Render – hospedagem da API

React + Web Speech API – integração de reconhecimento de voz no frontend
