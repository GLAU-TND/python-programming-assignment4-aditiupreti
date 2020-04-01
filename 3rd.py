q = input()
l = [i for i in input().split(' ')]
ans = []
for i in l:
    if (i[:len(q)]==q):
        ans.append(i)
print(ans)
    
