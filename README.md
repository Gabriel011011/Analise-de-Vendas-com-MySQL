# 📊 Análise de Vendas com MySQL

<br>

## 📌 Sobre o Projeto

Este projeto tem como objetivo realizar uma análise exploratória de dados de vendas utilizando MySQL, com foco em métricas de negócio e extração de insights a partir de consultas SQL.

<br>

Os dados foram previamente tratados em Python e carregados para o banco de dados, simulando um fluxo real de trabalho em análise de dados.

<br>

---

<br>

## 🎯 Objetivo

Demonstrar domínio de SQL aplicado a análise de dados, incluindo:

- Consultas com SELECT
- Agregações com SUM, AVG, COUNT
- Uso de GROUP BY e ORDER BY
- Análise de métricas de negócio (receita, volume, margem, ticket médio)

<br>

---

<br>

## 🛠️ Ferramentas Utilizadas

- **MySQL**
- **MySQL Workbench**
- **Python** (Pandas + SQLAlchemy) — para ingestão e tratamento dos dados

<br>

---

<br>

## ⚙️ Pipeline do Projeto

### 1️⃣ Extração
- Dados provenientes de arquivo CSV

<br>

### 2️⃣ Transformação (Python)
- Limpeza de valores monetários (R$)
- Ajuste de separadores decimais
- Conversão de porcentagens
- Padronização de tipos de dados

<br>

### 3️⃣ Carga
- Inserção no MySQL com `pandas.to_sql()`

<br>

### 4️⃣ Análise (SQL)
- Execução de queries analíticas

<br>

---

<br>

## 🗂️ Estrutura da Tabela

Principais campos utilizados:

- `data` (DATE)
- `mes` (VARCHAR)
- `ano` (INT)
- `produto` (VARCHAR)
- `categoria` (VARCHAR)
- `regiao` (VARCHAR)
- `vendedor` (VARCHAR)
- `quantidade` (INT)
- `receita` (FLOAT)
- `custo` (FLOAT)
- `lucro` (FLOAT)
- `margem` (FLOAT)

<br>

---

<br>

## 📊 Análises Realizadas

### 🔹 Exploração Inicial
- Total de vendas por região
- Receita total por região
- Receita ao longo do tempo (por mês)

<br>

### 🔹 Análise de Produtos
- Produtos com maior receita
- Produtos mais vendidos (volume)

<br>

### 💡 Comparação entre:
- Valor gerado vs quantidade vendida

<br>

### 🔹 Análise de Vendedores
- Receita total por vendedor
- Ticket médio por vendedor

<br>

### 🔹 Análise de Rentabilidade
- Margem média por produto

<br>

---

<br>

## 🧠 Principais Insights

Diferença clara entre produtos que geram maior volume e maior receita
Vendedores apresentam variação significativa no ticket médio
Alguns produtos possuem alta margem, mesmo com menor volume de vendas
A análise de margem permite identificar oportunidades de maior lucratividade
A vendedora Ana se destaca tanto em receita total quanto em ticket médio


🚀 Diferenciais do Projeto

Integração entre Python + MySQL
Simulação de pipeline real de dados (ETL)
Foco em métricas de negócio
Queries organizadas por nível de complexidade
Análise comparativa (volume vs receita vs margem)


🤖 Uso de Inteligência Artificial
A Inteligência Artificial foi utilizada apenas como apoio ao aprendizado, auxiliando em:

revisão de estrutura do projeto
sugestões de melhoria
boas práticas em análise de dados

👉 Todas as queries e lógica analítica foram desenvolvidas manualmente.


<h4>👨‍💻 Autor
Gabriel Lima dos Santos
Estudante de Dados | Foco em Análise de Dados</h4>