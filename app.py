import streamlit as st
import requests

st.title("💬 Ufalme Wetu Virtual Assistant")

# ✅ Button to show a random quote
if st.button("✨ Show a Chama Quote ✨"):
    response = requests.get("http://127.0.0.1:8000/quote")
    quote = response.json()["quote"]
    st.toast(quote)  # Shows a pop-up

# ✅ User input for chatbot
query = st.text_input("Ask me about chamas...")

if st.button("Ask"):
    response = requests.post("http://127.0.0.1:8000/chat", json={"query": query})
    st.write("🤖:", response.json()["response"])




