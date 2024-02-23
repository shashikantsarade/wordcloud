import streamlit as st
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pdfplumber

st.title('PDF TO Word Cloud Generator')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    # Rest of the code
else:
    st.write("No text found in the PDF.")

    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(text)

    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    st.pyplot()

    st.download_button(
        label="Download Word Cloud",
        data=wordcloud.to_array(),
        file_name="word_cloud.png",
        mime="image/png"
    )
