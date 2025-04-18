import streamlit as st
import re

def check_password_strength(password):
    """Evaluate the strength of a password."""
    strength = 0
    criteria = {
        "Length (8+ characters)": len(password) >= 8,
        "Uppercase letters": bool(re.search(r'[A-Z]', password)),
        "Lowercase letters": bool(re.search(r'[a-z]', password)),
        "Numbers": bool(re.search(r'[0-9]', password)),
        "Special characters": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    for criterion, met in criteria.items():
        if met:
            strength += 1

    return strength, criteria

# Streamlit app
st.title("Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, criteria = check_password_strength(password)
    st.subheader("Password Strength")
    st.progress(strength / len(criteria))

    st.write("### Criteria:")
    for criterion, met in criteria.items():
        st.write(f"- {criterion}: {'✅' if met else '❌'}")

    if strength == len(criteria):
        st.success("Your password is strong!")
    elif strength >= len(criteria) // 2:
        st.warning("Your password is moderate. Consider improving it.")
    else:
        st.error("Your password is weak. Please make it stronger.")