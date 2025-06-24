from typing import List
from pydantic import BaseModel

class TranslateRequest(BaseModel):
    lines: List[str]
    from_lang: str = "zh-CN"
    to_lang: str = "en-US"