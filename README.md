# 🌍 Previsão de Níveis de Ozônio com Prophet

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Prophet](https://img.shields.io/badge/Prophet-v1.1-green?style=flat-square&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiIGZpbGw9IiMwMDc0YjciLz48L3N2Zz4=)](https://facebook.github.io/prophet/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

Sistema inteligente para **previsão de séries temporais** de concentração de ozônio (O₃) na atmosfera, utilizando a biblioteca **Prophet** do Facebook. Combina análise estatística avançada com uma interface web interativa.

## 📋 Sumário

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Dados](#dados)
- [Modelo & Resultados](#modelo--resultados)
- [Exemplos de Uso](#exemplos-de-uso)
- [Contribuições](#contribuições)
- [Licença](#licença)

## 🎯 Visão Geral

Este projeto implementa um **modelo de previsão de séries temporais** treinado com dados históricos de concentração de ozônio de 2020 a 2023. O objetivo é prever os níveis de O₃ nos próximos dias/meses com precisão, auxiliando em estudos de qualidade do ar e poluição atmosférica.

### Motivação

A concentração de ozônio na atmosfera é um indicador importante de qualidade do ar. Previsões precisas permitem:
- 🏥 Alertas para populações vulneráveis
- 🌱 Planejamento de políticas ambientais
- 📊 Análise de tendências de poluição
- 🔬 Apoio a pesquisas científicas

## ✨ Características

- ✅ **Modelo Prophet pré-treinado**: Carregamento rápido para inferência
- ✅ **Interface Web Interativa**: Dashboard Streamlit intuitivo
- ✅ **Previsões Dinâmicas**: Gere previsões de 1 a 365 dias
- ✅ **Visualizações Interativas**: Gráficos Plotly com componentes sazonais
- ✅ **Intervalos de Confiança**: Exibe limites superior e inferior das previsões
- ✅ **Análise Exploratória Completa**: Notebook Jupyter com EDA e validação
- ✅ **Decomposição Sazonal**: Análise de tendências, sazonalidade e componentes residuais

## 🛠️ Tecnologias

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| [Prophet](https://facebook.github.io/prophet/) | 1.1+ | Modelo de série temporal |
| [Streamlit](https://streamlit.io/) | 1.0+ | Framework web interativo |
| [Pandas](https://pandas.pydata.org/) | 1.3+ | Processamento de dados |
| [Plotly](https://plotly.com/python/) | 5.0+ | Visualizações interativas |
| [Scikit-learn](https://scikit-learn.org/) | 1.0+ | Métricas e avaliação |
| [Statsmodels](https://www.statsmodels.org/) | 0.13+ | Análise estatística de séries temporais |
| [NumPy](https://numpy.org/) | 1.20+ | Computação numérica |
| [Matplotlib](https://matplotlib.org/) | 3.5+ | Visualizações estáticas |
| [Seaborn](https://seaborn.pydata.org/) | 0.11+ | Visualizações estatísticas |

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### Passos

1. **Clone o repositório** (se estiver no GitHub):

```bash
git clone https://github.com/Johnny-DF26/Regress-o-prevendo-s-ries-temporais-com-Prophet.git
cd "Regressão prevendo séries temporais com Prophet"
```

2. **Crie um ambiente virtual** (recomendado):

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### Executar a Aplicação Web

Inicie o dashboard interativo com Streamlit:

```bash
streamlit run app.py
```

A aplicação abrirá em `http://localhost:8501`. Você poderá:

1. **Inserir o número de dias** desejados para previsão (1-365)
2. **Clicar em "Gerar Previsão"** para executar o modelo
3. **Visualizar o gráfico interativo** com as previsões
4. **Consultar a tabela de resultados** com valores diários

### Explorar o Notebook Jupyter

Para análise completa e desenvolvimento:

```bash
jupyter notebook notebooks/Regressão_prevendo_séries_temporais_com_Prophet.ipynb
```

O notebook contém:
- Importação e limpeza de dados
- Análise exploratória (EDA)
- Testes de estacionariedade (ADF, KPSS)
- Decomposição sazonal
- Treinamento do modelo Prophet
- Validação e métricas de desempenho
- Visualizações e insights

## 📁 Estrutura do Projeto

```
├── app.py                                    # Aplicação Streamlit principal
├── requirements.txt                          # Dependências do projeto
├── README.md                                 # Este arquivo
├── data/
│   └── processad/
│       └── previsao_ozonio.csv              # Dados processados para previsão
├── models/
│   └── saved/
│       └── modelo_prophet_final2.json       # Modelo Prophet serializado
├── notebooks/
│   └── Regressão_prevendo_séries_temporais_com_Prophet.ipynb  # Análise completa
└── src/
    └── [Módulos auxiliares]
```

### Descrição dos Diretórios

- **`app.py`**: Aplicação principal com interface Streamlit
- **`requirements.txt`**: Lista de todas as dependências Python necessárias
- **`data/processad/`**: Dados processados prontos para uso
- **`models/saved/`**: Modelo treinado em formato JSON (pronto para inferência)
- **`notebooks/`**: Jupyter notebooks com análise exploratória e treinamento
- **`src/`**: Módulos Python auxiliares (atualmente vazio)

## 📊 Dados

### Fonte de Dados

Os dados foram extraídos de um repositório público da **Alura** contendo medições de poluentes atmosféricos.

**URL Original**: `https://raw.githubusercontent.com/alura-cursos/series_temporais_prophet/main/Dados/poluentes.csv`

### Características do Dataset

| Atributo | Descrição |
|----------|-----------|
| **Data** | Data da medição (período: 2020-2023) |
| **O3** | Concentração de ozônio em µg/m³ |
| Outros poluentes | SO₂, NO₂, PM₁₀, etc. |
| **Unidade** | Microgramas por metro cúbico (µg/m³) |

### Estatísticas dos Dados

- **Período de cobertura**: 2020 a 2023
- **Frequência**: Diária
- **Variável alvo**: O3 (concentração de ozônio)
- **Total de observações**: ~1.400+ registros

## 📈 Modelo & Resultados

### Configuração do Modelo Prophet

O modelo Prophet foi treinado com as seguintes configurações:

```python
from prophet import Prophet

model = Prophet(
    interval_width=0.95,           # 95% de intervalo de confiança
    yearly_seasonality=True,       # Sazonalidade anual
    weekly_seasonality=True,       # Sazonalidade semanal
    daily_seasonality=False        # Sem sazonalidade diária
)
```

### Métricas de Desempenho

| Métrica | Valor |
|---------|-------|
| **RMSE (Erro Quadrático Médio)** | **17.43 µg/m³** |
| **Data de Treinamento** | Até 05/05/2023 |
| **Período de Teste** | Últimos 30 dias de dados |
| **Intervalo de Confiança** | 95% |

**Interpretação**: O modelo erra, em média, ~17.43 µg/m³ nas previsões, representando uma precisão adequada para previsões de qualidade do ar.

### Componentes do Modelo

O Prophet decompõe a série temporal em:

1. **Tendência (Trend)**: Padrão de longo prazo na concentração de O₃
2. **Sazonalidade Anual**: Variações que se repetem anualmente
3. **Sazonalidade Semanal**: Padrões que se repetem semanalmente
4. **Componentes Residuais**: Variações não explicadas

## 💡 Exemplos de Uso

### Exemplo 1: Previsão para 30 dias

```python
from prophet.serialize import model_from_json
import json

# Carregar modelo
with open('models/saved/modelo_prophet_final2.json', 'r') as f:
    model = model_from_json(f.read())

# Fazer previsão
future = model.make_future_dataframe(periods=30, freq='D')
forecast = model.predict(future)

# Ver últimas 30 previsões
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30))
```

### Exemplo 2: Visualizar Componentes

```python
# Plotar componentes
fig = model.plot_components(forecast)
fig.show()
```

### Exemplo 3: Previsão para 90 dias (via Streamlit)

1. Abra `http://localhost:8501`
2. Insira **90** no campo de dias
3. Clique em **"Gerar Previsão"**
4. Visualize o gráfico e tabela interativos

## 🔍 Análise Exploratória (Destacado do Notebook)

O notebook inclui análises aprofundadas como:

- **Gráficos de série temporal** (2020-2023)
- **Decomposição sazonal** com Statsmodels
- **Teste de Augmented Dickey-Fuller (ADF)** para estacionariedade
- **Teste KPSS** para validação
- **Gráficos ACF/PACF** para identificação de padrões
- **Heatmaps de correlação** entre poluentes
- **Análise mensal e sazonal** de O₃

## 🤝 Contribuições

Contribuições são bem-vindas! Se deseja melhorar este projeto:

1. **Faça um fork** do repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit suas mudanças** (`git commit -m 'Add AmazingFeature'`)
4. **Push para a branch** (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

### Possíveis Melhorias

- [ ] Adicionar suporte a outras variáveis (NO₂, PM₁₀, SO₂)
- [ ] Implementar retrainamento automático do modelo
- [ ] Criar API REST para previsões programáticas
- [ ] Adicionar análise de anomalias
- [ ] Melhorar ajuste de hiperparâmetros
- [ ] Comparar com outros modelos (ARIMA, LSTM, etc.)

## 📝 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Johnny DF26**

- GitHub: [@Johnny-DF26](https://github.com/Johnny-DF26)
- Repositório: [Regressão prevendo séries temporais com Prophet](https://github.com/Johnny-DF26/Regress-o-prevendo-s-ries-temporais-com-Prophet)

## 📚 Referências e Recursos

- [Documentação oficial do Prophet](https://facebook.github.io/prophet/)
- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Guia de Séries Temporais - Alura](https://github.com/alura-cursos/series_temporais_prophet)
- [Statsmodels - Análise de Séries Temporais](https://www.statsmodels.org/stable/tsa.html)

## 📞 Suporte

Se encontrar problemas ou tiver dúvidas:

1. Verifique o [Issues](https://github.com/Johnny-DF26/Regress-o-prevendo-s-ries-temporais-com-Prophet/issues) do repositório
2. Consulte a documentação do Prophet
3. Abra uma nova issue descrevendo o problema

---

<div align="center">

**⭐ Se este projeto foi útil, considere deixar uma estrela!**

Desenvolvido com ❤️ usando Prophet e Streamlit

</div>
