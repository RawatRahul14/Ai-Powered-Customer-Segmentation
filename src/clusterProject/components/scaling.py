# === Python Modules ===
import streamlit as st
import requests
import pandas as pd

def apply_scaling(
        API_URL: str
):
    """
    Apply scaling to the dataset based on the user's choice
    """
    # === Scaler selection ===
    scaler_option = st.selectbox(
        "🔄 Choose a Scaling Method:",
        ["StandardScaler (default)", "MinMaxScaler", "RobustScaler"]
    )

    # === Button to apply sclaing ===
    if st.button(
        label = "Apply Scaling?",
        key = "scaling_button"
    ):
        """
        Applying scaling only after the user clicked the button.
        """
        # === Updating the Scaling option ===
        st.session_state["scaling_option"] = scaler_option

        # === Sending the data to backend to apply scaling ===
        json_file = {
            "selected_columns": st.session_state["selected_columns"],
            "scaling_option": st.session_state["scaling_option"],
            "feature_weights": st.session_state["feature_weights"],
            "file_name": st.session_state["file_name"],
            "index_column": st.session_state["index_column"]
        }

        scaled_data = requests.post(
            url = f"{API_URL}/scaling",
            json = json_file
        )

        # === If the requests gets successful ===
        if scaled_data.status_code == 200:
            """
            Saving the scaled data
            """
            data_scaled = scaled_data.json()
            st.session_state["scaled_data"] = data_scaled["scaled"]

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📊 Original Data")
                original_df = pd.DataFrame(st.session_state["preview"])
                st.dataframe(original_df[st.session_state["selected_columns"]])

            with col2:
                st.subheader("⚖️ Scaled Data")
                st.dataframe(pd.DataFrame(st.session_state["scaled_data"]).head(5))

        # === Updaing the Step ===
        if st.session_state["step"] == 4:
            st.session_state["step"] = 5