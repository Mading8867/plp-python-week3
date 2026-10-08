count = 1
total = 0
# BUG: The while statement was missing a colon, so I added it.
# BUG: The loop stopped before reaching 5, so I changed < to <=.

while count <= 5:
    total = total + count
    count = count + 1

# BUG: I was trying to add a string and an integer, so I changed it to an f-string.
print(f"Sum of 1 to 5 is: {total}")