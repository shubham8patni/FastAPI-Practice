# closure : making a function inside a function allowing the inside function to by default inherit variables of outer function without passing them as parameter
# as you can see below we are returning a function itself "inner_func" and storing it in a variable and now the variable itself can be called like a function
def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

func = outer_func('hello there!!')
func()