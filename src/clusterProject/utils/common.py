# === Python Modules ===
import uuid
import datetime

import streamlit as st

# === Function to create a unique id per session ===
def create_uuid() -> str:
    """
    Function will create a uuid id using uuid + datetime modules

    Args:
        - None

    Returns:
        - uuid (str): Unique id per session
    """
    uuid_id: str = str(uuid.uuid4().hex[:23])
    time: str = str(datetime.datetime.now().strftime("%H%M%S"))

    uuid_str: str = f"{uuid_id}-{time}"

    return uuid_str

# === Function to initialise all the keys in session state of streamlit ===
def init_sessions():
    """
    Will initialise the session state keys
    """
    defaults = {
        "session_id": None,
        "file_name": "",
        "columns": [],
        "status": None,
        "preview": [],
        "error": "",
        "whole_file": None,
        "index_column": "",
        "filtered_columns": None,
        "selected_columns": None,
        "step": 0
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value