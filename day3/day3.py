import re

#Function for puzzle 2
def solution2(data):
    #regex to search based what's asked. I generally use regex101.com site build and test regex query
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", data)
    
    #Flag to be used to check number post do() or don't()
    enabled = True
    ans2 = 0
    #print(matches)
    #Iterate over matches
    for match in matches:
        if match[2] == "" and enabled:
            ans2 += int(match[0]) * int(match[1])
        else:
            if match[2] == "do()":
                enabled = True
            else:
                enabled = False

    return ans2

#Function for puzzle 1
def solution1(line):
    ans1=0
    #regex to search based what's asked. I generally use regex101.com site build and test regex query
    pattern = r"mul\(\d+,\d+\)"
    pattern_mul = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)

    #print(matches)
    #print(len(matches))
    #Iterate over matches
    for match in matches:
        #num1=match.split()
        #print(match)
        match_mul = re.search(pattern_mul, match)
        #print(match_mul,match_mul.group(1),match_mul.group(2))
        ans1 += int(match_mul.group(1))*int(match_mul.group(2))
    
    return ans1


#Read the input file
with open("./input_sample.txt") as fin:
    line = fin.read().strip()
    #print(line)
    print(solution1(line))
    print(solution2(line))
