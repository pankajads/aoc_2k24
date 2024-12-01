#pass your puzzle input in below path
filename="input_sample.txt"


def solution1(ltlst,rtlst):
    solution1 = 0
    ltlst = sorted(ltlst)
    rtlst = sorted(rtlst)

    for i in range(len(ltlst)):
        solution1 += abs(ltlst[i]-rtlst[i])

    return solution1

def solution2(ltlst,rtlst):
    solution2 = 0
    frequency = {}

    for element in rtlst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    for element in ltlst:
        if element in frequency:
            solution2 += element * frequency[element]
    
    return solution2




#Reading Input file and parse it line by line
with open(filename) as filehandler:
    #numarray=[]
    leftlst=[]
    rightlst=[]
    for line in filehandler.readlines():
        leftlst.append(int(line.split()[0]))
        rightlst.append(int(line.split()[1]))



print(solution1(leftlst,rightlst))  
print(solution2(leftlst,rightlst))  



    
        
