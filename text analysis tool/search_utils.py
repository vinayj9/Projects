import re

def search_keyword(sentences, keyword):
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    found = False

    for i, sentence in enumerate(sentences, start=1):
        if pattern.search(sentence):
            highlighted = pattern.sub(lambda m: f"[{m.group()}]", sentence)
            print(f"{i}. {highlighted}")
            found = True

    if not found:
        print("Not found!")
