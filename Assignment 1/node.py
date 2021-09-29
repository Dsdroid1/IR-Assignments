class Node:
    # Constructor
    def __init__(self,term,freq):
        self.term = term
        self.freq = freq
        self.right = None
        self.left = None

    # Getters
    def get_term(self):
        return self.term

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def get_freq(self):
        return self.freq

    # Setters
    def set_right_child(self,right_child):
        self.right = right_child

    def set_left_child(self,left_child):
        self.left = left_child

    # Print the whole tree
    def print_tree(self):
        # Preorder
        print(f'{self.term}-{self.freq}')
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()

    # Level wise traversal
    def level_order(self):
        queue = [self]
        level = 1
        nodes_in_level = 1
        nodes_in_next_level = 0
        print('Level 1')
        while queue:
            node_to_print = queue.pop(0)
            print(f'{node_to_print.term}-{node_to_print.freq}', end = " ")
            nodes_in_level -= 1
            if node_to_print.right is not None:
                queue.append(node_to_print.right)
                nodes_in_next_level += 1
            if node_to_print.left is not None:
                queue.append(node_to_print.left)
                nodes_in_next_level += 1
            if nodes_in_level == 0:
                level += 1
                print('')
                if nodes_in_next_level > 0:
                    print(f'## Level {level}')
                nodes_in_level = nodes_in_next_level
                nodes_in_next_level = 0

    # To search a word in our tree(internally)
    def internal_search(self, word, depth):
        if self.term == word:
            return depth
        elif self.term < word:
            if self.right is not None:
                return self.right.internal_search(word,depth+1)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.internal_search(word,depth+1)
            else:
                return False

    # Wrapper over internal search for depth = 0
    def search(self,word):
        result = self.internal_search(word,1)
        if result is not None:
            return result
        else:
            return False