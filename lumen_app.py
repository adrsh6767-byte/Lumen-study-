import streamlit as st
import google.generativeai as genai

# --- AI SETUP ---
# Replace the text below with your actual API key
genai.configure(api_key="PASTE_YOUR_KEY_HERE")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Lumen AI", layout="wide")

st.title("🛡️ Lumen: AI Tutor Mode")

# Simple Sidebar
menu = ["AI Explainer", "Study Tools"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "AI Explainer":
    st.subheader("🧠 Ask Lumen to Explain")
    topic = st.text_input("What concept should I explain?", placeholder="e.g. Newton's Third Law")
    
    if st.button("Explain Topic"):
        if topic:
            with st.spinner("Lumen is thinking..."):
                # This tells the AI to explain it specifically for your exams
                prompt = f"Explain the concept of {topic} clearly for an 18-year-old student preparing for engineering entrance exams. Use bullet points and simple examples."
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
        else:
            st.warning("Please enter a topic first!")

elif choice == "Study Tools":
    st.write("More tools coming soon for your prep!")
    
