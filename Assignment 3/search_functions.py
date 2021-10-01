from index_creation import create_index,clean_text

def binary_search(posting_list, prev_position, lo, hi):
    # lo = 0
    # hi = len(posting_list)-1
    if prev_position == 'inf':
        return 'inf'
    while lo<=hi:
        mid = int((lo + hi)/2)
        if posting_list[mid] == prev_position:
            if mid == len(posting_list)-1:
                return 'inf'
            else:
                return posting_list[mid+1]
        elif posting_list[mid] < prev_position:
            lo = mid + 1
        else:
            hi = mid - 1
    if lo == len(posting_list) :
        return 'inf'
    return posting_list[hi+1]

def linear_search(posting_list, prev_position):
    # Get the next value of position
    if prev_position == 'inf':
        return 'inf'
    i = 0
    L = len(posting_list)
    while i<L:
        if posting_list[i] <= prev_position:
            i += 1
        else:
            return posting_list[i]
    return 'inf'

def galloping_search(posting_list, prev_position):
    if prev_position == 'inf':
        return 'inf'
    search_length = 1
    search_start = 0
    if posting_list[search_start] > prev_position:
        return posting_list[search_start]
    if len(posting_list)>1:
        while posting_list[search_start+search_length] < prev_position:
            search_start += search_length
            if search_start >= len(posting_list):
                return 'inf'
            search_length *= 2
            if search_start+search_length >= len(posting_list)-1:
                search_length = len(posting_list) - search_start - 1
                break
        return binary_search(posting_list, prev_position, search_start, search_start+search_length)
    else:
        return 'inf'

def next_term_binary(index, doc_id, term, position):
    if index.get(term) is not None:
        if index[term].get(doc_id) is not None:
            return binary_search(index[term][doc_id],position,0,len(index[term][doc_id])-1)
        else:
            return 'inf'
    else:
        return 'inf'

def next_term_linear(index, doc_id, term, position):
    if index.get(term) is not None and index[term].get(doc_id) is not None:
        return linear_search(index[term][doc_id], position)
    else:
        return 'inf'

def next_term_galloping(index, doc_id, term, position):
    if index.get(term) is not None and index[term].get(doc_id) is not None:
        return galloping_search(index[term][doc_id], position)
    else:
        return 'inf'

def nextPhrase(index,terms,position,doc_id,next):
    # print(position)
    # print(f'{terms[0]}-{index[terms[0]][doc_id]}')
    u = next(index,doc_id,terms[0],position)
    # print(index[terms[0]][doc_id][-1])
    n = len(terms)
    v = u
    # print(u)
    for term in terms[1:]:
        # print(f'{term}-{index[term][doc_id]}')
        v = next(index,doc_id,term,v)
        # print(v)
    if v == 'inf':
        return ['inf','inf']
    # print(v)
    if v-u == n-1:
        return [u,v]
    else:
        return nextPhrase(index,terms,v-n,doc_id,next)

def nextPhraseOverCorpus(index, terms, next,verbose=False):
    # Get the list of all docs that contain all of the required terms
    docs = set(index[terms[0]].keys())-set(['freq'])
    # print(docs)
    count_matched = 0
    for term in terms:
        if index.get(term) is not None:
            docs = docs.intersection(set(index[term].keys()))
        else:
            if verbose:
                print('One of the terms is not in corpus, phrase cant be found')
            return None
    # print(docs)
    found = False
    for doc_id in docs:
        # Search using nextPhrase
        result = nextPhrase(index,terms,0,doc_id,next)
        if set(result) != set(['inf','inf']):
            found = True 
            count_matched += 1
            if verbose:
                print(f'Phrase found in documnet with id: {doc_id}, at positions ({result[0]},{result[1]})')

    if found == False and verbose:
        print('Phrase not found in corpus')
    return count_matched

if __name__ == '__main__':
    # inverted_index = create_index()
    # print(inverted_index['hello'])
    # pl = [2,3,6,9]
    # print(pl)
    # pos = int(input('Enter pos:'))
    # print(galloping_search(pl,pos))
    # doc_id = 1
    # # phrase = "the differences between commercial"
    # phrase  = "been there have"
    # terms = list(phrase.lower().split(" "))
    # index = create_index()
    # # print(index['there'][1])
    # # print(index['have'][1])
    # print(nextPhrase(index,terms,0,doc_id,next_term_binary))
    # print(nextPhrase(index,terms,0,doc_id,next_term_linear))
    # print(nextPhrase(index,terms,0,doc_id,next_term_galloping))
    index = create_index()
    phrase = input('Enter the phrase to search the corpus for:')
    phrase = clean_text(phrase)
    terms = phrase.strip().split(' ')
    nextPhraseOverCorpus(index,terms,next_term_binary)

