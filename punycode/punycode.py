import idna

def convert(input_text:str, ascii_only=False):
    if not isinstance(input_text, str):
        raise ValueError("Input must be string.")
    if (input_text[:4] == "xn--") | (".xn--" in input_text):
        if ascii_only:
            output_text = idna.encode(input_text).decode('utf-8')
        else:
            output_text = idna.decode(input_text)
    else:
        output_text = idna.encode(input_text).decode('utf-8')
    return output_text