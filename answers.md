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
  
map has  ð(ð)  work and  ð(1)  span
scan has  ð(ð)  work and  ð(lgð)  span
reduce has  ð(ð)  work and  ð(lgð)  span
So, combination has  ð(ð)  work and  ð(lgð)  span





- **f.**
ð(ð)=2ð(ð/2)+1 
leaf dominated: 1 -> 2 -> 4 -> 8 -> ...

number of leaves is 2lgð
-> ð(ð)
.
.

ð(ð)=ð(ð/2)+1
balanced: 1 -> 1 -> 1 -> ...

-> ð(lgð)