
def detect_bad_words(paragraph, bad_words):
    paragraph = paragraph.lower()
    bad_words = [word.strip().lower() for word in bad_words]
    for word in bad_words:
        if word in paragraph:
            return True
    return False