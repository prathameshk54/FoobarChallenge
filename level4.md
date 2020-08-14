Level4  

This time there were 2 challenges and each challenge had time of 2 weeks to solve!  
Here is the problem  

<a href="https://ibb.co/MNryzgq"><img src="https://i.ibb.co/Yjm45Nv/image.png" alt="image" border="0"></a>

The 1st problem to solve in this question is to detect if the givenm pair go in an infinite loop or converge having the same values for both variables.  
As usual, the first solution that striked in my mind was brute force.  
Where we can start doing the process in a loop(or recursivley as well) and check if we encounter the previously occured state (which means that we are in an infinte loop) or check if two variables x & y get the same value.  
But this is worst!!  

Then i started thinking to determine if x and y can get the same value.  
I took a pen paper and started in a reverse way trying to figure out the mathematical relation between the x & y.  
The updation rule for x, y is if y > x : (2x, y - x) else : (y, x)  

<a href="https://imgbb.com/"><img src="https://i.ibb.co/JdxRKC5/image.png" alt="image" border="0"></a>

If final x and y are same, then in prev state, y = 3*x  
(I followed that y will be having the value of the greater variable)  
Going back, div(y - x, 2x) = 3   
*where div(a, b)  function divides the greater variable of a & b by the smaller one.*  

^*Till this point all was going fine, but at next step I did a mistake which I realized much later.*  

I further went in previous step and substituted y - x at the place of y and 2*x at the place of x and kept doing this for few more steps and arrived at a conclusion that div(y - (2^n - 1)*x, 2^n * x) == 3  
Solving further, div(x, y) == 2^m - 1 where m is an integer and remainder is 0  

But at the step after ^this point, how could i know that if y > x then (y - x) > 2*x ? My all further steps were on this wrong assumptions. (I would say that I didn't considre other cases (I kept going only left in the tree :p))  
Then I searched over internet, and one person on github had also given the answer in the above way with one edit below that this doesn't work for all the cases, see the @xyz's comment below to make it work for all the cases.  
And that comment was saying that instead of comparing div(x, y) with 2^m - 1 compare div(x + y, gcd(x, y)) with the same and it covers remaining cases as well!  
I don't know how he/she arrived at this solution! I am now thinking on it.  

The next task was to find maximum numbr of pairs that will run in an infinite loop. At first, I tried a lot using graphs but wasn't able  to find an efficient algorithm. Then i searched on internet and came across blossom algorithm. If this algo is implemented in this question then you've the solution!!  
It took me 5-6 days to complete this problem and it was really difficult one, searching and learning different new things while solving the problem is probably the thing that Google is expecting from the participants.  

Challenge 2:  

<a href="https://ibb.co/PzQS7Kd"><img src="https://i.ibb.co/2YNbDxT/image.png" alt="image" border="0"></a>

This was a graph problem. Required search on internet and came to know about the flow networks.  
And this problem can be solved using Dinitz's algorithm.  
