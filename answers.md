# CMPS 2200 Assignment 3
## Answers

**Name:**_________________________


Place all written answers from `assignment-03.md` here for easier grading.






- **b.**
W(n) = O(n)
S(n) = O(n)




- **d.**
    history, last = scan(plus, 0, list(map(paren_map, mylist)))
    return last == 0 and reduce(min_f, 0, history) >= 0
  
map has  𝑂(𝑛)  work and  𝑂(1)  span
scan has  𝑂(𝑛)  work and  𝑂(lg𝑛)  span
reduce has  𝑂(𝑛)  work and  𝑂(lg𝑛)  span
So, combination has  𝑂(𝑛)  work and  𝑂(lg𝑛)  span





- **f.**
𝑊(𝑛)=2𝑊(𝑛/2)+1 
leaf dominated: 1 -> 2 -> 4 -> 8 -> ...

number of leaves is 2lg𝑛
-> 𝑂(𝑛)
.
.

𝑆(𝑛)=𝑆(𝑛/2)+1
balanced: 1 -> 1 -> 1 -> ...

-> 𝑂(lg𝑛)