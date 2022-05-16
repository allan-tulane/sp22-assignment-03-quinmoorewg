# assignment-03

# no other imports needed
from collections import defaultdict
import math

def plus(x,y):
  return x+y

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    ###TODO    
# #     # almost but not quite: consider ") ("
#     if next_input == '(':            # new open parens 
#         return current_output + 1
#     elif next_input == ')':          # new close parens
#         return current_output - 1
#     else:
#         return current_output
        
    
    if current_output == -math.inf:  # in an invalid state; carry it forward
        return current_output
    if next_input == '(':            # new open parens 
        return current_output + 1
    elif next_input == ')':          # new close parens
        if current_output <= 0:      # close before an open -> invalid
            return -math.inf
        else:                        # valid
            return current_output - 1
    else:                            # ignore non-parens input
        return current_output
    ###
    
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    ### TODO
    return iterate(parens_update, 0, mylist) == 0
    ###

def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False
    assert parens_match_iterative(['(', 'a', ')', '(', ')']) == True
    assert parens_match_iterative(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_iterative(['(', '(', ')']) == False
    assert parens_match_iterative(['(', 'a', ')', ')', '(']) == False
    assert parens_match_iterative([]) == True
    
test_parens_match_iterative()

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We'll discuss how to make it more efficient later.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    ###TODO
    history, last = scan(plus, 0, list(map(paren_map, mylist)))
    print(history, last)
    return last == 0 and reduce(min_f, 0, history) >= 0
    ###

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False
    assert parens_match_scan(['(', 'a', ')', '(', ')']) == True
    assert parens_match_scan(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_scan(['(', '(', ')']) == False
    assert parens_match_scan(['(', 'a', ')', ')', '(']) == False
    assert parens_match_scan([]) == True

# test_parens_match_scan()    
parens_match_scan(['(', ')', ')', '('])

# D&C parens_match

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses ), and
      L is the number of unmatched left parentheses (. This output is used by 
      parens_match_dc to return the final True or False value
    """
    ###TODO
    # Base cases
    if len(mylist) == 0:
        return [0,0]
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1) # one unmatched (
        elif mylist[0] == ')':
            return (1, 0) # one unmatched )    
        else:
            return (0, 0)
    r1,l1 = parens_match_dc_helper(mylist[:len(mylist)//2])
    r2,l2 = parens_match_dc_helper(mylist[len(mylist)//2:])
    # Combination:
    # Return the tuple (R,L) using some combination of the values i,j,k,l defined above.
    # This should be done in constant time.
    if l1 > r2:
        return (r1, (l1 - r2) + l2)
    else:
        return ( (r2 - l1) + r1,   l2)
    ###
    # if we did this, would return negative values 
    # return ((r2-l1)+r1, (l1-r2)+l2)
    
def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
    assert parens_match_dc(['(', 'a', ')', '(', ')']) == True
    assert parens_match_dc(['(',  '(', '(', ')', ')', ')']) == True
    assert parens_match_dc(['(', '(', ')']) == False
    assert parens_match_dc(['(', 'a', ')', ')', '(']) == False
    assert parens_match_dc([]) == True    

test_parens_match_dc()
# parens_match_dc(['(', 'a', ')', ')', '(', ])