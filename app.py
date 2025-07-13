import streamlit as st
from collections import Counter
import string
import matplotlib.pyplot as plt

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    words = [word for word in tokens if word.isalpha()]
    return words

def get_word_frequencies(words):
    return Counter(words)

st.title("📊 FRELYZER : A Frequency Analyzer")

input_text = st.text_area("Enter text to analyze", height=1000)

if st.button("Analyze"):
    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        words = preprocess_text(input_text)
        freq = get_word_frequencies(words)
        
        st.subheader("Top 10 Words")
        for word, count in freq.most_common(10):
            st.write(f"**{word}**: {count}")

        # Plot
        common = freq.most_common(10)
        labels, counts = zip(*common)

        fig, ax = plt.subplots()
        ax.bar(labels, counts, color='skyblue')
        plt.xticks(rotation=45)
        st.pyplot(fig)
