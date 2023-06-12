#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    if tuple_a[0] and tuple_b[0]:
        a = tuple_a[0] + tuple_b[0]
    if tuple_a[1] and tuple_b[1]:
       b = tuple_a[1] + tuple_b[1]
        

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
