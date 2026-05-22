# https://codeforces.com/gym/105909

def main():
    s = input().strip()
    if s.endswith('isallyouneed'):
        print('Yes')
        print(s[0 : -(len('isallyouneed'))])
    else:
        print('No')


main()
