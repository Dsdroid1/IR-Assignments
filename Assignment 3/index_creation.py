import os
import re
import random

def initInvertedIndex():
    dictionary = {}
    # Implementation used: Python dict to maintain the words and list as the posting list
    return dictionary

def clean_text(text):
    return re.sub(r'[^\w\s]','',text)

def indexDocument(doc, inverted_index):
    # Input: doc -> (id, plaintext) Plain text, cleaned of punctuations etc
    doc_id,plain_text = doc
    for i,word in enumerate(plain_text):
        word = word.strip()
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
            data = data.strip().split(" ")
            data = [w for w in data if w!=""]
            doc = (doc_id,data)
            doc_id += 1
            indexDocument(doc,inverted_index)
            # print(inverted_index)
    # print(inverted_index['intermediate'])
    return inverted_index

def generate_phrases():
    dataset_loc = os.path.join('.','dataset','Int-Txt')
    files = os.listdir(dataset_loc)
    num_docs = len(files)
    phrases_generated = []
    max_phrase_length = 15
    min_phrase_length = 2
    max_phrases_required = 10000
    # DEBUGS
    lens =set()
    while len(phrases_generated) < max_phrases_required:
        # Choose a file for phrase gen
        f_index = random.randint(1,num_docs)
        with open(os.path.join(dataset_loc,files[f_index-1])) as f:
            lines = f.readlines()
            # Clean up the document 
            data = ""
            for line in lines:
                line = line.strip()
                line = line.lower()
                line = re.sub(r'[^\w\s]','',line)
                data += (line + " ")
            # Now pick up some random phrase
            data = data.strip().split(" ")
            data = [w for w in data if w!=""]
            data_len = len(data)
            start = random.randint(0, max(0,data_len-max_phrase_length-1))
            len_taken = random.randint(min_phrase_length,max_phrase_length)
            end = min(data_len-1, start+len_taken-1)
            lens.add(end-start+1)
            # end = random.randint(start+min_phrase_length+1, min(start+max_phrase_length+1, data_len))
            phrase = " ".join(data[start:end+1])
            if len(" ".join(data[start:end+1]).strip().split(" ")) == 1:
                print(phrase)
                print(data[start:end+1])
                print(files[f_index-1])
            phrases_generated.append(phrase.strip())
    print(lens)
    with open('queries.txt','w') as f:
        for phrase in phrases_generated:
            f.write(phrase+'\n')
            

def phrases_len_2():
    dataset_loc = os.path.join('.','dataset','Int-Txt')
    files = os.listdir(dataset_loc)
    num_docs = len(files)
    phrases_generated = []
    phrase_len = 2
    max_phrases_required = 1000
    # DEBUGS
    lens =set()
    while len(phrases_generated) < max_phrases_required:
        # Choose a file for phrase gen
        f_index = random.randint(1,num_docs)
        with open(os.path.join(dataset_loc,files[f_index-1])) as f:
            lines = f.readlines()
            # Clean up the document 
            data = ""
            for line in lines:
                line = line.strip()
                line = line.lower()
                line = re.sub(r'[^\w\s]','',line)
                data += (line + " ")
            # Now pick up some random phrase
            data = data.strip().split(" ")
            data = [w for w in data if w!=""]
            data_len = len(data)
            start = random.randint(0, max(0,data_len-2-1))
            len_taken = phrase_len
            end = min(data_len-1, start+len_taken-1)
            lens.add(end-start+1)
            # end = random.randint(start+min_phrase_length+1, min(start+max_phrase_length+1, data_len))
            phrase = " ".join(data[start:end+1])
            if len(" ".join(data[start:end+1]).strip().split(" ")) == 1:
                print(phrase)
                print(data[start:end+1])
                print(files[f_index-1])
            phrases_generated.append(phrase.strip())
    print(lens)
    with open('queries_2.txt','w') as f:
        for phrase in phrases_generated:
            f.write(phrase+'\n')

if __name__ == '__main__':
    # inverted_index = create_index()
    generate_phrases()
    phrases_len_2()