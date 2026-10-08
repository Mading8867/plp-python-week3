# Week 3 Assignment on Conditions and Loops

## Files

- `grade_reporter.py` - Uses a for loop and conditions to assign grades, count passes and failures, and calculate the average score.
- `bug_hunt.py` - Finds and fixes three bugs in a while loop program that calculates the sum of 1 to 5.

## Bug Hunt Reflection

The hardest bug to find was the loop condition because the program ran without showing an error message. I knew something was wrong because the program printed 10 instead of the expected answer, 15. I checked the loop and realized that `count < 5` stopped the loop before it could add 5, so I changed it to `count <= 5`.