from collections import defaultdict

def checkMagazine(magazine, note):
    
    mag = defaultdict(int)
    
    for m in magazine:
        mag[m] += 1
    
    for n in note:
        if mag[n] == 0:
            print('No')
            return
        elif mag[n] > 0:
            mag[n] -= 1

    print('Yes')

m1, n1 = 'give me one grand today night', 'give one grand today'
m2, n2 = 'ive got a lovely bunch of coconuts', 'ive got some coconuts'
m3, n3 = 'two times three is not four', 'two times two is four'

checkMagazine([m for m in m1.split(' ')], [n for n in n1.split(' ')])
checkMagazine([m for m in m2.split(' ')], [n for n in n2.split(' ')])
checkMagazine([m for m in m3.split(' ')], [n for n in n3.split(' ')])