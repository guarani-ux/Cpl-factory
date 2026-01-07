import streamlit as st
import pandas as pd
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="CPL Factory | Executive Strategy", layout="wide")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 CPL Factory: Algorithm & Strategy Engine")
st.subheader("Bypass hardware. Deploy 24/7.")

# --- SIDEBAR: INPUTS ---
with st.sidebar:
    st.header("Project Parameters")
    project_name = st.text_input("Program Name", placeholder="e.g. Calgary Tech Seniors")
    audience = st.selectbox("Primary Audience", ["Seniors", "Youth", "Newcomers", "General"])
    goal = st.radio("Primary Goal", ["Brand Awareness", "Direct Signups", "Educational"])
    
    st.divider()
    uploaded_file = st.file_uploader("Upload CPL Strategy Doc (PDF/TXT)", type=["pdf", "txt"])

# --- MAIN LOGIC ---
if st.button("Generate Strategy & Asana Blueprint"):
    if project_name:
        # Mocking the AI Analysis Logic for the prompt context
        st.success(f"Analysis Complete for {project_name}")
        
        # --- TABBED RESULTS ---
        tab1, tab2 = st.tabs(["📺 YouTube Strategy", "📋 Asana Blueprint"])
        
        with tab1:
            st.markdown("### Top 3 Optimized Concepts")
            data = {
                "Title Idea (High CTR)": [
                    f"Why {project_name} is Changing Lives",
                    f"The Secret to Success in {project_name}",
                    f"Don't Start {project_name} Until You See This"
                ],
                "Search Intent": ["Informational", "Comparison", "Tutorial"],
                "Hook Type": ["Story-based", "Fear of Missing Out", "Direct Value"]
            }
            st.table(pd.DataFrame(data))
            
        with tab2:
            st.markdown("### Asana Project Structure")
            tasks = [
                {"Task Name": "Scripting: Retention-focused", "Section": "Pre-Production", "Priority": "High"},
                {"Task Name": "Thumbnail A/B Test Design", "Section": "Creative", "Priority": "High"},
                {"Task Name": "CPL Brand Compliance Review", "Section": "Legal/Compliance", "Priority": "Medium"}
            ]
            df_tasks = pd.DataFrame(tasks)
            st.dataframe(df_tasks)
            
            # --- CSV DOWNLOAD FOR ASANA ---
            csv = df_tasks.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Asana CSV Import File",
                data=csv,
                file_name=f"{project_name}_asana_import.csv",
                mime="text/csv",
            )
    else:
        st.error("Please enter a Program Name to begin.")

# --- FOOTER ---
st.divider()
st.caption("CPL Factory v2.0 | Operational Strategy | GitHub Cloud Deployment")
