def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """

    # x: expected_num
    # y: count
    # n: observed_num

    def g(x, y):
        # g(x,y)返回了一个函数h，而且这个函数记住了x和y
        # 函数h就专注于吃每次看见的num n，然后和它记住的x进行比较，并酌机更新y
        # 返回新的自己
        def h(n):
            if (x==0) or (x==n):
                return g(x+1, y)
            else:
                print(x,y+1)
                return g(n+1, y+1)
        return h
    return g(0,0)
