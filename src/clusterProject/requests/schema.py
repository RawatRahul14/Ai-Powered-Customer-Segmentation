# === Pyuthon Modules ===
from pydantic import BaseModel
from typing import List

# === Schema for Column request ===
class ColumnRequest(BaseModel):
    index_column_name: str
    all_columns: List[str]