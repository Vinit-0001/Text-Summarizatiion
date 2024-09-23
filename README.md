**Content Summarizer - Text, PDF, and URL**
This Streamlit-based application allows users to summarize content from various input types—text, PDFs, and URLs—using a state-of-the-art transformer-based summarization model. The app supports real-time summarization by extracting the key points from lengthy documents, articles, or raw text, making it an ideal tool for quick content insights.

**Key Features**
1) Text Summarization: Input large chunks of text and get a concise summary.
2) PDF Summarization: Upload PDFs, extract their content, and summarize it instantly.
3) URL Summarization: Input a URL, extract its main content, and summarize it within seconds.
4) Real-time Processing: Responsive interface powered by Streamlit, providing real-time text extraction and summarization.
4) AI-powered Summarization: Uses the Transformer model from Hugging Face's transformers library for advanced natural language processing.

**Dependencies**
1) Streamlit: For building an interactive UI.
2) PyPDF2: For extracting text from PDFs.
3) BeautifulSoup4: For scraping text from URLs.
4) Requests: For making HTTP requests to retrieve web content.
5) Transformers: Hugging Face’s library to load the pre-trained summarization model.
