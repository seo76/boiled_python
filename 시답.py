import random
"""
def go(x,y):
    a, x, y =0, 0, 0
    dire=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    random.shuffle(dire)
    return(dire(x,y))

print(dire[1])
print(go(1,2))
"""

x=0
y=0

dire=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]

print(dire[1])

def go(x,y):
    ran=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    random.shuffle(ran)
    return ran[1]

print(go(1,2))
