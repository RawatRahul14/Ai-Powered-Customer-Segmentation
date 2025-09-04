# === Pyuthon Modules ===
from pydantic import BaseModel
from typing import List, Dict

# === Schema for Column request ===
class ColumnRequest(BaseModel):
    index_column_name: str
    all_columns: List[str]

class ScaledRequest(BaseModel):
    selected_columns: List[str]
    scaling_option: str
    feature_weights: Dict[str, float]
    file_name: str
    index_column: str