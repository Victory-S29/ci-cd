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