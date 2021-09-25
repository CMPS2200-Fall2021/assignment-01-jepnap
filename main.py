"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x 
    else: 
        return foo(x-1) + foo(x-2)
    ### TODO
    pass

def longest_run(mylist, key):
    lister = []
    j = 0
    for i in range(len(mylist)):
        if key == mylist[i]:
            j+=1
        elif key != mylist[i]:
            lister.append(j)
            j = 0
    c = 0 
    for i in range(len(lister)):
        if lister[c] < lister[i]:
            c = i
    return lister[c]
    
    ### TODO
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on l side of input
        self.right_size = right_size             # run on r side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    middle = int(len(mylist)/2) 

    if len(mylist) == 1:

        if mylist[0] == key:
            return Result(1,1,1,True)
        else:
            return Result(0,0,0,False)
    
    else:

        l = longest_run_recursive(mylist[0:middle], key)

        r = longest_run_recursive(mylist[middle: len(mylist)], key)
        
        if l.is_entire_range and r.is_entire_range:
            genius = Result(l.left_size + r.right_size,l.left_size+r.right_size,max(l.right_size+r.left_size,l.longest_size,r.longest_size),True) 
        elif l.is_entire_range:
            genius = Result(l.left_size + r.left_size,r.right_size,max(l.right_size+r.left_size,l.longest_size,r.longest_size),False) 
        elif r.is_entire_range:
            genius = Result(l.left_size, l.right_size + r.right_size,max(l.right_size+r.left_size,l.longest_size,r.longest_size),False) 
        else:
            genius = Result(l.left_size,r.right_size,max(l.right_size+r.left_size,l.longest_size,r.longest_size),False) 
            
        return genius

    ### TODO
    pass

## Feelgeniusee to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

#rint(foo(3))
#print(longest_run([2,12,12,8,12,12,12,0,12,1], 12))
#print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 1))