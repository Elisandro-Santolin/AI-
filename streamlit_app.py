import streamlit as st 
from langchain_openai.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


st.title("🔗 SmartLocker IA")

openai_api_key = os.getenv('API_KEY')


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.1, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("input_form"):
    text = st.text_area(
        "Informe sua dúvida:"
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Your OpenAI API key is invalid!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)
