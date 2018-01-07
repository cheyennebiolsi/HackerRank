from collections import Counter

def ransom_note(magazine, ransom):
    magazineWords = Counter(magazine)
    for word in ransom:
        if word not in magazineWords or magazineWords[word] == 0:
            return False
        magazineWords[word] -= 1
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
