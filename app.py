import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pdfplumber

st.title('PDF To Word Cloud Generator')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    try:
        # Open PDF with error handling
        with pdfplumber.open(uploaded_file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()

        # Preprocess text (optional):
        # - Remove unwanted characters, punctuations, or stop words
        # - Perform stemming or lemmatization for better analysis

        wordcloud = WordCloud(
            width=800, height=400, background_color='white',
            stopwords={'the', 'a', 'an', 'of', 'is'}  # Add common stopwords
        ).generate(text)

        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot()

        # Download option with error handling
        try:
            st.download_button(
                label="Download Word Cloud",
                data=wordcloud.to_array(),
                file_name="word_cloud.png",
                mime="image/png"
            )
        except Exception as e:
            st.error(f"Error downloading Word Cloud: {e}")

    except Exception as e:
        st.error(f"Error processing PDF: {e}")

else:
    st.write("No PDF uploaded.")
