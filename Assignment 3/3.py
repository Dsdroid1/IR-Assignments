import mathplotlib.pyplot as plt

def initInvertedIndex():
    dictionary = {}
    # Implementation used: Python dict to maintain the words and list as the posting list
    return dictionary

def histogramize(plaintext):
    pass

def indexDocument(doc, inverted_index):
    # Input: doc -> (id, plaintext) Plain text, cleaned of punctuations etc
    doc_id,plain_text = doc
    word_data = histogramize(plain_text)
    for word in plain_text.split(" "):
        if inverted_index.get(word) is not None:
            # 'word' was already present in the index, then update the posting list
            pass
        else:
            # Create a new posting list for this word
            inverted_index[word] = [()]
