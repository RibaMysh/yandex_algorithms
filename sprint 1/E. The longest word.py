n = int(input())
lst = input().split()
mx = -1
mWord = lst[0]
for word in lst:
    if len(word) > mx:
        mx = len(word)
        mWord = word
print(mWord, mx, sep='\n')



