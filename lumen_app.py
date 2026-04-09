import streamlit as st
import sqlite3
import pandas as pd
import time
import random
from datetime import datetime

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('lumen_study.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sessions 
                 (id INTEGER PRIMARY KEY, topic TEXT, duration INTEGER, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS formulas 
                 (id INTEGER PRIMARY KEY, subject TEXT, name TEXT, equation TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- APP LAYOUT ---
st.set_page_config(page_title="Lumen AI Study Tool", layout="wide")
st.title("🛡️ Lumen: Study Command Center")

menu = ["Dashboard", "Deep Work Timer", "Formula Vault", "Feynman Auditor"]
choice = st.sidebar.selectbox("Navigate", menu)

# --- MODULE 1: DASHBOARD ---
if choice == "Dashboard":
    st.subheader("Progress Analytics")
    conn = sqlite3.connect('lumen_study.db')
    try:
        df = pd.read_sql_query("SELECT * FROM sessions", conn)
        if not df.empty:
            st.bar_chart(df.set_index('topic')['duration'])
        else:
            st.info("No study sessions logged yet.")
    except:
        st.info("Start your first session to see data!")
    conn.close()

# --- MODULE 2: DEEP WORK TIMER ---
elif choice == "Deep Work Timer":
    st.subheader("Focus Mode")
    topic = st.text_input("What are we mastering right now?")
    if st.button("🚀 Start Session"):
        st.session_state.start_time = time.time()
        st.success(f"Session started for {topic}!")
    if st.button("🛑 End Session"):
        if 'start_time' in st.session_state:
            elapsed = int((time.time() - st.session_state.start_time) / 60)
            conn = sqlite3.connect('lumen_study.db')
            c = conn.cursor()
            c.execute("INSERT INTO sessions (topic, duration, date) VALUES (?, ?, ?)", 
                      (topic, elapsed, datetime.now().strftime("%Y-%m-%d")))
            conn.commit()
            conn.close()
            st.success(f"Logged {elapsed} minutes!")
            del st.session_state.start_time
        else:
            st.error("No active session.")

# --- MODULE 3: FORMULA VAULT ---
elif choice == "Formula Vault":
    st.subheader("Physics & Chemistry Reference")
    with st.form("formula_form"):
        f_sub = st.selectbox("Subject", ["Physics", "Chemistry", "Math"])
        f_name = st.text_input("Concept Name")
        f_equ = st.text_input("Formula")
        if st.form_submit_button("Save"):
            conn = sqlite3.connect('lumen_study.db')
            c = conn.cursor()
            c.execute("INSERT INTO formulas (subject, name, equation) VALUES (?, ?, ?)", (f_sub, f_name, f_equ))
            conn.commit()
            conn.close()
            st.success("Saved!")

# --- MODULE 4: FEYNMAN AUDITOR ---
elif choice == "Feynman Auditor":
    st.subheader("🧠 The Feynman Challenge")
    concept = st.text_input("Concept Name")
    exp = st.text_area("Your explanation:")
    if st.button("Audit"):
        if len(exp.split()) < 30:
            st.warning("Too brief! Explain the 'why'.")
        else:
            challenges = ["How does this change if we double the temperature?", "What's the real-world application?"]
            st.success("Good depth!")
            st.write(f"**Challenge:** {random.choice(challenges)}")
          
