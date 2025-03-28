import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open("tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)

# Load trained model
model = tf.keras.models.load_model("fake_news_detector.h5")

# Compile model again to avoid warnings (doesn't affect inference)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Define max sequence length (should match what was used in training)
MAX_SEQUENCE_LENGTH = 300

# Streamlit UI
st.title("📰 Fake News Detector")
st.write("Enter a news article below to check if it's real or fake.")

# User Input
news_text = st.text_area("Paste the news article here:")

if st.button("Check News"):
    if news_text.strip():
        with st.spinner("Analyzing the news..."):
            # Preprocess input
            seq = tokenizer.texts_to_sequences([news_text])
            padded_seq = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH, padding='post')

            # Make prediction
            prediction = model.predict(padded_seq)[0][0]

        # Display result
        st.progress(float(prediction))  # Show probability as progress bar
        
        if prediction > 0.5:
            st.error("🚨 Fake News Detected!")
            st.write("🔍 **Why is this flagged as fake?**")
            st.write("- The language might match previously detected fake news.")
            st.write("- The claim might not align with verified sources.")
            st.write("- The structure of the article might resemble misinformation patterns.")
        else:
            st.success("✅ This news appears to be real.")
            st.write("🔍 **Why is this considered real?**")
            st.write("- The article structure aligns with credible news sources.")
            st.write("- No strong fake news signals were detected.")
            st.write("- The claim may match fact-checked reliable sources.")

        st.write(f"**Fake News Probability:** {prediction:.2%}")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
