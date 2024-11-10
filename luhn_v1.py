
#digits="17893729974"
def verify(digits):
    total = 0
    for i, d in enumerate(reversed(digits[:-1])): # TODO ideally avoid slice
        if i % 2 == 0:
            multiplier = 2
        else:
            multiplier = 1
        x = int(d) * multiplier # TODO name x
        total += x // 10 + x % 10
        print(total)
    return False

if __name__ == '__main__':
    assert verify("17893729974")
    assert not verify("17893729975")
    print('ok')
