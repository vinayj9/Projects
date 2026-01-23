import text_utils as textprocessing
import search_utils as search
import read_file as read

def display_results(analysis):
    print(f"\nTotal words: {analysis['total_words']}")
    print(f"Unique words: {analysis['unique_words']}")
    print(f"Total sentences: {analysis['sentence_count']}")
    print(f"Average word length: {analysis['avg_word_length']:.2f}")
    print(f"Average words per sentence: {analysis['avg_words_per_sentence']:.2f}")
    print(f"Longest word: {analysis['longest_word']}")
    print(f"Shortest word (>=3 chars): {analysis['shortest_word']}")
    print("Most common words:")
    for word, count in analysis["top5"]:
        print(f"{word:<15}: {count}")
        
def main():
    print("Text Analyzer started!\n")
    while True:

        text = read.read_file()
        if text is None:
            print("Nothing to analyze.")
            return

        analysis = textprocessing.analyze_text(text)
        display_results(analysis)

        sentences = textprocessing.split_into_sentences(text)

        keyword = input("\nSearch for (press Enter to skip): ").strip()
        if keyword:
            search.search_keyword(sentences, keyword)
        a=input("Analyze another file?[Y/N]:").strip().upper()
        if a=="Y":
            continue
        elif a=="N":
            break
        else:
            print("Invalid input")
    
if __name__ == "__main__":
    main()    

