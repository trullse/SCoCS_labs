FILE_DIRECTORY = "test_text.txt"

SENTENCE_TEMPLATE = r"(\.|\.\.\.|!|\?)[\s\"']"
ABBREVIATIONS = ("Mr.", "Mrs.", "Dr.", "Lt.", "Rep.", "Jan.", "Feb.", "Mar.", "Apr.", "B.A.", "Ph.D.",
                 "Jun.", "Jul.", "Aug.", "Sep.", "Sept.", "Oct.", "Nov.", "Dec.", "Mon.", "Tu.", "Tue.",
                 "Tues.", "Wed.", "Th.", "Thu.", "Thur.", "Thur.", "Thurs.", "Fri.", "Sat.", "Sun.",
                 "in.", "lbs.")
END_ABBREVIATIONS = r"(etc\.|e\.g\.|i\.e\.)\s+[^A-Z]"
INITIALS_TEMPLATE = r"[A-Z]\.\s"
NON_DECLARATIVE_TEMPLATE = r"!|\?[\s\"']"
WORD_TEMPLATE = r"\b\w+\b"
NUMBER_TEMPLATE = r"\b\d[\d\.]*\b"
