def increment(x):
    return x + 1

def higher_order_function(x, func):
    return x + func(x)

result = higher_order_function(2, increment)
print(result)

increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func_v2(2, increment_v2)
print(result)