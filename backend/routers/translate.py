from pypinyin import lazy_pinyin, Style
import epitran
from PersianG2p import Persian_g2p_converter
from deep_translator import GoogleTranslator, MyMemoryTranslator


from fastapi import APIRouter
from googletrans import Translator
from models.request import TranslateRequest

router = APIRouter()
translator = Translator()
epi_fa = epitran.Epitran('fas-Arab')
PersianG2Pconverter = Persian_g2p_converter()


def get_transliteration(text: str, lang: str) -> str:
    try:
        if lang == "zh-CN":
            return " ".join(lazy_pinyin(text, style=Style.TONE3))
        elif lang == "fa-IR":
            return PersianG2Pconverter.transliterate(text, secret = True).replace("č", "ch").replace("š", "sh").replace("ž", "zh").replace("x", "kh")
        else:
            return ""
    except Exception as e:
        print(f"Transliteration failed for '{text}' in {lang}: {e}")
        return ""

@router.post("/translate")
async def translate(req: TranslateRequest):
    translated = []
    transliterated = []

    for line in req.lines:
        if not line.strip():
            translated.append("")
            transliterated.append("")
            continue
        # result = translator.translate(line, src=req.from_lang, dest=req.to_lang)
        result = MyMemoryTranslator(source= req.from_lang, target='en-US').translate(line)
        translated.append(result)
        transliterated.append(get_transliteration(line, req.from_lang))

    return {
        "translated": translated,
        "transliterated": transliterated
    }
