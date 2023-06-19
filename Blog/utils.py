import re


def spam_check(text: str):
    spam_words = ["poker", "casino"]
    if re.search("(?P<url>https?://[^\s]+)", text) or re.search("(?P<domain>\w+\.\w{2,3})", text):
        return False
    for word in spam_words:
        if word in text.lower():
            return False
    return True
