
#digits="17893729974"
def verify(digits):
    for d in reversed(digits[:-1]):
        print(d)
    return False

if __name__ == '__main__':
    assert verify("17893729974")
    assert not verify("17893729975")
    print('ok')
