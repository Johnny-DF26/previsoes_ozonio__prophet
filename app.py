from prophet.serialize import model_from_json
from prophet.plot import plot_plotly
import streamlit as st
import json

# ==============================================================
# Criando Sessão
# ==============================================================
st.set_page_config(
    page_title="Previsão de Níveis de Ozônio (O3)", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# ==============================================================
# Carregar modelo (executado apenas uma vez)
# ==============================================================
@st.cache_resource
def load_model() -> json:
    with open('models/saved/modelo_prophet_final2.json', 'r') as f:
        return model_from_json(f.read())


# ==============================================================
# Inicializar variáveis da sessão
# ==============================================================
if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "dias" not in st.session_state:
    st.session_state.dias = 30


# ==============================================================
# Carregar modelo
# ==============================================================
modelo_prophet = load_model()


# ==============================================================
# Configuração do layout do Streamlit
# ==============================================================
st.title("Previsão de Níveis de Ozônio (O3) Utilizando Prophet", text_alignment='center')

# Adicionando textos ao layout do Streamlit
st.caption('''Este projeto utiliza a biblioteca Prophet para prever os níveis de ozônio em ug/m3. O modelo
           criado foi treinado com dados até o dia 05/05/2023 e possui um erro de previsão (RMSE - Erro Quadrático Médio) igual a 17.43 nos dados de teste.
           O usuário pode inserir o número de dias para os quais deseja a previsão, e o modelo gerará um gráfico
           interativo contendo as estimativas baseadas em dados históricos de concentração de O3.
           Além disso, uma tabela será exibida com os valores estimados para cada dia.''')

st.subheader('Insira o número de dias para previsão:')

dias = st.number_input('', 
                       min_value=1, 
                       max_value=365, 
                       value=30, 
                       step=1, 
                       key='dias_previsao'
        )


# ==============================================================
# Botão e geração da previsão
# ==============================================================
if st.button("Gerar Previsão"):
    st.session_state.dias = dias

    # Gerar previsão
    with st.spinner("⏳Gerando previsão..."):
        future = modelo_prophet.make_future_dataframe(periods=dias, freq='D')
        prediction = modelo_prophet.predict(future)
        st.session_state.prediction = prediction
        

# ==============================================================
# Exibir resultados
# ==============================================================
if st.session_state.prediction is not None:

    st.divider()
    st.subheader("Gráfico da Previsão")

    # Gerar gráfico interativo com Plotly
    fig = plot_plotly(modelo_prophet, st.session_state.prediction)
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',  # Define o fundo da área do gráfico como branco
        'paper_bgcolor': 'rgba(255, 255, 255, 1)', # Define o fundo externo ao gráfico como branco
        'title': {'text': "Previsão de Ozônio", 'font': {'color': 'black'}},
        'xaxis': {'title': 'Data', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}},
        'yaxis': {'title': 'Nível de Ozônio (O3 μg/m3)', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}}
    })

    st.plotly_chart(fig, use_container_width=True)

    # Gerar tabela de previsão
    previsoes_novas = st.session_state.prediction.tail(st.session_state.dias)[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    previsoes_novas = previsoes_novas.rename(columns={'ds':'Data', 
                                                      'yhat':'Previsão', 
                                                      'yhat_lower':'Limite Inferior', 
                                                      'yhat_upper':'Limite Superior'}).reset_index(drop=True)
    previsoes_novas["Data"] = previsoes_novas["Data"].dt.strftime('%d/%m/%Y')
    previsoes_novas["Previsão"] = previsoes_novas["Previsão"].round(2)
    previsoes_novas["Limite Inferior"] = previsoes_novas["Limite Inferior"].round(2)
    previsoes_novas["Limite Superior"] = previsoes_novas["Limite Superior"].round(2)

    # Visualizando o DataFrame das previsões
    st.subheader("Tabela de Previsão")
    st.dataframe(
        previsoes_novas[["Data", "Previsão"]],
        use_container_width=True
    )

    # ==============================================================
    # Salvando a tabela de previsão em CSV
    # ==============================================================
    st.download_button(
        label="Baixar Previsão em CSV",
        data=previsoes_novas[["Data", "Previsão"]].to_csv(index=False).encode('utf-8'),
        file_name=f'previsao_ozonio_{dias}dias.csv',
        mime='text/csv'
    )
