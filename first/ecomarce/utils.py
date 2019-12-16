def max_n(numbers):
    m = 0
    for i in numbers:
        if i > m:
            m = i
    return m