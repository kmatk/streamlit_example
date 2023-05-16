import streamlit as st
import pandas as pd
import numpy as np
import joblib
import seaborn as sns

from PIL import Image

st.sidebar.title('Sidebar')

st.title('Streamlit Demo with Penguins')
st.header('This is a header')

side_button = st.sidebar.button('Press me!')
if side_button:
    st.sidebar.write('Sidebar button was pressed')

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.subheader('Col2')

col21, col22, col23 = st.columns([3,2,1])
col21.write('Widest column, testing 123, text should wrap around')
col22.write('Medium column, again, were wrapping')
col23.write('Small col, check \'er out')

col2.write('Some information here')

st.markdown('Markdown **syntax** *works*')

'Markdown'
'# Magic'
'$\\frac{WOW}{FRAC}$'

st.write('<h2 style="text-align:center"> Text aligned with HTML code</h2>', unsafe_allow_html=True)

check = st.checkbox('Please check me!')

button_check = st.button('Is box checked')
if button_check:
    if check:
        st.write('The box was checked')
    else:
        st.write('Box was not checked')

animal_options = ['Cats', 'Dogs', 'Guinea Pigs', 'Bearded Dragons']
fav_animal = st.radio('Which animal is your favorite?', animal_options)
fav_button = st.button('Submit Animal')
if fav_button:
    st.write(f'You selected {fav_animal} as your favorite animal')
    if fav_animal == 'Cats':
        st.write('Meow')
    else:
        st.write('Animal noises')

fav_animal2 = st.selectbox('Fav Animal?', animal_options)
fav_button2 = st.button('Submit Animal2')
if fav_button2:
    st.write(f'You selected {fav_animal2} as your favorite animal')
    if fav_animal2 == 'Cats':
        st.write('Meow')
    else:
        st.write('Animal noises')

multi_animal = st.multiselect('Which animals do you like?', animal_options)
button_like = st.button('Submit')
if button_like:
    st.write(multi_animal)
    st.write(f'Youf first pick was {multi_animal[0]}')

num_pets = st.slider('How many pets do you have?', min_value=2, max_value=10, step=2)

in_text = st.text_input('What is your pets name?', value='I don\'t have a pet')
st.write(f'Pet\'s name is: {in_text}')

in_num = st.number_input('How many pets do you have?', min_value=0)
st.write(f'You have {in_num} pets')

penguins = sns.load_dataset('penguins')
st.write(penguins.head())