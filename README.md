# Minimum Window Substring

Given two strings *s* and *t* of lengths *m* and *n* respectively, return the **minimum window substring** of *s* such that every character in *t* (**including duplicates**) is included in the window. If there is no such substring, return the empty string *""*.

The testcases will be generated such that the answer is **unique**.

A **substring** is a contiguous sequence of characters within the string.

## Example:

**Input**: s = "ADOBECODEBANC", t = "ABC"
**Output**: "BANC"
**Explanation**: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

## Strategy
1. Use counter of t to check if the substring is qualified: 
  - subtract its value by 1 when a char is added to the substring 
  - if current value is 0 or less, this addition is consider 'valid'
  - when number of valid addition sums to the length of t, the substring is qualified (contains all chars of t including duplicates)
2. Use 2 pointer tech to 'define' the substring:
  - sqeeze the left pointer to get the **shortest qualified substring**
  - store the shortest substring's start and end index
  
## Time Complexy
O(m+n)
