import streamlit as st
import pandas as pd
from openai import OpenAI

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="CPL Execution Suite", layout="wide")

# Connect to the "Brain" (Secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🏛️ CPL Factory: Production Architect")

# --- SIDEBAR: MODE SELECTION ---
with st.sidebar:
    st.header("Strategic Controls")
    mode = st.radio("Operating Mode", ["Ideation & Scratchpad", "Document Analysis"])
    
    project_name = st.text_input("Project Name", placeholder="e.g., Calgary Tech Hub")
    
    st.divider()
    st.caption("Mode: Cloud-Active | Specialist Enabled")

# --- MAIN INTERFACE ---
if project_name:
    # Ideation Scratchpad (Always visible in Ideation Mode)
    if mode == "Ideation & Scratchpad":
        user_notes = st.text_area("Ideation & Scratchpad", 
                                 placeholder="Type your raw thoughts, hooks, or specialist requirements here...",
                                 height=150)
        
        if st.button("🚀 Generate Full 2-Page Brief"):
            with st.spinner("Architecting Production Assets..."):
                # AI Prompting for Specialist-Level Output
                prompt = f"""
                Act as an Executive Producer and Algorithm Specialist. 
                Generate a 2-page Production Brief for the project: '{project_name}'.
                Context from Specialist Notes: {user_notes}
                
                Requirements:
                1. Executive Summary & Goal
                2. Search Intent & Audience Psychographics
                3. Full 3-Act Script (Hook, Value, CTA)
                4. 12-Step Asana Technical Implementation Map
                """
                
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "system", "content": "You are a specialized production consultant."},
                              {"role": "user", "content": prompt}]
                )
                
                st.session_state.full_brief = response.choices[0].message.content

    # --- RESULTS DISPLAY ---
    if 'full_brief' in st.session_state:
        tab1, tab2 = st.tabs(["📄 2-Page Production Brief", "📋 Asana Technical Map"])
        
        with tab1:
            st.markdown(st.session_state.full_brief)
            st.download_button("📥 Download Full Brief", st.session_state.full_brief, file_name=f"{project_name}_Brief.md")
            
        with tab2:
            st.subheader("Implementation Checklist")
            tasks = [
                {"Task": "Keyword Gap Analysis", "Section": "Strategy"},
                {"Task": "Final Script Compliance", "Section": "Pre-Prod"},
                {"Task": "A-Roll Executive Filming", "Section": "Production"},
                {"Task": "Metadata & CTA Link Setup", "Section": "Post-Prod"}
            ]
            st.table(pd.DataFrame(tasks))
else:
    st.info("Enter a Project Name in the sidebar to begin Ideation.")
