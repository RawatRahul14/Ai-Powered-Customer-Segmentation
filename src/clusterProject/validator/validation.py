# === Python Modules ===
from pydantic import BaseModel
from typing import List, Dict, Any, Optional, Literal

# === Validators ===

## === File Upload ===
class UploadResponse(BaseModel):
    session_id: Optional[str] = None
    status: Literal["success", "fail"] = "fail"
    file_name: Optional[str] = None
    columns: Optional[List[str]] = None
    rows: Optional[int] = None
    preview: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None
    whole_file: Optional[List[Dict[str, Any]]] = None

# === Columns ===
class ColumnResponse(BaseModel):
    filtered_columns: Optional[List[str]] = None
    error: Optional[str] = ""

class ScalingResponse(BaseModel):
    scaled: Optional[List[Dict[str, Any]]] = None
    error: Optional[str] = None