import re

def extract_arabic_mixtral(text):
    # Check if 'assistant' is in the text
    if 'assistant' in text:
        # Split by 'assistant'
        parts = text.split('assistant')

        # Check the number of 'assistant' occurrences
        if len(parts) > 2:
            # Extract text between the first two 'assistants'
            extracted_text = parts[1].strip() + ' ' + parts[2].strip()
        elif len(parts) == 2:
            # Extract text after the first 'assistant'
            extracted_text = parts[1].strip()
        else:
            # No 'assistant' found, return an empty string
            extracted_text = ""
    else:
        # Find all occurrences of 'SystemMessage(content='
        parts = text.split("SystemMessage(content=")

        if len(parts) > 1:
            # Take the last part after the last 'SystemMessage(content='
            last_part = parts[-1]
            # Extract text before the first 'HumanMessage(content='
            extracted_text = last_part.split("HumanMessage(content=")[0]
        else:
            # No 'SystemMessage(content=' found, return empty string
            extracted_text = ""

    # Remove non-Arabic characters but keep Arabic and standard numerals
    arabic_text = re.sub(r'[^\u0600-\u06FF0-9٠-٩\s]', '', extracted_text)

    # Return the extracted Arabic text
    return arabic_text.strip()