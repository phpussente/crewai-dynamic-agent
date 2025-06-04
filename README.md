# Agentes Busca Dinâmica

Este repositório contém agentes inteligentes para classificação e análise de planilhas relacionadas a vendas, utilizando a biblioteca [CrewAI](https://github.com/joaomdmoura/crewAI) e ferramentas auxiliares.

## Requisitos

- Python 3.12 ou superior
- [pip](https://pip.pypa.io/en/stable/)
- (Opcional) [virtualenv](https://virtualenv.pypa.io/en/latest/) para ambientes isolados

## Instalação

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/seu-usuario/agentes_busca_dinamica.git
   cd agentes_busca_dinamica
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```sh
   python -m venv .venv
   # No Windows:
   .venv\Scripts\activate
   # No Linux/Mac:
   source .venv/bin/activate
   ```

3. **Instale as dependências:**

   ```sh
   pip install -r requirements.txt
   ```

   > **Nota:** Se o arquivo `requirements.txt` não existir, gere-o a partir do `pyproject.toml`:
   >
   > ```sh
   > pip install pip-tools
   > pip-compile pyproject.toml
   > pip install -r requirements.txt
   > ```

## Configuração

1. **Variáveis de ambiente**

   Copie o arquivo `.env.example` para `.env` e preencha as variáveis necessárias, como chaves de API para LLMs ou serviços externos.

   ```sh
   cp .env.example .env
   # Edite o arquivo .env conforme necessário
   ```

2. **Arquivos de dados**

   Certifique-se de que o arquivo `vendas_ficticias_brasil.csv` está presente na raiz do projeto. Ele é utilizado para consultas e relatórios de vendas.

## Uso

### Classificação de Texto

Você pode utilizar a classe [`FacadeCrew`](crew_facade.py) para classificar textos em "vendas" ou "trivialidades".

Exemplo de uso interativo:

```python
from crew_facade import FacadeCrew

facade = FacadeCrew()
texto = "Quantas vendas foram realizadas no último mês?"
resultado = facade.kickoff(texto)
print(resultado)
```

### Geração de Relatórios de Vendas

Utilize a classe [`SalesReportCrew`](crew_sales_report.py) para gerar relatórios baseados no CSV de vendas.

Exemplo de uso:

```python
from crew_sales_report import SalesReportCrew

report_crew = SalesReportCrew()
query = "Qual foi o total de vendas em março?"
resultado = report_crew.kickoff(query)
print(resultado)
```

### Executando Testes

Se houver testes implementados (ex: [`app_test.py`](app_test.py)), execute:

```sh
python app_test.py
```

## Estrutura do Projeto

- [`crew_facade.py`](crew_facade.py): Classificação de textos.
- [`crew_sales_report.py`](crew_sales_report.py): Relatórios de vendas a partir de CSV.
- [`vendas_ficticias_brasil.csv`](vendas_ficticias_brasil.csv): Base de dados fictícia de vendas.
- [`app.py`](app.py): Ponto de entrada principal (se aplicável).
- [`generate.py`](generate.py), [`send_message.py`](send_message.py), [`transcript.py`](transcript.py): Utilitários auxiliares.

## Observações

- O projeto utiliza modelos LLM (ex: `gpt-4o-mini`). Certifique-se de ter as credenciais necessárias configuradas no `.env`.
- Para funcionalidades de áudio, consulte [`fluxo_audio.py`](fluxo_audio.py) e [`evolution-api/`](evolution-api/).

## Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

---

**Dúvidas?** Consulte os comentários nos arquivos ou abra uma issue.