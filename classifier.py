import re

from rules import MESSAGE_TYPES

def classify_message(message: str):
    message_lower = message.lower()
    
    for category, keywords in MESSAGE_TYPES.items():
        for keyword in sorted(keywords, key=lambda x: -len(x)):
            
            pattern = r"\b" + re.escape(keyword) + r"\b"
            if re.search(pattern, message_lower):
                return category
    return "informational"
