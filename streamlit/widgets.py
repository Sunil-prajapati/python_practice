import streamlit as st
import pandas as pd

st.title("Stream text input")

name = st.text_input("Enter you name:")

age = st.slider("select your age:",0,100,25)

st.write(f"your age is , {age}")

options = ["Python", "Javascript", "Java"]
choice = st.selectbox("Choose your favourite language:",options)

st.write(f"Your selected language is {choice}")

if name:
    st.write(f"Hello, {name}")

data = {
    "Name":["John","Jane","Jake"],
    "Age":[28,24,40],
    "City":["New york", "Los Angeles", "Mumbai"]
}
df = pd.DataFrame(data)
df.to_csv("sampleData.csv")
st.write(df)



uploaded_files = st.file_uploader("Choose a CSV File", type="csv")
if uploaded_files is not None:
    df= pd.read_csv(uploaded_files)
    st.write(df)
