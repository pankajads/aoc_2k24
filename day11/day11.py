from collections import defaultdict  

#Read the file
with open("./input_sample.txt") as fin:
    raw_nums = list(map(int, fin.read().strip().split()))

#defaultdict to count occurrences of each number
nums = defaultdict(int)

# Populate the nums dictionary with the counts of each number in the input.
for x in raw_nums:
    nums[x] += 1


#function to simulate one blink transformation of the stones.
def blink(nums: dict) -> dict:
    #new defaultdict
    new_nums = defaultdict(int)
    
    # Iterate through each unique stone in the current dictionary.
    for x in nums:
        l = len(str(x))  
        
        #Rule 1
        if x == 0:
            new_nums[1] += nums[0]
        
        #Rule 2
        elif l % 2 == 0:
            new_nums[int(str(x)[:l//2])] += nums[x]
            new_nums[int(str(x)[l//2:])] += nums[x]
        
        #In case doesn't fit to any rule
        else:
            new_nums[x * 2024] += nums[x]
    
    # Return the new stone dictionary after the blink.
    return new_nums



# Replace `75` with a different value to compute for a different number of blinks.
for i in range(75):
    nums = blink(nums)

# Calculate the total number of stones after 75 blinks.
ans = 0
for x in nums:
    ans += nums[x]

# Print the total number of stones.
print(ans)
