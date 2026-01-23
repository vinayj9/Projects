from collections import Counter
import re
import string
def split_into_sentences(text):
    # 1)
    # sentences=re.split(r'[.!?]+', text)
    # for x in sentences:
    #     print(x)
    # 2)
    # temp=text.strip().replace('.','#').replace('!','#').replace('?','#')
    # result=temp.split('#')
    # result=[item for item in result if item]
    # print(result)
        result = re.findall(r'[^.!?]+(?:[.!?]+|$)', text)
        return [s.strip() for s in result if s.strip()]
def analyze_text(text, min_word_length=3):
    # Removing punctuations
    removal=str.maketrans("","",string.punctuation)
    cleantext=text.translate(removal)
    # Splitting into list of words
    words=[word.lower() for word in cleantext.split() if word.isalpha()]
    # Getting total count of occurences for a word
    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0)+1
    
    # Sentence stats
    sentences=split_into_sentences(text)
    sentence_count=len(sentences)
    words_per_sentence=[
        len([w for w in s.translate(removal).split() if w.isalpha()])
        for s in sentences
    ]
    avg_words_per_sentence = (
        sum(words_per_sentence) / sentence_count
        if sentence_count else 0
    )
    # Word stats
    # Computing avg word length
    avg_word_length=sum([len(word) for word in words]) / len(words) if words else 0
    longest_word = max(words, key=len) if words else None
    valid_short_words = [w for w in words if len(w) >= min_word_length]
    shortest_word = min(valid_short_words, key=len) if valid_short_words else None
    # Getting 5 most common words
    c=Counter(words)
    try:
        top=int(input("Number of Top Words:"))
        if top>len(set(words)):
            top=len(set(words))
    except ValueError:
        top=5
    top_w=c.most_common(top)
    return{
        "total_words": len(words),
        "unique_words": len(set(words)),
        "avg_word_length": avg_word_length,
        "sentence_count": sentence_count,
        "avg_words_per_sentence": avg_words_per_sentence,
        "longest_word": longest_word,
        "shortest_word": shortest_word,
        "top5": top_w,
    }
# analyze_text(text="Twenty-two years after the Jurassic Park disaster on Isla Nublar in 1993,[b] a new dinosaur theme park called Jurassic World has been built on the island, owned by Masrani Global Corporation in affiliation with InGen, which created the dinosaurs. Brothers Zach and Gray Mitchell visit the park, where their aunt Claire Dearing works as the operations manager. She assigns her assistant Zara to guide them, but they evade her and explore on their own. don't go 1980") 