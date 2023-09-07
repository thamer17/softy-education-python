#1
def swap_tuples(t1, t2):
    print("Before swap:")
    print("tuple 1: ",t1)
    print("tuple 2: ",t2)
    print("After swap:")
    nt1 = (t2[0], t1[1], t2[2])
    nt2 = (t1[0], t2[1], t1[2])
    print("tuple 1: ",nt1)
    print("tuple 2: ",nt2)
    
t1 = (1, 2, 3)
t2 = (4, 5, 6)
swap_tuples(t1,t2)
#2
def swap_lists(l1, l2):
    print("Before swap:")
    print("list 1: ",l1)
    print("list 2: ",l2, "\n")
    print("After swap:")
    temp = l1[0]
    l1[0] = l2[0]
    l2[0] = temp 
    temp = l1[2]
    l1[2] = l2[2]
    l2[2] = temp 
    print("list 1: ",l1)
    print("list 2: ",l2)
    
l1 = [1, 2, 3]
l2 = [4, 5, 6]

swap_lists(l1, l2)




