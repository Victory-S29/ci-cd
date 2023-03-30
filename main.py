def word_counter(words):
    """return dictionary with 10 most common words"""
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10])
    return word_counts

def find_top_words(word_counts):
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_words = dict(sorted_word_counts[:10])
    return top_words
