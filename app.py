import streamlit as st
import pandas as pd
from openai import OpenAI
from pypdf import PdfReader
from docx import Document
import io

# EXECUTION ENGINE CONFIG
st.set_page_config(page_title="CPL Travertine Architect", layout="wide")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- SIDEBAR ---
with st.sidebar:
    st.title("🏛️ CPL ARCHITECT")
    project = st.text_input("Project Name", placeholder="e.g. Calgary Tech Strategy")
    st.divider()
    st.info("Status: Travertine Mode Active")

# --- MAIN INTERFACE ---
if project:
    st.header(f"💠 Project: {project}")
    
    # DUAL INPUT SECTION
    col1, col2 = st.columns(2)
    with col1:
        manual_notes = st.text_area("1. Ideation & Specialist Notes", height=200, placeholder="Type your vision here...")
    with col2:
        uploaded_file = st.file_uploader("2. Drop PDF or Word Doc", type=["pdf", "docx"])

    if st.button("🚀 EXECUTE TRAVERTINE PACKAGE"):
        # Text Extraction Logic
        context = manual_notes
        if uploaded_file:
            if uploaded_file.type == "application/pdf":
                pdf_reader = PdfReader(uploaded_file)
                context += "\n" + "".join([p.extract_text() for p in pdf_reader.pages])
            else:
                doc = Document(io.BytesIO(uploaded_file.read()))
                context += "\n" + "".join([p.text for p in doc.paragraphs])

        if context:
            with st.spinner("Architecting Deliverables..."):
                # Professional Prompting for 2-Page Brief
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "Generate a 2-page production brief and 12-step Asana map."},
                              {"role": "user", "content": f"Project: {project}\nContext: {context}"}]
                )
                
                # OUTPUT TABS
                tab1, tab2, tab3 = st.tabs(["📄 2-Page Brief", "📋 Asana Map", "🎯 SEO Strategy"])
                with tab1:
                    st.markdown(response.choices[0].message.content)
                with tab2:
                    st.table(pd.DataFrame({"Step": range(1,7), "Task": ["SEO Analysis", "Script Lockdown", "A-Roll", "B-Roll", "Edit", "Deploy"]}))
                with tab3:
                    st.code("Primary Tag: Travertine_Package_V1")
        else:
            st.error("Please provide notes or a document to generate the package.")
else:
    st.warning("👈 Enter a Project Name in the sidebar to reveal the Production Suite.")
