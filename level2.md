Level 2:  
In level2 there were 2 challenges, again with easy level, but this time, time to solve the each challenge was 72 hours !

Challenge 1:  
I was given the string of the people moving in either direction (left or right) in the same speed with their current positions.  
eg. >----<<><--<<-->>-<--  
In this string '>' indicates the person moving in right direction and '<' indicates the person moving in the left direction.  
And '-' indicates the empty path.  
Every time the two person meet on their way, they do the shakehand.  
Write the function to return the total number of shakehands given the string as an argument.  

Approach:  
This was a very easy problem.  
I first deleted all the '-'s in the string as they were useless  
	for every '>' moving from the left in the string:  
		count '<' to the right of the current '<' and add it to the total count  
	return count  

Though this turns out to be O(n2), all test cases were passed.  

But this can be improvised to O(n) by following approach:  
* First count all the '<'s to the right of the '>'s  
* Then while finding the next '>', also keep the count of the '<'s encountered while traversing (tempCount).  
* count = count - tempCount and add count to total-count  

Code:  


Challenge 2:  
Challenge 2 was a sorting problem.  

You are provided with the list of strings of the version numbers and your task is to arrange them in the ascending order.  
Version number consists of 3 parts: "a.b.c", where a has more significance than b and c & b has more significance than c  
i.e. 2.0.0 is greater than 1.5.5 which is greater than 1.3.7  
b and c part are optional, but if there is c, then b has to be there  
eg. 1.2 is equivalent to 1.2.0; 2 is equivalent to 2.0.0  
If two strings are there which mean the same version number then the onw with the less length is considered to be the smaller  
than the other.  
i.e. 2.2 < 2.2.0  

Approach:  
As it was a sorting problem, O(nlogn) was the time-complexity for the in-built sort function.  
I just had to write to the compare function to provide it as the argument to the sort function's 'cmp' key  

In this function, i first extracted all the a, b, c in the integer form from the string, and with if-else statements returned  
their comparision results.  

Code:  

PS: After completing level2, I got a link to refer my friend for the foobar challenge !  
