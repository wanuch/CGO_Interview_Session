def solution(X, A):
    pos = set()

    for i, j in enumerate(A):
        pos.add(j)
        if len(pos) == X:
            return i
    return -1