def unify_var(var, x, theta):
    """
    Unify a variable var with the expression x using the given substitution theta.
    """
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    elif occurs_check(var, x, theta):
        return None
    else:
        theta[var] = x
        return theta

def unify(x, y, theta):
    """
    Unify the two expressions x and y with the given substitution theta.
    """
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and is_variable(x):
        return unify_var(x, y, theta)
    elif isinstance(y, str) and is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        else:
            return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def is_variable(x):
    """
    Check if the given expression x is a variable.
    """
    return isinstance(x, str) and x.islower()

def occurs_check(var, x, theta):
    """
    Check if variable var occurs in x with the given substitution theta.
    """
    if var == x:
        return True
    elif isinstance(x, str) and is_variable(x) and x in theta:
        return occurs_check(var, theta[x], theta)
    elif isinstance(x, list):
        return any(occurs_check(var, term, theta) for term in x)
    else:
        return False

# Example usage
if __name__ == "__main__":
    # Define expressions
    expression1 = ['P', 'x', 'y']
    expression2 = ['P', 'A', 'B']
   
    # Unify the expressions
    substitution = unify(expression1, expression2, {})
   
    # Print the result
    if substitution is None:
        print("Unification failed.")
    else:
        print("Unification successful. Substitution:", substitution)
