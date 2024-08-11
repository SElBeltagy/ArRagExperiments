import re
def extract_text_llama(text):
    # Check if 'assistant' is present
    if 'assistant' in text:
        # Split the text by 'assistant'
        parts = text.split('assistant')

        # Check the number of 'assistant' occurrences
        if len(parts) >= 2:
            # Extract text between the first two 'assistant'
            extracted_text = parts[1].strip()
        else:
            # Extract all text after the first 'assistant'
            extracted_text = parts[1].strip() if len(parts) > 1 else ""

        return extracted_text.strip()
    else:
        # Use regex to find all sequences of English characters and numbers
        english_pattern = re.compile(r'[a-zA-Z0-9٠-٩\s]+')
        english_matches = list(english_pattern.finditer(text))

        if len(english_matches) >= 1:
            # Extract Arabic text from the first English sequence to the end
            start_index = english_matches[0].end()
            arabic_text = text[start_index:]

            # Use regex to find all sequences of Arabic characters and numbers within the extracted text
            arabic_pattern = re.compile(r'[\u0600-\u06FF0-9٠-٩\s]+')
            arabic_matches = list(set(arabic_pattern.findall(arabic_text)))

            return ''.join(arabic_matches).strip()