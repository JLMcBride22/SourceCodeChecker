def solution(A, B):
    largest = A
    smallest = B

    if B > A:
        largest = B
        smallest = A

    side = int((A+B)/4)

    if(side == 0):
        return 0
    
    noSidesFromLargest = int(largest/side)

    if noSidesFromLargest == 4:
        return side

    noSidesFromSmallest = 4 - noSidesFromLargest
    if smallest < (noSidesFromSmallest) * side:
        if smallest == 0:
            print("failure")
        diff= int(largest/smallest)# test  a lot of zero and equal cases. shouldn't be a problem
        if diff > smallest:
            diff = 1
        smallest -= diff
        side = solution(largest, smallest)
    
    return side


if 33==solution(100, 50):
    print("yay")
else:
    print("bad")

if 5 == solution(13, 11):
    print("yay")
else:
    print("bad")

if 3 == solution(14, 2):
    print("yay")
else:
    print("bad")

if solution(10, 0) == 2:
    print("yay")
else:
    print("bad")
