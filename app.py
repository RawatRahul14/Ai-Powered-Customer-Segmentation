# === Python Modules ===
import streamlit as st
import pandas as pd

# === Utils ===
from clusterProject.utils.common import init_sessions

# === Components ===
from clusterProject.components.sidebar import render_sidebar
from clusterProject.components.columns import get_columns

# === FastAPI Endpoint ===
API_URL = "http://127.0.0.1:8000"

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
    if st.session_state["status"] == "fail":
        st.subheader(f"Error: {st.session_state['error']}")

    elif st.session_state["status"] == "success":
        st.subheader("🗂️ Data Preview: ")
        st.dataframe(pd.DataFrame(st.session_state["preview"]))

        # === Updating the step ===
        st.session_state["step"] = 1

        #### === Step 2: Selecting the Index Column ===
        if st.session_state["step"] == 1:
            st.markdown("---")
            st.subheader("🔑 Select the index column:")
            ## === Column Selection function ===
            get_columns(API_URL)

            #### === Step 3: Selecting the Columns ===
            if st.session_state["step"] == 2:
                st.markdown("---")
                st.subheader("📊 Select Columns for Clustering:")

# === Runing the function ===
if __name__ == "__main__":
    main()