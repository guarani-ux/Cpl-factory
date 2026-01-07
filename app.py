import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. PAGE SETUP
st.set_page_config(page_title="CPL Factory: Travertine Suite", layout="wide")

# 2. THE BRAIN
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 3. GLOBAL INPUT (Sidebar)
with st.sidebar:
    st.title("🏛️ CPL ARCHITECT")
    project_name = st.text_input("Project Name", placeholder="e.g. Calgary Tech Skills")
    st.divider()
    st.info("Operating in Travertine Mode")

# 4. MAIN CONTENT AREA
if project_name:
    st.header(f"Project: {project_name}")
    
    # THIS IS THE AREA YOU ARE LOOKING FOR
    brief_input = st.text_area(
        "📝 Enter Project Brief / Ideation Notes", 
        placeholder="Type your vision here to turn it into a Travertine execution package...",
        height=300
    )
    
    if st.button("🚀 Generate Full Travertine Package"):
        if brief_input:
            with st.spinner("Processing Specialist Logic..."):
                # Call GPT-4o for 2-page brief + Asana map
                st.success("Package Generated! See tabs below.")
                t1, t2 = st.tabs(["📄 2-Page Brief", "📋 Asana Roadmap"])
                with t1:
                    st.write("Detailed Script and Strategy...")
                with t2:
                    st.table(pd.DataFrame({"Task": ["SEO", "A-Roll", "B-Roll"], "Owner": ["Specialist", "Editor", "Lead"]}))
        else:
            st.error("Please add some notes to the brief area first.")
else:
    st.warning("👈 Enter a Project Name in the sidebar to reveal the Ideation area.")
