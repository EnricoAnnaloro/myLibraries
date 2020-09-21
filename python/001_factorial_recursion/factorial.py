def factorial(n):
    """Performs the factorial of n using recursion"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    test1_solution = 5*4*3*2*1
    test2_solution =  7*6*5*4*3*2*1
    test3_solution = 9*8*7*6*5*4*3*2*1
    test_1 = factorial(5)
    test_2 = factorial(7)
    test_3 = factorial(9)

    if test_1 != test1_solution:
        raise Exception(f'Test 1 was not passed! test_1 is {test_1}, should be {test1_solution}.')
    elif test_2 != test2_solution:
        raise Exception(f'Test 2 was not passed! test_2 is {test_2}, should be {test2_solution}.')
    elif test_3 != test3_solution:
        raise Exception(f'Test 3 was not passed! test_3 is {test_3}, should be {test3_solution}.')
    else:
        print("Tests passed.")


