from translate import Translator


class TranslateTextEncode:
    CATEGORY = "epub"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":
                {
                    "source": (["zh", "en"],),
                    "to": (["en", "zh"],),
                    "text": ("STRING", {"multiline": True}),
                }
        }

    FUNCTION = "translate_text"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)

    @staticmethod
    def translate_text(source, to, text):
        return (Translator(from_lang=source, to_lang=to).translate(text),)


NODE_CLASS_MAPPINGS = {
    "TranslateTextEncode": TranslateTextEncode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TranslateTextEncode": "TranslateTextEncode"
}
