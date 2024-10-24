

s = 0
prev, curr = 1, 2

while curr < 4000000:
    if curr%2==0:
        s += curr
        
    nxt = curr + prev
    prev = curr
    curr = nxt
    
print(s)