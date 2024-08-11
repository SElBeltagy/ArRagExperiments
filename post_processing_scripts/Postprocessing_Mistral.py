import re
def extract_arabic_mistral(text):
    # Define patterns for Arabic responses and messages
    response_patterns = [
        r'\s*Arabic\s*response\s*\d*:\s*(.*?)(?=\n\n|$)',    
        r'ArabicMessage\(content=\'(.*?)\'\)',                         

    ]
    
    extracted_text = ""
    # Try to find the first matching response
    for pattern in response_patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            extracted_text = match.group(1).strip()
            break

    # If no specific response is found, return the original text stripped
    if not extracted_text:
        return text.strip()

    # Define a regular expression to match Arabic text and keep numerals (Arabic and English)
    arabic_pattern = re.compile(r'[\u0600-\u06FF0-9٠-٩]+')
    
    # Find all Arabic text segments in the extracted text
    arabic_matches = arabic_pattern.findall(extracted_text)
    
    # Join the Arabic text segments into a single string
    arabic_text = ' '.join(arabic_matches).strip()
    
    # If the length of the Arabic text is less than or equal to 20 characters, use the entire text
    if len(arabic_text) <= 20:
        arabic_text = extracted_text.replace('\n\n', ' ').replace('\n', ' ').strip()
    
    return arabic_text