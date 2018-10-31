# example: 
# expression = "(ln (/ (max (min X 9999.0) 1.0) (- 10000 (max (min X 9999.0) 1.0))))"  # log odds of X 

def DecodeFromFreeForm(expression):
    items = expression.split(' ')
    LeftOperations = set({"min", "max"})
    MiddleOperations = set({"-", "+", "*", "/"})
    SingleOperations = set({"ln"})
    stack = []
    left = 0
    right = 0
    for item in items:
        if item.startswith('('): # it is an operation
            left += 1
            stack.append(item)
        elif item.endswith(')'): # it is a variable or number
            nums = item.count(')')
            right += nums
            cur = item.rstrip(')')
            
            for _ in range(nums): # nums of operations
                prev = stack.pop()
                if prev.startswith('('): # it is a single operation
                    if prev.lstrip('(') not in SingleOperations:
                        print(prev + "is not a single operation!")
                    cur = prev.lstrip('(') + "(" + cur + ")"
                else: # it is a variable
                    action = stack.pop()
                    if not action.startswith('('):
                        print("error!")
                    action = action.lstrip('(')
                    if action in LeftOperations:
                        cur = action + "(" + prev + " , " + cur + ")"
                    elif action in MiddleOperations:
                        cur = "(" + prev + " " + action + " " + cur + ")"
            stack.append(cur)               
        else:
            stack.append(item)
    #print("left = " + str(left))
    #print("right = " + str(right))
    #print("stack len = " + str(len(stack)))
    return stack[0]