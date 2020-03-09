from collections import defaultdict

# Two solutions based on https://stackoverflow.com/a/60592052/12671057

# 100%: https://app.codility.com/demo/results/trainingX6MXQ4-MCN/
def solution(N, A):
    counters = defaultdict(int)
    for a in A:
        if a <= N:
            counters[a] += 1
        elif counters:
            counters = defaultdict(max(counters.values()).__int__)
    return [counters[i] for i in range(1, N+1)]

# 100%: https://app.codility.com/demo/results/trainingJTCGM7-JVV/
def solution(N, A):
    default = 0
    counters = defaultdict(lambda: default)
    for a in A:
        if a <= N:
            counters[a] += 1
        elif counters:
            default = max(counters.values())
            counters.clear()
    return [counters[i] for i in range(1, N+1)]
