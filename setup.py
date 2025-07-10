import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Ai-Powered-Customer-Segmentation"
AUTHOR_USER_NAME = "RawatRahul14"
SRC_REPO = "clusterProject"
AUTHOR_EMAIL = "rahulrawat272chd@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "An interactive Streamlit app for clustering customer data using KMeans with optional LLM-based segment naming.",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)