import streamlit as st
import pandas as pd

# STABILITY FIRST
st.set_page_config(page_title="CPL Factory", layout="centered")

st.title("🏛️ CPL Factory Pro")

# SIDEBAR: Always put inputs here for mobile
with st.sidebar:
    st.header("1. Input")
    project = st.text_input("Program Name")
    st.divider()
    st.info("System Online")

# MAIN CONTENT: No tabs, just vertical flow
if project:
    st.subheader(f"🚀 Execution Plan: {project}")
    
    # Placeholder for the Brief
    st.markdown("### 📄 2-Page Executive Brief")
    st.write("Generating deep-intelligence brief for specialists...")
    
    # Simple Table for Asana
    st.markdown("### 📋 Asana Technical Map")
    data = {"Task": ["Strategy Gap", "Script Review", "Compliance"], "Status": ["Pending", "Pending", "Urgent"]}
    st.table(pd.DataFrame(data))
else:
    st.warning("👈 Enter a Project Name in the sidebar.")
