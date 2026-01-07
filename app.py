import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Page Config for Mobile Stability
st.set_page_config(page_title="CPL Factory", layout="wide")

# 2. Connection to the Brain
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("Missing API Key in Secrets!")
    st.stop()

# 3. Sidebar: Ideation First
with st.sidebar:
    st.header("Executive Suite")
    mode = st.radio("App Mode", ["Ideation Scratchpad", "Document Analysis"])
    project_name = st.text_input("Project Name", placeholder="e.g. Calgary Tech Skills")
    st.divider()
    st.info("Status: Execution Ready")

# 4. Main Engine
if project_name:
    st.title(f"🏛️ {project_name}: Strategy")
    
    if mode == "Ideation Scratchpad":
        user_notes = st.text_area("Ideation & Specialist Requirements", height=200)
        
        if st.button("Generate 2-Page Execution Brief"):
            with st.spinner("AI Architecting..."):
                # Specialist-level prompt for 2-page depth
                prompt = f"Create a 2-page production brief for {project_name}. Notes: {user_notes}. Include 3-act script and 12-step Asana map."
                # [Internal call to gpt-4o logic here]
                st.success("Brief Generated Below")
                st.markdown("### 📄 Production Brief")
                st.write("Content expanding based on your specialist notes...")
else:
    st.warning("👈 Enter a Project Name in the sidebar to begin.")
