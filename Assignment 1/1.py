from node import Node

def get_all_terms(filename):
    # Function to get all the terms in the dictionary and sort them lexicographically
    with open(filename, 'r') as file:
        dictionary = {}
        lines = file.readlines()
        for line in lines:
            for term in line.strip().split():
                term = term.lower()
                if dictionary.get(term) is not None:
                    dictionary[term] +=1 # Increase the frequency
                else:
                    dictionary[term] = 1 # First time seeing this term
        # Create a list of tuples to be sorted lexicographically
        terms = [(term, frequency) for (term, frequency) in dictionary.items()] 
        terms.sort(key = lambda x: x[0])
        return terms

def freq_sum(terms,i,j):
    # Get the sum of all frequency terms from i to j
    sum = 0
    for k in range(i,j+1):
        sum += terms[k][1]
    return sum

def make_tree(dp,i,j,terms):
    get_best_root = dp[i][j][1]
    root = Node(terms[get_best_root][0],terms[get_best_root][1])
    # Now, set its child as the answer from the subproblems
    if i != j:
        if get_best_root == j:
            root.set_left_child(make_tree(dp,i,j-1,terms))
        elif get_best_root == i:
            root.set_right_child(make_tree(dp,i+1,j,terms))
        else:
            root.set_left_child(make_tree(dp,i,get_best_root-1,terms))
            root.set_right_child(make_tree(dp,get_best_root+1,j,terms))
    return root

def optimal_binary_search_tree(terms):
    # Use dp to get the optimal binary search tree structure and cost
    dp = []
    n = len(terms)
    # Initialize the dp matrix
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append((0,None))
        dp.append(temp)
    # This problem is similar to MCM, hence length based diagonal approach to fill in.
    # dp at i,j will tell solution for problem from i to j
    for i in range(n):
        dp[i][i] = (terms[i][1],i)

    # Subproblem length 2, 3, ... . l is chain length.
    for l in range(2, n + 1):
        # i is row number in cost
        for i in range(n - l + 1): # i upto n-l
            # Get the required column number, so that j-i+1 = l (subproblem from i to j)
            j = i + l - 1
            # print(f'Len {l} can be achieved with indices ({i},{j})')
            min_cost = None
            min_root = None
            # Try making each of i,i+1,...,j as root to get the minimum cost
            for root_index in range(i,j+1):
                current_cost = None
                # Tree will have from i to root_index and root_index+1 to j
                if root_index == i:
                    current_cost = dp[i+1][j][0]
                elif root_index == j:
                    current_cost = dp[i][j-1][0]
                else:
                    current_cost = dp[i][root_index-1][0]+dp[root_index+1][j][0]
                current_cost += freq_sum(terms,i,j)
                if min_cost is None:
                    min_cost = current_cost
                    min_root = root_index
                if current_cost < min_cost:
                    min_cost = current_cost
                    min_root = root_index
            dp[i][j] = (min_cost, min_root)
    # print(dp)
    # Now construct the actual tree
    tree = make_tree(dp,i,j,terms)
    return tree,dp[0][n-1][0]

if __name__ == '__main__':
    data = get_all_terms('dictionary.txt')
    # data = [(10,34),(12,8),(20,50)]
    tree,cost = optimal_binary_search_tree(data)
    # print(tree)
    # tree.print_tree()
    print(f'Optimal BST has been created, with cost: {cost}')
    print('Level Order Traversal of the Tree:(word-freq format)')
    tree.level_order()
    # print(tree.search('item'))
    # print(tree.search('tree'))
    done = False
    while not done:
        word = input('Enter the word to search for:').strip().lower()
        result = tree.search(word)
        if result:
            print(f'Word "{word}" found at level {result}')
        else:
            print('Word does not exist in dictionary')
        y = input('Do you want to cotinue?(Y/N)')
        if y.lower() != 'y':
            done = True
