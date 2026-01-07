import streamlit as st
import pandas as pd
from openai import OpenAI
from pypdf import PdfReader
from docx import Document
import io

st.set_page_config(page_title="CPL Travertine Architect", layout="wide")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- SIDEBAR ---
with st.sidebar:
    st.title("🏛️ CPL ARCHITECT")
    project = st.text_input("Project Name", value="Freedom to read")
    st.divider()
    st.info("Travertine Engine: Active")

# --- MAIN INTERFACE ---
if project:
    st.header(f"💠 Project: {project}")
    
    # NEW: MULTI-SOURCE INPUT
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Option A: Manual Ideation")
        manual_notes = st.text_area("Scratchpad notes...", height=200)

    with col2:
        st.subheader("Option B: Upload Document")
        uploaded_file = st.file_uploader("Drop PDF or Word Doc here", type=["pdf", "docx"])

    if st.button("🚀 EXECUTE TRAVERTINE PACKAGE"):
        context = manual_notes
        
        # Logic to extract text from files
        if uploaded_file:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                context += "\n" + "".join([page.extract_text() for page in reader.pages])
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                doc = Document(io.BytesIO(uploaded_file.read()))
                context += "\n" + "".join([para.text for para in doc.paragraphs])

        if context:
            with st.spinner("Analyzing Brief & Designing Package..."):
                # Specialist Prompting
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "Generate a 2-page production brief and 12-step Asana map."},
                              {"role": "user", "content": f"Context: {context}"}]
                )
                output = response.choices[0].message.content
                
                # Deliverables Display
                t1, t2 = st.tabs(["📄 Full Travertine Brief", "📋 Asana Roadmap"])
                with t1:
                    st.markdown(output)
                with t2:
                    st.table(pd.DataFrame({"Step": range(1,5), "Task": ["SEO Analysis", "Script Lockdown", "A-Roll", "Distribution"]}))
        else:
            st.error("Please provide manual notes or upload a document to proceed.")
