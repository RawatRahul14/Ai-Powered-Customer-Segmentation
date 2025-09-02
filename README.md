# 📊 AI-Powered-Customer-Segmentation

![Python](https://img.shields.io/badge/python-3.9%2B-blue)  ![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)  ![Streamlit(https://img.shields.io/badge/Streamlit-1.30+-brightgreen)]  ![Redis](https://img.shields.io/badge/Redis-7.0+-red)  ![scikit--learn](https://img.shields.io/badge/scikit--learn-1.3+-orange)  ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)  

An end-to-end AI-driven customer segmentation system built with FastAPI, Streamlit, and Redis. The project allows users to upload datasets, preview them, select features, run clustering algorithms such as K-Means, and visualize the results interactively. The backend is designed in a modular and production-ready way with FastAPI, making it easy to integrate directly into a React frontend or any other modern UI framework.

## 🚀 Features

- 📂 Secure File Uploads (FastAPI backend with session management)
- 🗂️ Dataset Preview (columns, rows, sample data)
- 🔑 Index Column Selection for structured analysis
- 🔍 Feature Selection for clustering
- 🤖 AI-Powered Clustering (K-Means, PCA-based visualization)
- 📈 Interactive Visualizations (Streamlit frontend)
- ⚡ In-memory Storage with Redis for fast session handling
- 🔐 Temporary Data (auto-cleared after session end)

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Database/Cache**: Redis
- **Data Processing**: Pandas, Scikit-learn
- **Visualization**: Matplotlib, Seaborn

## 📂 Project Structure
```
Directory structure:
└── rawatrahul14-ai-powered-customer-segmentation/
    ├── README.md
    ├── app.py
    ├── LICENSE
    ├── main.py
    ├── requirements.txt
    ├── setup.py
    ├── template.py
    ├── data/
    │   └── data.xlsx
    ├── research/
    │   └── trials.ipynb
    ├── src/
    │   └── clusterProject/
    │       ├── __init__.py
    │       ├── components/
    │       │   ├── __init__.py
    │       │   ├── columns.py
    │       │   └── sidebar.py
    │       ├── pipeline/
    │       │   └── __init__.py
    │       ├── requests/
    │       │   ├── __init__.py
    │       │   └── schema.py
    │       ├── utils/
    │       │   ├── __init__.py
    │       │   └── common.py
    │       └── validator/
    │           ├── __init__.py
    │           └── validation.py
    └── uploads/
        └── data.xlsx
```

## ⚡ Installation & Setup

1️⃣ Clone the Repository:
```bash
git clone https://github.com/RawatRahul14/Ai-Powered-Customer-Segmentation.git
cd Ai-Powered-Customer-Segmentation
```

2️⃣ Create Virtual Environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3️⃣ Install Dependencies:
```bash
pip install -r requirements.txt
```

4️⃣ Configure Environment:
Create a .env file in the root folder:
```env
# === Redis Info ===
redis_username: str = ""
redis_host: str = ""
redis_password: str = ""
redis_port: int = 0000
```

5️⃣ Run Backend (FastAPI):
```bash
uvicorn backend.main:app --reload
```

6️⃣ Run Frontend (Streamlit):
```bash
streamlit run frontend/app.py
```

## 🖼️ Usage Flow

1. Upload a CSV dataset.
2. Preview dataset & metadata (rows, columns, sample).
3. Select index column & clustering features.
4. Run clustering → K-Means groups customers into segments.
5. Visualize clusters with interactive plots.

## 📊 Example Output
- Clustered scatter plots (PCA reduced)
- Segment summaries
- Customer group statistics

## 🧩 Future Improvements

- ✅ Add DB persistence (MongoDB/Postgres for long-term storage)
- ✅ Support multiple clustering algorithms (DBSCAN, Hierarchical)
- ✅ Add auth system for multi-user access
- ✅ Deploy on AWS/GCP with Docker

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## 👨‍💻 Author

Rahul Rawat  
[🔗 LinkedIn](https://www.linkedin.com/in/rahul148) | [🌐 Portfolio](https://www.rawatrahul.com)