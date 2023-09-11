from fuzzywuzzy import fuzz
import random

class KeywordChecker:
    def __init__(self, filepath, threshold=85):  # Setting default threshold to 85, you can adjust this
        self.filepath = filepath
        self.keywords = self.load_keywords()
        self.threshold = threshold

    def load_keywords(self):
        with open(self.filepath, 'r') as file:
            keywords = [keyword.strip() for keyword in file.read().split(",")]
            # Add misspellings for each keyword
            for keyword in keywords[:]:
                keywords.extend(generate_misspellings(keyword))
            return keywords

    def fuzzy_match(self, word):
        for keyword in self.keywords:
            if fuzz.ratio(word, keyword) >= self.threshold:
                return keyword
        return None

    def check_keywords_in_text(self, text):
        words = text.split()  # Split the text into words
        found_keywords = set()  # Use a set to avoid duplicates
        for word in words:
            match = self.fuzzy_match(word)
            if match:
                found_keywords.add(match)
        return list(found_keywords)

    def has_keywords(self, text):
        return any(self.fuzzy_match(word) for word in text.split())

    def keywords_found(self, notes):
        keywords = set()  # We use a set to avoid duplicate keywords
        lower_notes = notes.lower()  # Convert notes to lowercase once to optimize
        for keyword in self.keywords:
            if keyword in lower_notes:  # You're already converting keywords to lowercase in load_keywords
                keywords.add(keyword)
        return list(keywords)

    def replace_keywords_with_emoji(self, notes):
        lower_notes = notes.lower()
        for keyword in self.keywords:
            if keyword in lower_notes:
                notes = notes.replace(keyword, f"💥⛔❗👉 {keyword}")
        return notes

def generate_misspellings(word):
    if len(word) <= 3:
        return []

    # Some common misspelling patterns
    patterns = [
        (lambda w: w[:-1], 0.2),  # drop the last character
        (lambda w: w + w[-1], 0.2),  # duplicate the last character
        (lambda w: w[1:] + w[0], 0.1),  # move the first character to the end
        (lambda w: w[:-1] + w[-2], 0.1),  # duplicate the second last character
        (lambda w: w[0] + w[2] + w[1] + w[3:], 0.3)  # swap two adjacent characters
    ]

    misspellings = set()
    for pattern, prob in patterns:
        if random.random() < prob:
            misspellings.add(pattern(word))

    return list(misspellings)
