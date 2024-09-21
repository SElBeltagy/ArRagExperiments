def extract_arabic_jais(text):
    # Check for "الجواب" scenario
    keyword = " :الجواب"
    keyword_index = text.find(keyword)
    if keyword_index != -1:
        start_index = keyword_index + len(keyword)
        return text[start_index:].strip()

    # Check for "AI:" scenario
    start_keyword = "AI:"
    start_index = text.find(start_keyword)
    if start_index != -1:
        start_index += len(start_keyword)
        remaining_text = text[start_index:]
        # Regex to find the start of English text
        end_match = re.search(r'[a-zA-Z]', remaining_text)
        if end_match:
            end_index = end_match.start()
            return remaining_text[:end_index].strip()
        return remaining_text.strip()