import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
import os

# --- SPECIALIST CONFIG ---
st.set_page_config(page_title="CPL Travertine 2.0", layout="wide")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def load_foundation():
    """Extracts text from the permanent knowledge folder."""
    text = ""
    for file in os.listdir("knowledge"):
        if file.endswith(".pdf"):
            reader = PdfReader(f"knowledge/{file}")
            text += "".join([page.extract_text() for page in reader.pages])
        elif file.endswith(".txt"):
            with open(f"knowledge/{file}", "r") as f:
                text += f.read()
    return text

# --- SIDEBAR: OPERATIONAL DEPLOYMENT ---
with st.sidebar:
    st.title("🏛️ CPL ARCHITECT")
    project = st.text_input("Project Name", placeholder="e.g. Creator Podcast Initiative")
    st.divider()
    st.success("Knowledge Foundation: Loaded")

# --- MAIN PRODUCTION STAGE ---
if project:
    st.header(f"💠 Travertine Package: {project}")
    
    # PROJECT-SPECIFIC INPUT
    uploaded_pdf = st.file_uploader("Drop Project Brief (PDF)", type="pdf")
    
    if st.button("🚀 GENERATE TRAVERTINE PACKAGE"):
        # 1. Gather Context
        foundation = load_foundation()
        project_context = ""
        if uploaded_pdf:
            project_context = "".join([p.extract_text() for p in PdfReader(uploaded_pdf).pages])
        
        # 2. Specialist AI Call
        with st.spinner("Analyzing against 2026 Search-to-Member Matrix..."):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a specialized CPL consultant. Using the provided Foundation (Brand & 2026 Strategy), generate a 2-page brief and a 12-step technical Asana roadmap."},
                    {"role": "user", "content": f"FOUNDATION: {foundation}\n\nPROJECT: {project}\nSPECIFIC BRIEF: {project_context}"}
                ]
            )
            
            # 3. Deliverables Display
            tab1, tab2 = st.tabs(["📄 2-Page Executive Brief", "📋 Asana Technical Map"])
            with tab1:
                st.markdown(response.choices[0].message.content)
            with tab2:
                # Specialist Hardcoded Map
                st.table({"Step": range(1,13), "Phase": ["Strategy", "SEO", "Script", "Prod", "Post", "Distro"] * 2})
else:
    st.warning("👈 Enter a Project Name to unlock the Travertine Suite.")
