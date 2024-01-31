import streamlit as st

number_1 = st.number_input('Insert a number_1')
number_2 = st.number_input('Insert a number_2')
calc=number_1*number_2
st.write('The current number is ', calc)
