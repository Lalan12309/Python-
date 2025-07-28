from itertools import permutations

def can_defeat(a, b):
    # Try all permutations of a and b
    for pa in permutations(a):
        for pb in permutations(b):
            wins = sum(pa[i] > pb[i] for i in range(3))
            if wins >= 2:
                return True
    return False

def possibleWinners(boost_a, boost_b, boost_c):
    n = len(boost_a)
    boosts = [boost_a, boost_b, boost_c]
    result = 0

    for i in range(n):
        player = [boost_a[i], boost_b[i], boost_c[i]]
        can_beat_all = True
        for j in range(n):
            if i == j:
                continue
            opponent = [boost_a[j], boost_b[j], boost_c[j]]
            if not can_defeat(player, opponent):
                can_beat_all = False
                break
        if can_beat_all:
            result += 1
    return result