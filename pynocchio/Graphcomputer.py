import random
'''
to generate the operation sequence from a given graph
method : topological sort
'''
def graph2sequence(graph):
    node_sequence = []
    while len(graph) > 0:
        all_input = []
        all_output = []

        for n in graph:
            # type of graph[n] is : List
            # value of graph[n] is the node that n point to.
            all_input  += graph[n]
            all_output.append(n)

        all_input = set(all_input)
        all_output = set(all_output)

        #the node that only have output but do not have any input can be removed now
        zero_in = all_output - all_input

        if len(zero_in) > 0:
            node = random.choice(list(zero_in))

            current = [node]
            # if this is the last node
            if len(zero_in) == 1:
                #zero_in[node] is the method of node output, exp: linear,sigmoid
                current += zero_in[node]

            #delete this node
            graph.pop(node)
            node_sequence += current

            for _,links in graph.items():
                if node in links:
                    links.remove(node)
        else:
            break
    return node_sequence
