# Import libraries
import streamlit as st
import pandas as pd
import pickle
with open('model_best.pkl', 'rb') as file_5:
    model = pickle.load(file_5)

def run():
    st.write("# Predict Player's Rating")

    # Form Inference
    with st.form('Form'):
        st.write('### Isi dengan data pemain')
        name = st.text_input('Masukkan nama pemain', placeholder='John Simatupang')
        age = st.number_input('Masukkan usia pemain', min_value=0, max_value=60, value=25)
        height = st.number_input('Masukkan tinggi pemain', min_value=0, max_value=250, value=180)
        weight = st.number_input('Masukkan berat pemain', min_value=0, max_value=100, value=50)
        price = st.number_input('Masukkan harga pemain dalam euro', min_value=0)

        # Input
        pilihan = ['Low', 'Medium', 'High']
        attack = st.selectbox('Attacking Work Rate', pilihan)
        defence = st.selectbox('Defensive Work Rate', pilihan)

        # Slider
        pace = st.slider('Pace Total', min_value=0, max_value=100)
        shoot = st.slider('Shoot Total', min_value=0, max_value=100)
        passing = st.slider('Pass Total', min_value=0, max_value=100)
        dribbling = st.slider('Dribble Total', min_value=0, max_value=100)
        defending = st.slider('Defend Total', min_value=0, max_value=100)
        physics = st.slider('Physicality Total', min_value=0, max_value=100)

        submit = st.form_submit_button('predict')
        
    # Inference dataset
    data_inf = {
    'Name': name,
    'Age': age,
    'Height': height,
    'Weight': weight,
    'Price': price,
    'AttackingWorkRate': attack,
    'DefensiveWorkRate': defence,
    'PaceTotal': pace,
    'ShootingTotal': shoot,
    'PassingTotal':passing,
    'DribblingTotal': dribbling,
    'DefendingTotal': defending,
    'PhysicalityTotal':physics}

    data_inf = pd.DataFrame([data_inf])
    data_inf

    # predict
    if submit:
        result = model.predict(data_inf)
        st.write(f'si {data_inf["Name"][0]}, memiliki rating {round(result[0])}')
    