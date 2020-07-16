Level3  
Level 3 had 3 challenges to complete, this time difficulty level was increased and for each challenge 96 hours were given.  

Challenge 1:  

This question used heavy words to explain the problem hence it took me much time to exactly understand the problem!  

<a href="https://ibb.co/Wp4H9d3"><img src="https://i.ibb.co/k6sGnry/image.png" alt="image" border="0"></a>

Approach:  
The first thing that i was worrying about, after understanding the probem : how to handle number as large as 10^50 ?  
Then I searched for the range of long in python and came to know that it can hold number of any size!!! I got something new  
to learn, and started to build the solution.  

I drew the tree on the paper with root (1, 1) and both possible replications as its children (1, 2) & (2, 1); and continued ...  
Then i observed that, the bomb which is less number, is the one who replicated itself in the previous generation  
And if I subtract the less-number from greater-number then I'll get the number of bombs(of another type) that was there in the   
previous generation.  

So my approach was keep counting the the number of generations starting from end i.e. from (m, n) to (1, 1) by repeated subtraction, till i reach (1, 1)  
If I can not reach (1, 1), and ran into the negative side, the "impossible was returned"  

Later, I searched for it on internet, and found little improvement in my approach:  
	Instead of just subtracting and incrementing the count by 1, take mod and increment count by the quotient!  

I wrote the code (taking help from internet), and it passed all the test-cases!  

Challenge 2:  

This question was based on the probabilty and absorbing markov chain.  

<a href="https://ibb.co/nmR6Hk3"><img src="https://i.ibb.co/qjx7t10/image.png" alt="image" border="0"></a>

I knew the Markov Chain concept as I had studied it in my academic-course. So when I first read the problem, I got an idea that  
this is the markov chain problem, but I was not getting the solution to find number of steps after which I have to find the  
probabilities, because there can be any number of steps to reach the terminal node.  
Then after searching on internet, I came to know about absorbing markov chain. I studied it, and it turned out to be the very  
easy problem!  
The only difficulty was to find the inverse of the matrix, so again i searched and found the gauss elimination method to find  
an inverse. I'll not elaborate that here. There was also the problem of converting the float values to the fractions.  
So I used fractions.Fraction Library in the Python.  
Actually this solution becomes very easy if you code it using numpy! As it has in-built function to find inverse of the matrix!  
But, numpy doesn't accept 'fractions.Fraction' object and I don't know whether foobar supports importing numpy.  

Challenge 3:

This question was of dynamic programming and the familiar to me because I had already tried it in one of the aptitude-tests.  

<a href="https://ibb.co/7gLWy6v"><img src="https://i.ibb.co/N1bjYHx/image.png" alt="image" border="0"></a>  

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be  
built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200,  
because Commander Lambda is not made of money!  

Solution:  
I first tried to use recursion on small numbers.  
As the algorithm seemed to be the correct, I implemented dynamic programming by creating an 2x2 array (for prev and n) to store  
the results, and improve the time complexity.  

Logic of recursion was, pass the numbers of bricks in previous step(prev) and number of bricks left to the function rec()  
This function recursively calls itself for all the possible^ number of bricks in the next step and adds the result to return.  
^ number of bricks left after constructing a step with n bricks must be greater than n or 0  
To take care of 0, I have initiated the count to 1 (1 possibilty of constructing step with all remaining bricks)  
	*if n > prev and its not the first step*  

Code:  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/F87DFt3/image.png" alt="image" border="0"></a>  

After completing level3, it asked me my personal details along with my cv for the google recruiters to contact if they want.  
