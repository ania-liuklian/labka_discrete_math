"""belman_ford"""
def belman_ford(graph: dict[str, dict[str, int]], start_point: str):
    """
    Docstring for belman_ford

    >>> graph = {'S': \
    {'A':10, 'E':8}, \
    'A':{'C':2}, \
    'B':{'A': 1}, \
    'C': {'B': -2}, \
    'D': {'C':-1, 'A':-4}, \
    'E':{'D': 1}}
    >>> print(belman_ford(graph, 'S'))
    Point S: Dictance 0
    Point A: Dictance 5
    Point B: Dictance 5
    Point C: Dictance 7
    Point D: Dictance 9
    Point E: Dictance 8

    >>> g2 = {'A': {'B': 5}, 'B': {'C': 3}, 'C': {}}
    >>> print(belman_ford(g2, 'A'))
    Point A: Dictance 0
    Point B: Dictance 5
    Point C: Dictance 8

    >>> g3 = {'A': {'B': 10, 'C': 2}, 'C': {'B': 3}, 'B': {}}
    >>> print(belman_ford(g3, 'A'))
    Point A: Dictance 0
    Point C: Dictance 2
    Point B: Dictance 5

    >>> g4 = {'X': {'Y': 10, 'Z': 5}, 'Z': {'Y': -20}, 'Y': {}}
    >>> print(belman_ford(g4, 'X'))
    Point X: Dictance 0
    Point Z: Dictance 5
    Point Y: Dictance -15
    """

    point_weight = {start_point: 0}
    for point in graph:
        if point!=start_point:
            point_weight[point] = 'inf'

    for _ in range(len(graph)-1):
        for top, next_point_weight in graph.items():
            if point_weight[top] == 'inf':
                continue
            for next_top, top_weight in next_point_weight.items():
                if (point_weight[next_top] == 'inf'
                or point_weight[next_top]>top_weight+point_weight[top]):
                    point_weight[next_top] = top_weight+point_weight[top]
    final_return = [f'Point {point}: Dictance {weight}'for point, weight in point_weight.items()]
    return "\n".join(final_return)

if __name__=='__main__':
    import doctest
    print(doctest.testmod())
