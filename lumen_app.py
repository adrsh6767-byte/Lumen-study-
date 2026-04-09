import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
API_KEY = "AIzaSyBcKA2-64-kpT0eIqRkqA6JVWsBomnfYrE" 
genai.configure(api_key=API_KEY)

# Using the most widely compatible model name
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Lumen AI", layout="wide", page_icon="🛡️")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background-color: #2e7bcf;
        color: white;
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Lumen: Tutor Mode")
st.write("Your personal engineering entrance exam coach.")

st.divider()

topic = st.text_input("Enter a concept to master:", placeholder="e.g. Rotational Dynamics")

if st.button("Explain to Me"):
    if topic:
        with st.spinner("Lumen is connecting to the brain..."):
            try:
                # Custom prompt tailored for JEE/MHT-CET prep
                prompt = (f"Provide a clear, high-yield explanation of {topic} for a student "
                          f"preparing for engineering entrance exams. Include core concepts, "
                          f"key formulas, and one practical application.")
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success(f"Mastering: {topic}")
                    st.markdown(response.text)
                else:
                    st.error("The AI returned an empty response. Please try again.")
                
            except Exception as e:
                # Direct error reporting to identify the exact issue
                st.error(f"Connection Issue: {str(e)}")
                st.info("Tip: If you just created the API key, it can take 5-10 minutes to activate.")
    else:
        st.warning("Please enter a topic first!")

st.sidebar.info("Lumen Status: Online")
