LEVEL 1

Level1 was an easy one with only 1 problem to solve within 2 days after you request the challege.  
The challenge was :

Two lists were given. One of them had some integers (non-unique) in it and the second list had the same integers (with same  
number of occurences for each one) but in shuffled order. Additionaly there was an one additional unique integer in one of the  
lists. I had to write the function which returns this additional integer.

Initially, i thought of 'Brute Force' i.e. comparing each integer in 1 list with every other integer in the other list, but it  
was clearly mentioned that commander lambda in the story of the problem loves efficiency and wants an efficient code!

So I used hash-table / dictionary to store the unique integers in the list and just iterated through the another list checking  
whether the key of the element in the other list exists in the dictionary or not.  
This gives us the result in the O(n) time.

Code:

