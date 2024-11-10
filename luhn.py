def verify(digits):
    total = 0
    for i, d in enumerate(reversed(digits)): 
        x = int(d) * (1 + i % 2)
        total += x // 10 + x
    return total % 10 == 0

if __name__ == '__main__':
    assert verify("17893729974")
    assert not verify("17893729975")
    print('ok')
