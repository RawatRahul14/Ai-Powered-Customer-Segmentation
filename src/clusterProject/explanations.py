intro = """
    👋 Welcome to the **Interactive Customer Segmentation App**!  

    Upload your **CSV or Excel** file, select the features you'd like to analyze, and let the app:  
    - 📊 Apply **K-Means clustering**  
    - 🧠 Use AI to automatically **name and describe segments**  
    - 🎯 Reveal meaningful **customer personas** to guide your decisions  

    ---
    """

weightage = """
    ⚖️ In standard K-Means clustering, all features are treated with **equal weight** after scaling.  
    However, in practice, some features may play a **bigger role** in defining customer behavior.  

    **Examples:**  
    - A retail brand may emphasize **Spending Score** more than **Age**  
    - An insurance provider might prioritize **Income** over **Gender**  

    👉 Use this option to assign **relative importance** to each feature before clustering.  
    """

scaler_md = """
    🔧 **Choose a scaling method** (applied before clustering):  

    - **StandardScaler:** Standardizes features by removing the mean and scaling to unit variance.  
        ✅ Best for data that follows a normal distribution.  

    - **MinMaxScaler:** Transforms features to a fixed range, usually [0, 1].  
        ✅ Useful when features have very different scales.  

    - **RobustScaler:** Uses the median and interquartile range (IQR) for scaling.  
        ✅ More resilient when data contains **outliers**.  
    """