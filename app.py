# === Python Modules ===
import streamlit as st
import pandas as pd

# === Utils ===
from clusterProject.utils.common import init_sessions

# === Components ===
from clusterProject.components.sidebar import render_sidebar

# === FastAPI Endpoint ===
API_URL = "http://127.0.0.1:8000"  # FastAPI backend

# === Main Body ===
def main():
    """
    AI Powered Customer Segmentation
    """

    init_sessions()

    # === Page Configurations ===
    st.set_page_config(
        page_title = "AI powered Customer Segmentation",
        layout = "wide"
    )

    # === Page Title ===
    st.header("📊 AI Powered Customer Segmentation")

    ## === Sidebar ===
    with st.sidebar:
        render_sidebar(API_URL)

    #### === Step 1: Show Preview ===
    if st.session_state["status"] == "success":
        st.subheader("Data Preview: ")
        st.dataframe(pd.DataFrame(st.session_state["preview"]))

    if st.session_state["status"] == "fail":
        st.subheader(f"Error: {st.session_state['error']}")

# === Runing the function ===
if __name__ == "__main__":
    main()