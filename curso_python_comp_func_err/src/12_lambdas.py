def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

print(increment(10))

print(increment_v2(20))

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
print(full_name('nicolas', 'perez casas'))