import streamlit as st

st.title('hello world!')
st.write('this in my first streamlit app,')
st.markdown('**Bold** test')

name = st.text_input('what  is your name?')
age = st.slider('pick your age', 0 , 100)
choice = st.button('click me')


st.line_chart([1,2,3])

st.title('my model')
if st.button('predict'):
    st.write('hello world!')