import numpy as np
import streamlit as st
import joblib

def load_model():
    return joblib.load("regression.joblib")

def predict(model, size, nb_rooms, garden):
    return model.predict(np.array([[size, nb_rooms, garden]]))

model = load_model()

size = st.number_input("Insert size", step=1)
nb_rooms = st.number_input("Insert bedrooms number", step=1)
garden = st.toggle("Has garden ?")

st.write(predict(model, size, nb_rooms, garden))
