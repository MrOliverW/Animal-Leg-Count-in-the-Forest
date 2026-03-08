# Animal-Leg-Count-in-the-Forest
AD311 Animal Leg Count in the Forest program that examines an array of different animals and determines how many of them have exactly four legs

Clarifying Questions
A few good questions about this exercise I might ask:
1.	Case Sensitivity: Should 'Lion' and 'lion' be treated the same? (I'll assume case-insensitive).
2.	Unknown Animals: How should the program handle animals not in our predefined list? (I'll assume we ignore them/count as 0).
3.	Input Size: Are we dealing with a few animals or millions? (This determines if we need to worry about memory).

Complexity Analysis
Time Complexity: O(n + m)
•	$n$ is the number of animals in the input array. We must visit each animal once.
•	$m$ is the number of animals in our reference set (used to build the set initially).
•	Since set lookup is $O(1)$, the total time scales linearly with the input.

Space Complexity: O(m)
•	We store m animal names in our four_legged_reference set. The size of the input array doesn't increase our permanent memory usage because we don't store the input; we just iterate through it.
•	

