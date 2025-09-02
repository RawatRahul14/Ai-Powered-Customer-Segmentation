# === Python Modules ===
import streamlit as st
import requests

# === Main function body to extract index ===
def get_index(
        API_URL: str
):
    """
    Get the names of the index column
    """
    # === Giving the user option to select the columns ===
    index_column = st.selectbox(
        label = "Select the name of the column you want to use as index:",
        options = st.session_state["columns"],
        index = 0
    )

    # === Button to move ahead ===
    if st.button(
        label = "You want to continue with this column?" ,
        key = "index_column_button"
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
            if st.session_state["step"] == 1:
                st.session_state["step"] = 2

# === Main function body to extract columns ===
def get_column_names():
    """
    Get the names of the columns user selected
    """
    selected_columns = st.multiselect(
        label = "Select the name of the columns you want to use: (make sure to not select a column with long description)",
        options = st.session_state["filtered_columns"],
        default = []
    )

    if selected_columns:
        st.markdown(f"List of the selected columns: {selected_columns}")
    else:
        st.warning("⚠️ Please select at least columns for each.")

    st.session_state["selected_columns"] = selected_columns

    # === Button to proceed ===
    if st.button(
        label = "Proceed to next step?",
        key = "column_selection_button"
    ):
        # === If not columns selected it will through error ===
        if not selected_columns:
            st.error("You must select at least one column.")
            return

        # === Updaing the Step ===
        if st.session_state["step"] == 2:
            st.session_state["step"] = 3