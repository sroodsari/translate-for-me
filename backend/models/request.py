from pydantic import BaseModel
from typing import List

class TranslateRequest(BaseModel):
    lines: List[str]
    from_lang: str = "zh-cn"
    to_lang: str = "en"
