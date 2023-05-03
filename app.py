import streamlit as st

st.header('HELLO WORLD')
st.header(':red[_PLI AKA BOGOR_]')
st.write('Kalkulator')
number = st.number_input('Masukkan nomor anda')
st.write(f'The current number is ', 54)
st.write('Bilangan ketiga adalah')
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['46', '31', '27'])

st.line_chart(chart_data)