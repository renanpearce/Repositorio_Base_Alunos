# criar um ambiente virtual para instatlações dos arquuivos
# 1) instalar o venv com o comando: ptyhon -m venv .ven
# 2) ativar o venv com o comando: .venv\script\activate
# 3) instalar o stremlit com o comando: pip install streamlite
# 4) começar o arquivo app.py

import streamlit as st
import os

# Sidebar
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", width=150)
else:
    st.sidebar.markdown('### 🚲BikeRent🚲')
st.sidebar.title('BikeRent - aluguel de bicicletas')

# lista de bicicletas disponiveis
bicicletas = ['Mountain Bike', 'Road Bike', 'City Bike', 'Eletric Bike']
opcao = st.sidebar.selectbox('Escolha a bike alugada', bicicletas)

# principal
st.title('🚲BikeRent - Aluguel de bicicletas')
st.markdown('Pedale com liberdade, alugue com facilidade!')

# imagens das bicicletas
image_urls = {
    'Mountain Bike': 'https://images.unsplash.com/photo-1575585269294-7d28dd912db8?w=400',
    'Road Bike': 'https://images.unsplash.com/photo-1576435728678-68d0fbf94e91?w=400',
    'City Bike': 'https://images.unsplash.com/photo-1592704655614-6e94863fb0bc?w=400',
    'Eletric Bike': 'https://images.unsplash.com/photo-1670868079900-356caf7b52d8?w=400'
}
st.image(image_urls[opcao], width=400)

st.markdown(f'## Você escolheu a: {opcao}')
st.markdown('---')

# inputs do usuário
col1, col2, col3 = st.columns(3)

with col1:
    dias = st.number_input(
        f'Por quantos dias a {opcao} foi alugada?',
        min_value=0,
        max_value=30,
        value=1,
        step=1
    )

with col2:
    horas = st.number_input(
        f'Quantas horas extras?',
        min_value=0,
        max_value=23,
        value=0,
        step=1
    )

with col3:
    km = st.number_input(
        f'Quantos km você pedalou com a {opcao}?',
        min_value=0.0,
        value=0.0,
        step=0.1,
        format='%.1f'
    )

# preços das bicicletas
if opcao == 'Mountain Bike':
    diaria = 80
    hora_extra = 15
elif opcao == 'Road Bike':
    diaria = 100
    hora_extra = 20
elif opcao == 'Eletric Bike':
    diaria = 120
    hora_extra = 25
elif opcao == 'City Bike':
    diaria = 50
    hora_extra = 10

# informaçoes adicionais sobre cada bike
st.markdown('---')
st.markdown('### Informações da bicicleta')

info_bikes = {
    'Mountain Bike': 'Ideal para trilhas e terrenos irregulares. Suspensão dianteira, pneus largos.',
    'Road Bike': 'Perfeita para estradas pavimentadas. Leve e aerodinâmica para alta velocidade.',
    'City Bike': 'Confortável para ruas urbanas. Cestinha incluída, perfeita para passeios.',
    'Eletric Bike': 'Assistência elétrica para subidas longas. Autonomia de até 60km.'
}
st.info(info_bikes[opcao])

# cálculo do aluguel
if st.button('Calcular o valor do aluguel', type='primary'):
    total_dias = dias * diaria
    total_horas_extras = horas * hora_extra
    total_km = km * 2
    aluguel_total = total_dias + total_horas_extras + total_km

    with col2:
        if horas > 0:
            st.metric('Horas Extras', f'R${total_horas_extras:.2f}',
                      f'{horas}h x R${hora_extra}')
        else:
            st.metric('Horas Extras', 'R$ 0,00')

    with col3:
        if km > 0:
            st.metric('Quilometragem', f'R${total_km:.2f}',
                      f'{km} km x R$ 2,00')
        else:

            st.metric('Quilometragem', 'R$ 0,00')

    # resultado final
    st.markdown('---')
    st.markdown(f'''
    ###  Resumo do Aluguel
    - **Período:** {dias} dias + {horas} horas  
    - **Distância:** {km} km  
    - **Valor Total:** **R$ {aluguel_total:.2f}**
    ''')
# Rodapé
st.markdown('---')
st.markdown('''
<div style='text-align: center'>
<p> Contato: (11) 9999-88888 | contato@bikerent.com.br</p>
<p>2025 BikeRent - Todos os direirots reservados</p>
</div>
''', unsafe_allow_html=True)
