import streamlit as st

# --- SESSION PERSISTENCE (Stops Greying Out) ---
if "execution_ready" not in st.session_state:
    st.session_state.execution_ready = False

st.title("🏛️ CPL Executive Terminal")

# This forces the app to hold data even if the connection blips
@st.cache_data
def get_heavy_strategy_data(name):
    # Simulated complex logic for a specialist
    return f"Full 2000-word Blueprint for {name}..."

p_name = st.text_input("Enter Project Name", key="p_name_input")

if st.button("Initialize Full Suite"):
    st.session_state.execution_ready = True

if st.session_state.execution_ready:
    st.success("System Live: Execution Mode Active")
    # Your robust script and Asana code goes here
