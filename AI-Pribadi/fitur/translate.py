from langchain_core.tools import tool

@tool
def translate(text: str, target_lang: str = "en") -> str:
    """Menerjemahkan teks ke bahasa lain. Gunakan target_lang seperti: en, id, ja, etc."""
    from deep_translator import GoogleTranslator
    try:
        result = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return result
    except Exception as e:
        return f"Error saat menerjemahkan: {str(e)}"
