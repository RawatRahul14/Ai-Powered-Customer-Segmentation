# === Python Packages ===
from typing import Dict
import streamlit as st

# === Main Function to handle the weightage ===
def apply_weightage():
    """
    Function will apply the weighatge to every column if, told you the user
    """
    # === A checkbox to ask if there's any need to do weighting ===
    apply_weights = st.checkbox(
        label = "⚖️ Assign custom feature weights?",
        value = False
    )

    if apply_weights:
        """
        If the user wants to apply weights
        """
        # === Dictionary to hold values ===
        feature_weights: Dict[str, float] = {}

        ## === Getting weigts for each value selected by the user ===
        for col in st.session_state["selected_columns"]:
            weight = st.slider(
                label = f"⚖️ Set importance for **{col}**",
                min_value = 0.1,
                max_value = 5.0,
                value = 1.0,
                step = 0.1,
                help = "Default is 1.0 (equal importance). Increase if this feature should influence clustering more."
            )

            ## === Saving each value in the dict ===
            feature_weights[col] = weight

        ## === Saving in the session ===
        st.session_state["feature_weights"] = feature_weights

        # === Preview the weights ===
        st.success("✅ Feature weights set:")
        st.json(feature_weights)

    else:
        """
        If the user did not select for weights
        """
        # === If not applying weights, default to 1.0 ===
        st.session_state["feature_weights"] = {col: 1.0 for col in st.session_state["selected_columns"]}
        st.info("All features will be treated equally (weight = 1.0).")

    # === Show "Proceed to Clustering" Button ===
    if st.button(
        label = "➡️ Next: Choose Scaling",
        key = "weightage_button"
    ):
        # === Updaing the Step ===
        if st.session_state["step"] == 3:
            st.session_state["step"] = 4