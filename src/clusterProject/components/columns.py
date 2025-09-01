# === Python Modules ===
import streamlit as st
import requests

# === Main Column Extraction Function ===
def get_columns(
        API_URL: str
):
    """
    Get the names of the columns user selects
    """
    # === Giving the user option to select the columns ===
    index_column = st.selectbox(
        label = "Select the name of the column you want to use as index:",
        options = st.session_state["columns"],
        index = 0
    )

    # === Button to move ahead ===
    if st.button(
        label = "You want to continue with this column?" 
    ):
        """
        Saves the column name in the session and returns the rest of the columns using FastAPI endpoint.
        """
        # === If the user did not select the column ===
        if index_column is None:
            st.error("First you need to select the column.")

        st.session_state["index_column"] = index_column

        filtered_columns = requests.post(
            url = f"{API_URL}/columns",
            json = {
                "index_column_name": index_column,
                "all_columns": st.session_state["columns"]
            }
        )

        if filtered_columns.status_code == 200:
            """
            Saving the filtered columns in session_state
            """
            data_col = filtered_columns.json()
            st.session_state["filtered_columns"] = data_col["filtered_columns"]

            # === Updaing the Step ===
            st.session_state["step"] = 2