import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength_criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase Letter": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special Character (!@#$%^&*)": bool(re.search(r"[!@#$%^&*]", password))
    }

    # Calculate strength
    strength_score = sum(strength_criteria.values())

    # Determine strength level
    if strength_score == 5:
        strength = "Very Strong ✅"
        color = "green"
    elif strength_score == 4:
        strength = "Strong 🟢"
        color = "blue"
    elif strength_score == 3:
        strength = "Moderate ⚠️"
        color = "orange"
    else:
        strength = "Weak ❌"
        color = "red"

    return strength, color, strength_criteria

# Streamlit App UI
st.title("🔒 Password Strength Checker")
st.write("Enter a password below to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    strength, color, criteria = check_password_strength(password)
    
    st.markdown(f"### Strength: <span style='color:{color}; font-size:20px'>{strength}</span>", unsafe_allow_html=True)
    
    # Show criteria feedback
    st.subheader("Password Strength Criteria")
    for criterion, met in criteria.items():
        icon = "✅" if met else "❌"
        st.write(f"{icon} {criterion}")

    # Suggestions
    if strength in ["Weak ❌", "Moderate ⚠️"]:
        st.subheader("🔹 Suggestions to Improve Your Password")
        st.write("- Use at least 8 characters.")
        st.write("- Include both uppercase and lowercase letters.")
        st.write("- Add numbers and special characters (!@#$%^&*).")

# Run the app using:
# streamlit run app.py
