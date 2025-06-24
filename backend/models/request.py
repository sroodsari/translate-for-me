from pydantic import BaseModel
from typing import List

class TranslateRequest(BaseModel):
    lines: List[str]
    from_lang: str = "zh-CN"
    to_lang: str = "en-US"
