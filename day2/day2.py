def is_safe(report):
    print(report)
    # Iterate over consecutive elements to check the difference
    for i in range(len(report) - 1):
        diff = int(report[i + 1]) - int(report[i])  # Get the difference between consecutive numbers
        
        # Check if the difference is greater than 3 or less than -3, or if it's zero
        if abs(diff) > 3 or diff == 0:
            return False
        
        # Check for any inconsistent increase and decrease patterns (increasing then decreasing or vice versa)
        if i > 0:
            prev_diff = int(report[i]) - int(report[i - 1])
            if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                return False
    return True

def is_safe_with_removal(report):
    print(report)

    # Try removing each level and check if the report becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the ith element
        if is_safe(modified_report):
            return True
    
    # If none of the removal cases result in a safe report, return False
    return False

filename="input_sample.txt"
safe_reports = 0
safe_reports_with_removal = 0
with open(filename) as filehandler:
    for line in filehandler.readlines():
        if is_safe(line.split()):
            safe_reports += 1
        
        if is_safe_with_removal(line.split()):
            safe_reports_with_removal += 1


print(safe_reports)
print(safe_reports_with_removal)
