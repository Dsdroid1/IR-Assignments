import os
import re

def initInvertedIndex():
    dictionary = {}
    # Implementation used: Python dict to maintain the words and list as the posting list
    return dictionary

def clean_text(text):
    return re.sub(r'[^\w\s]','',text)

def indexDocument(doc, inverted_index):
    # Input: doc -> (id, plaintext) Plain text, cleaned of punctuations etc
    doc_id,plain_text = doc
    for i,word in enumerate(plain_text.split(" ")):
        if inverted_index.get(word) is not None:
            # 'word' was already present in the index, then update the posting list
            if inverted_index[word].get(doc_id) is not None:
                inverted_index[word][doc_id].append(i+1)
            else:
                inverted_index[word][doc_id] = [i+1]
            inverted_index[word]['freq'] += 1 
        else:
            # Create a new posting list for this word
            inverted_index[word] = {}
            inverted_index[word][doc_id] = [i+1]
            inverted_index[word]['freq'] = 1


def create_index():
    dataset_loc = os.path.join('.','dataset','Int-Txt')
    files = os.listdir(dataset_loc)
    # print(files)
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    doc_id = 1
    inverted_index = initInvertedIndex()
    for file in files:
        with open(os.path.join(dataset_loc,file),'r') as f:
            lines = f.readlines()
            # Clean up the document 
            data = ""
            for line in lines:
                line = line.strip()
                line = line.lower()
                line = re.sub(r'[^\w\s]','',line)
                data += (line + " ")
            # print(data)
            doc = (doc_id,data)
            doc_id += 1
            indexDocument(doc,inverted_index)
            # print(inverted_index)
    # print(inverted_index['intermediate'])
    return inverted_index



if __name__ == '__main__':
    inverted_index = create_index()