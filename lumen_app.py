import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
# 1. Make sure there are NO spaces inside the quotation marks with your key
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 

genai.configure(api_key=API_KEY)

# Using the most stable model name
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Lumen AI", layout="wide")

st.title("🛡️ Lumen: Tutor Mode")

st.subheader("🧠 Ask Lumen to Explain")
topic = st.text_input("What concept should I explain?", placeholder="e.g. Newton's Third Law")

if st.button("Explain Topic"):
    if topic:
        if API_KEY == "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE":
            st.error("Wait! You forgot to paste your actual API Key in the code.")
        else:
            with st.spinner("Lumen is gathering knowledge..."):
                try:
                    # Specific prompt for your exam prep
                    prompt = f"Explain the concept of {topic} clearly for a student preparing for competitive exams. Use bullet points and practical examples."
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"AI Error: {e}")
    else:
        st.warning("Please enter a topic first!")
        
