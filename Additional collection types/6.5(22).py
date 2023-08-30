def wins(pairs):
    from collections import defaultdict
    data = defaultdict(set)
    for pair in pairs:
        data[pair[0]].add(pair[1])

    return data