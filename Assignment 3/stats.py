import time
import matplotlib.pyplot as plt
from index_creation import create_index
from search_functions import nextPhraseOverCorpus,next_term_binary,next_term_linear,next_term_galloping

def run_queries(query_file,inverted_index,next):
    with open(query_file,'r') as f:
        phrases = f.readlines()
        response_times = []
        for phrase in phrases:
            # print(f'Searching for :{phrase.strip()}')
            before = time.time()
            result = nextPhraseOverCorpus(inverted_index,phrase.strip().split(' '),next)
            # if result is None:
            #     print(phrase)
            after = time.time()
            response_times.append(((after-before)*1000,len(phrase.strip().split(" "))))
            # print("")
    return response_times

def get_average_response_times(response_times):
    aggregate = {}
    for time,length in response_times:
        # avg_time[length] = 0
        if aggregate.get(length) is not None:
            aggregate[length]['time'] += time
            aggregate[length]['count'] += 1
        else:
            aggregate[length] = {}
            aggregate[length]['time'] = time 
            aggregate[length]['count'] = 1
    avg_resp_time = []
    for length in aggregate.keys():
        avg_resp_time.append((length,aggregate[length]['time']/aggregate[length]['count']))
    avg_resp_time.sort(key=lambda x:x[0])
    return avg_resp_time

def longest_posting_list_data(inverted_index,next,query_file='queries_2.txt'):
    with open(query_file,'r') as f:
        phrases = f.readlines()
        response_times = []
        for phrase in phrases:
            # print(f'Searching for :{phrase.strip()}')
            before = time.time()
            result = nextPhraseOverCorpus(inverted_index,phrase.strip().split(' '),next)
            after = time.time()
            terms = phrase.strip().split(' ')
            longest_posting_list_len = max(inverted_index[terms[0]]['freq'],inverted_index[terms[1]]['freq'])
            response_times.append(((after-before)*1000,longest_posting_list_len))
            # print("")
    return get_average_response_times(response_times)


if __name__ == '__main__':
    inverted_index = create_index()
    mode = int(input('Enter 1 for len of query vs time, 2 for longest posting list vs time:'))
    if mode == 1:
        query_file = 'queries.txt'
        # run_queries(query_file, inverted_index,next_term_binary)
        # run_queries(query_file, inverted_index,next_term_linear)
        # run_queries(query_file, inverted_index,next_term_galloping)
        # print(get_average_response_times(run_queries(query_file, inverted_index,next_term_binary)))
        
        # Query length vs Time
        times_binary = get_average_response_times(run_queries(query_file,inverted_index,next_term_binary))
        # print(times_binary)
        times_linear = get_average_response_times(run_queries(query_file,inverted_index,next_term_linear))
        times_galloping = get_average_response_times(run_queries(query_file,inverted_index,next_term_galloping))

        # Get the lengths of the queries
        lengths_x = [l for (l,t) in times_binary]
        # print(lengths_x)
        time_b_y = [t for (l,t) in times_binary]
        # print(time_b_y)
        time_l_y = [t for (l,t) in times_linear]
        time_g_y = [t for (l,t) in times_galloping]

        # Plot all lines
        plt.plot(lengths_x,time_b_y,label = 'binary_next')
        plt.plot(lengths_x,time_l_y,label = 'linear_next')
        plt.plot(lengths_x,time_g_y,label = 'galloping_next')

        # naming the x axis
        plt.xlabel('Length of queries')
        # naming the y axis
        plt.ylabel('Average response times(in ms)')

        plt.title('Average Response Times vs Query Length')
        
        plt.legend()
        
        plt.show()
    else:
        # posting list len vs time
        query_file = 'queries_2.txt'
        times_binary = longest_posting_list_data(inverted_index,next_term_binary,query_file)
        times_linear = longest_posting_list_data(inverted_index,next_term_linear,query_file)
        times_galloping = longest_posting_list_data(inverted_index,next_term_galloping,query_file)

        # Get the lengths of the queries
        lengths_x = [l for (l,t) in times_binary]
        # print(lengths_x)
        time_b_y = [t for (l,t) in times_binary]
        # print(time_b_y)
        time_l_y = [t for (l,t) in times_linear]
        time_g_y = [t for (l,t) in times_galloping]

        # Plot all lines
        plt.plot(lengths_x,time_b_y,label = 'binary_next')
        plt.plot(lengths_x,time_l_y,label = 'linear_next')
        plt.plot(lengths_x,time_g_y,label = 'galloping_next')

        # naming the x axis
        plt.xlabel('Length of posting lists')
        # naming the y axis
        plt.ylabel('Average response times(in ms)')

        plt.title('Average Response Times vs Longest posting list Length')
        
        plt.legend()
        
        plt.show()