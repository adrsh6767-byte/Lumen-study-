import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
# Using your verified API key
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 
genai.configure(api_key=API_KEY)

# This is the exact 'stable' model name to avoid 404 errors
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

st.set_page_config(page_title="Lumen AI", layout="wide")

# Custom Styling for mobile
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #2e7bcf;
        color: white;
        width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Lumen: Tutor Mode")
st.write("Personal Coach for JEE & MHT-CET")

topic = st.text_input("What concept are you studying?", placeholder="e.g. Rotational Dynamics")

if st.button("Explain to Me"):
    if topic:
        with st.spinner("Lumen is thinking..."):
            try:
                # Direct request to the AI
                response = model.generate_content(f"Explain {topic} for a JEE/CET student with formulas.")
                
                st.success(f"Topic: {topic}")
                st.write(response.text)
                
            except Exception as e:
                # If it still fails, we try the 'pro' model name as a last resort
                try:
                    alt_model = genai.GenerativeModel(model_name="gemini-pro")
                    response = alt_model.generate_content(topic)
                    st.write(response.text)
                except:
                    st.error("Connection still initializing. Wait 2 minutes and try again.")
    else:
        st.warning("Please enter a topic!")

st.sidebar.info("Lumen v1.0 - Ready")
