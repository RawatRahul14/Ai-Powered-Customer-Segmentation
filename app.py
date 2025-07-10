# === User Interface ===
import streamlit as st

# === Data Frame ===
import pandas as pd

def main():

    # === Header ===
    st.set_page_config(page_title = "AI Customer Segmentation",
                       layout = "wide")
    
    st.header("🤖 AI Powered Customer Segmentation")
    st.markdown("""
        Welcome to the interactive customer segmentation app!  
        Upload your **CSV or Excel** file, choose the features you want to use, and let the app:
        - 📊 Perform K-Means clustering
        - 🧠 Use AI to name segments
        - 🎯 Help you discover customer personas

        ---
    """)

    # === File upload on sidebar ===
    with st.sidebar:
        uploaded_file = st.file_uploader(label = "📁 Upload your csv data.",
                                         accept_multiple_files = False,
                                         type = ["csv", "xlsx"])
        
        # === Handle file switch without rerun ===
        if uploaded_file is not None:
            if "file_name" not in st.session_state or uploaded_file.name != st.session_state.get("file_name", ""):
                # Update stored file info
                st.session_state["file_name"] = uploaded_file.name
                st.session_state["uploaded_file"] = uploaded_file
                st.session_state["step"] = 1

    # === Show Data ===
    if "uploaded_file" in st.session_state:

        uploaded_file = st.session_state["uploaded_file"]
        
        try:
            # === Detect file type and read accordingly ===
            if "file_name" not in st.session_state:
                st.session_state["file_name"] = uploaded_file.name

            # === CSV Files ===
            if st.session_state["file_name"].endswith(".csv"):
                dataset = pd.read_csv(uploaded_file)

            # === Excel Files ===
            elif st.session_state["file_name"].endswith(".xlsx"):
                dataset = pd.read_excel(uploaded_file, engine = "openpyxl")

            # === Unknown File Type ===
            else:
                with st.sidebar:
                    st.error("Unsupported file format. Please upload a CSV or Excel file.")
                    return
            
            # === If correct Data Format ===
            with st.sidebar:
                st.success("✅ File uploaded and loaded successfully!")

            st.subheader("Preview of Uploaded Data:")
            st.dataframe(dataset.head())

            # === Get Column Selection ===
            st.markdown("---")
            st.subheader("🎯 Select Columns for Clustering:")

            # === Extracting Column Names ===
            try:
                all_columns = dataset.columns.tolist()

            except Exception as e:
                st.error("Not able to extract the column names")

            # === Giving the user option to select the columns ===
            selected_columns = st.multiselect(label = "Select the name of the columns you want to use:",
                                              options = all_columns,
                                              default = None)

            if selected_columns:
                st.success(f"List of the selected columns: {selected_columns}")
            else:
                st.warning("⚠️ Please select at least one column to continue.")

            # === Save selection ===
            st.session_state["selected_columns"] = selected_columns

            # === Show "Proceed to Apply Weightage" Button ===
            if st.button("Proceed to Apply Weightage") and selected_columns:
                st.session_state["step"] = 2

            # === Weightage ===
            if st.session_state.get("step", 1) >= 2 and selected_columns:
                st.markdown("---")
                st.subheader("⚖️ Do You Want to Apply Weightage to Selected Features?")

                # === Explanation ===
                with st.expander("💡 Why use weightage?"):
                    st.markdown("""
                    In K-Means clustering, features are usually **equally weighted** after scaling.  
                    But in real-world cases, some features might be **more important** than others.

                    For example:
                    - A retail company may care more about `Spending Score` than `Age`
                    - An insurance company may prioritize `Income` over `Gender`

                    Use this option to assign **relative importance** to each feature before clustering.
                    """)

                # === Checkbox toggle ===
                apply_weights = st.checkbox("Yes, I want to assign custom weightage",
                                            value = False)

                if apply_weights:

                    # Dictionary to store user-assigned weights
                    feature_weights = {}

                    for col in selected_columns:
                        weight = st.slider(
                            f"🔧 Weight for '{col}'",
                            min_value = 0.1,
                            max_value = 5.0,
                            value = 1.0,
                            step = 0.1
                        )
                        feature_weights[col] = weight

                    st.session_state["feature_weights"] = feature_weights

                    # === Preview the weights ===
                    st.success("✅ Feature weights set:")
                    st.json(feature_weights)

                else:
                    # === If not applying weights, default to 1.0 ===
                    st.session_state["feature_weights"] = {col: 1.0 for col in selected_columns}
                    st.info("All features will be treated equally (weight = 1.0).")

            # === Show "Proceed to Clustering" Button ===
            if st.button("Proceed to Clustering"):
                st.session_state["step"] = 3

            if st.session_state.get("step", 1) >= 3:
                st.markdown("---")
                st.subheader("📏 Step 3: Feature Scaling (with Weightage)")

        except Exception as e:
            st.error(f"❌ Error reading file: {e}")

    else:
        st.info("👈 Please upload a CSV file to get started.")

if __name__ == "__main__":
    main()