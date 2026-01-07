import streamlit as st
import pandas as pd

# --- MOBILE STABILITY CONFIG ---
st.set_page_config(page_title="CPL Factory", layout="wide")

st.title("🏛️ CPL Factory: Production Architect")

# --- SIDEBAR: IDEATION MODE ---
with st.sidebar:
    st.header("Executive Controls")
    # We set 'Ideation' as the DEFAULT so it never asks for a document first
    mode = st.radio("App Mode", ["Ideation Scratchpad", "Document Analysis"])
    project_name = st.text_input("Program Name", placeholder="e.g. Calgary Tech Skills")
    
    st.divider()
    st.info("System Status: Execution Ready")

# --- MAIN ENGINE: NO DOCUMENT REQUIRED ---
if project_name:
    if mode == "Ideation Scratchpad":
        st.subheader(f"🚀 Ideation: {project_name}")
        scratchpad = st.text_area("Drop your raw vision here...", height=200)
        
        if st.button("Generate 2-Page Execution Brief"):
            st.success("Drafting Specialist-Level Blueprint...")
            # This is where the AI Brief logic lives
            st.markdown("### 📄 Page 1: Strategic Alignment")
            st.write("Targeting high-retention audience segments in the Calgary niche...")
            
    elif mode == "Document Analysis":
        uploaded_file = st.file_uploader("Upload Strategy Doc")
        if uploaded_file:
            st.write("Document Analyzed.")
else:
    st.warning("👈 Enter a Project Name in the sidebar to start Ideation.")
