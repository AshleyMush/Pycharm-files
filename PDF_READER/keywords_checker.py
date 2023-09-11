from fuzzywuzzy import fuzz

class KeywordChecker:
    #TODO ADJUJST THRESHOLD FOR MORE ACCURACY || THE HIGHER THE STRICTER
    def __init__(self, filepath, threshold=85):  # Setting default threshold to 85, you can adjust this
        self.filepath = filepath
        self.keywords = self.load_keywords()
        self.threshold = threshold

    def load_keywords(self):
        with open(self.filepath, 'r') as file:
            return [keyword.strip() for keyword in file.read().split(",")]

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


"""

class KeywordChecker:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keywords = self.load_keywords()

    def load_keywords(self):
        with open(self.filepath, 'r') as file:
            # Reads all keywords, strips whitespace and splits by commas
            return [keyword.strip() for keyword in file.read().split(",")]

    def check_keywords_in_text(self, text):
        found_keywords = [keyword for keyword in self.keywords if keyword in text]
        return found_keywords

    def has_keywords(self, text):
        return any(keyword in text for keyword in self.keywords)

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


"""


#
#
# class KeywordChecker:
#     def __init__(self, filepath, threshold=85):
#         self.filepath = filepath
#         self.keywords = self.load_keywords()
#         self.threshold = threshold
#
#     def load_keywords(self):
#         with open(self.filepath, 'r') as file:
#             # Reads all keywords, strips whitespace and splits by commas
#             return [keyword.strip() for keyword in file.read().split(",")]
#
#     def fuzzy_match(self, word, keyword):
#         return fuzz.ratio(word, keyword) >= self.threshold
#
#     def check_keywords_in_text(self, text):
#         found_keywords = [keyword for keyword in self.keywords if self.fuzzy_match(keyword, text)]
#         return found_keywords
#
#     def has_keywords(self, text):
#         return any(self.fuzzy_match(keyword, text) for keyword in self.keywords)
#
#     def keywords_found(self, notes):
#         keywords = set()  # We use a set to avoid duplicate keywords
#         lower_notes = notes.lower()  # Convert notes to lowercase for consistent matching
#
#         for keyword in self.keywords:
#             if self.fuzzy_match(lower_notes, keyword):
#                 keywords.add(keyword)
#
#         return list(keywords)






