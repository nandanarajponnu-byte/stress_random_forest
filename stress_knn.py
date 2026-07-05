import streamlit as st
import pickle
st.write("enter the values required if you're stressed or not")
a=st.number_input("Enter humidity level")
b=st.number_input("Enter temperature level")
c=st.number_input("Enter number of steps")
if st.button("predict"):
    with open(r"C:\Users\nanda\PycharmProjects\akira\stress_model2.pkl", "rb") as file:
        loaded_model2 = pickle.load(file)
    result=loaded_model2.predict([[a,b,c]])
    st.write(result)