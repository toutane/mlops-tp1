def avg(l: list) -> float:
    return sum(l) / len(l)

def avg_buggy(l: list) -> float:
    return sum(l) % len(l)

def test_avg_easy():
    l = [1, 4, 8, -3, 9, -7]
    assert avg(l) == 2.0

def test_avg_hard():
    l = [1, 4, 8, -3, 9, -7, 8, 2, -10, 20]
    assert avg(l) == 3.2

#def test_avg_buggy_easy():
#    l = [1, 4, 8, -3, 9, -7]
#    assert avg_buggy(l) == 2.0
#
#def test_avg_buggy_hard():
#    l = [1, 4, 8, -3, 9, -7, 8, 2, -10, 20]
#    assert avg_buggy(l) == 3.2
