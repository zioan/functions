## Functions with more than 1 arguments

#default argument
def area (a, b):
  return a * b
print(area(4, 5))

#key position argument
def area (a, b):
  return a * b
print(area(b=4, a=3))

#paramether (default value)
def area (a, b=3):
  return a * b
print(area(2))
#6


# exercise 1

def str_concat (a, b):
  result = f"{a} {b}"
  return result

print(str_concat("hello", "there"))
# hello there / as strings concatenation

############# OR

def result(a,b):
    return "{} {}".format(a,b)


######################################################################################
# Functions with an Arbitrary Number of Non-keyword Arguments
def mean(*args):
  return args
print(mean(1, 3, "a", 4))
#return a tuple (1, 3, "a", 4) 

def average(*args):
  return sum(args) /len(args)
print(average(1, 3, 4))
# 2.6666666666666665

#exercise (the arguments must be uppercase and alphabetical ordered)
def ordering(*args):
  result_upper = []
  for i in args:
    result_upper.append(i.upper())
    for word in result_upper:
      result_order = sorted(result_upper)
  return result_order

print(ordering("snow", "glacier", "iceberg"))


#####################################################################################
# Functions with an Arbitrary Number of Keyword Arguments

def mean(**kwargs):
  return kwargs
print(mean(a=1, b=2, c=3))
# result is a dictionary {'a': 1, 'b': 2, 'c': 3}

# exercise
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3, b=6))