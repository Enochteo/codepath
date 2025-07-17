```python
def evaluate_ternary_expression_recursive(expression):
    def helper(i):
        # Base case: return a digit or boolean value if it's just that
        if i >= len(expression) or expression[i] not in 'TF?' or (expression[i] in 'TF' and (i+1 >= len(expression) or expression[i+1] != '?')):
            return expression[i], i

        # Current character should be a condition (either 'T' or 'F')
        condition = expression[i]
        i += 2  # Skip condition and '?'

        # Recursively evaluate the true_expression
        true_val, i = helper(i)

        i += 1  # Skip ':'
        # Recursively evaluate the false_expression
        false_val, i = helper(i)

        if condition == 'T':
            return true_result, i
        else:
            return false_result, i

    result, _ = helper(0)
    return result
```
