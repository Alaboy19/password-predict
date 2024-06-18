import streamlit as st
import hashlib  # For password hashing (replace with your actual prediction logic)

st.title("Password Frequency Predictor(Per million Usage)")

# Password input
password = st.text_input("Password", type="password")  # Masks input for security

# Prediction (placeholder logic - replace with your real model)
if password:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash for demonstration
    strength_score = len(hashed_password) / 100.0  # Dummy score based on hash length

    # Display prediction
    st.metric("Prediction", f"{strength_score:.2f}", delta=None, delta_color="normal")
else:
    st.warning("Please enter a password.")