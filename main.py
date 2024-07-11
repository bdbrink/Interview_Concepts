

def enum_basic(s: list):
    list1_enum = enumerate(s)
    return list1_enum

l1 = ["test", "testing", "tester"]

test = enum_basic(l1)
print(type(test))
print(list(test))

testing = enumerate(l1)
next_ele = next(testing)
print(next_ele)
