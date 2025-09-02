# === Python Modules ===
import streamlit as st
import requests
import pandas as pd

# ===  ===
def render_sidebar(
        API_URL: str
):
    """
    Here the user uploads the file, in either csv or xlsx format. And the function also handles file switch.
    """
    uploaded_file = st.file_uploader(
        label = "📁 Upload CSV or Excel file",
        accept_multiple_files = False,
        type = ["csv", "xlsx"]
    )

    if uploaded_file is not None:
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }
        response = requests.post(
            f"{API_URL}/upload",
            files = files
        )

        if response.status_code == 200:
            data = response.json()
            st.session_state["session_id"] = data["session_id"]
            st.session_state["file_name"] = data["file_name"]
            st.session_state["columns"] = data["columns"]
            st.session_state["status"] = data["status"]
            st.session_state["preview"] = data["preview"]
            st.session_state["error"] = data["error"]
            st.session_state["whole_file"] = data["whole_file"]

            st.success(f"✅ File '{data['file_name']}' uploaded successfully!")
        else:
            st.error(f"❌ Upload failed: {response.text}")

    else:
        st.info("👈 Please upload a file to get started.")
        st.session_state["file_name"] = ""
        st.session_state["uploaded_file"] = None
        st.session_state["step"] = 1