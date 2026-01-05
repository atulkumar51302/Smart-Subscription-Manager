#in method 

name = "atul kumar sharma"

letter_count = {}
for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)  
