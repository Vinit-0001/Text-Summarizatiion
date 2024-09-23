import streamlit as st
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

import requests
from transformers import pipeline


summarizer = pipeline('summarization')


def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator='\n', strip=True)
        return text
    except Exception as e:(
        st.error(f"Error extracting text from URL: {e}"))
    return ""


def extract_text_from_pdf(pdf):
    try:
        doc = PdfReader(pdf)
        text = ""
        for page in doc.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""


def summarize_text(text, max_length=150, min_length=50):
    if len(text) < 50:
        st.error("Text is too short for summarization.")
        return ""
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


st.title("Content Summarizer")
st.write("Upload PD, input text or provide an URL for summarization")
input_type = st.sidebar.selectbox("Select input type", ['Text', 'URL', 'PDF'])

txt = ""

if input_type == "Text":
    text_input = st.text_area("Enter you text here")
    txt = text_input
elif input_type == "PDF":
    pdf = st.file_uploader("Choose a PDF file", type=["pdf"])
    if pdf:
        with st.spinner("Extracting Text"):
            txt = extract_text_from_pdf(pdf)
            st.success("Text extracted successfully")
            st.text_area("Extracted Text",txt)
elif input_type == "URL":
    url = st.text_input("Enter the URL")
    if url:
        with st.spinner("Extracting text from URL"):
            txt = extract_text_from_url(url)
            st.success("Text extracted successfully")
            st.text_area("Extracted Text", txt)

if txt:
    if st.button("Summarize"):
        with st.spinner("Summarizing text"):
            summary = summarize_text(txt)
            st.success("Summary Generated")
            st.text_area("Summary", summary)
