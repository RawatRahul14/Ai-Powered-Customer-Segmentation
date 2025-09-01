# === Python Packages ===
from fastapi import FastAPI, UploadFile, File
from typing import Dict, Any
import pandas as pd
import io, os
import redis
from dotenv import load_dotenv

# === Custom Modules ===
from clusterProject.utils.common import (
    create_uuid
)
from clusterProject.validator.validation import (
    UploadResponse,
    ColumnResponse
)

# === Schema ===
from clusterProject.requests.schema import ColumnRequest

# === FastAPI Connection ===
app = FastAPI()

# === Config Flags ===
LOAD_ENV = True
USE_S3 = False

# === Loading env keys ===
if LOAD_ENV:
    load_dotenv()
    redis_username = os.getenv("redis_username")
    redis_host = os.getenv("redis_host")
    redis_password = os.getenv("redis_password")
    redis_port = os.getenv("redis_port")

# === Redis Connection ===
r = redis.Redis(
    host = str(redis_host),
    port = int(redis_port),
    decode_responses = True,
    username = str(redis_username),
    password = str(redis_password)
)

# === Local Dev ===
if not USE_S3:
    UPLOAD_DIR: str = "uploads"
    os.makedirs(
        UPLOAD_DIR,
        exist_ok = True
    )

@app.post("/upload", response_model = UploadResponse)
async def upload_file(
    file: UploadFile = File(...)
):
    """
    Uploads the file from frontend to backend
    """
    try:
        # === Reading the Content ===
        contents = await file.read()

        # === Saving file either on local or s3 ===
        if not USE_S3:
            ## === Making the Path ===
            file_path = os.path.join(
                UPLOAD_DIR,
                file.filename
            )

            ## === Saving the Content ===
            with open(file_path, "wb") as f:
                f.write(contents)

            ## === Loading into Pandas ===
            if file.filename.endswith(".csv"):
                dataset: pd.DataFrame = pd.read_csv(io.BytesIO(contents))

            elif file.filename.endswith(".xlsx"):
                dataset: pd.DataFrame = pd.read_excel(io.BytesIO(contents))

        # === Getting the Unique ID ===
        session_id: str = create_uuid()

        # === Saving the session on Redis ===
        r.set(
            session_id,
            1,
            ex = 1800
        )

        return UploadResponse(
            session_id = session_id,
            file_name = file.filename,
            columns = dataset.columns.tolist(),
            rows = len(dataset),
            preview = dataset.head(5).to_dict(orient = "records"),
            status = "success",
            whole_file = dataset.to_dict(orient = "records")
        )
    except Exception as e:
        return UploadResponse(
            session_id = None,
            status = "fail",
            error = str(e)
        )

@app.post("/columns", response_model = ColumnResponse)
def get_filtered_columns(
    payload: ColumnRequest
):
    """
    Removes the name of the column from the whole list
    """
    try:
        """
        Using a for loop to remove the index column name
        """
        filtered = [c for c in payload.all_columns if c != payload.index_column_name]

        # === Returning the List of all the columns ===
        return ColumnResponse(
            filtered_columns = filtered
        )

    # === Returning the error string ===
    except Exception as e:
        return ColumnResponse(
            error = str(e)
        )