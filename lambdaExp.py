# Notes for Python Tutorial on Lists and Lambda Expressions as anoymous functions



# Sort list by last name in alphabetical order

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# Help(scifi_authors.sort)

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

# Write a function that makes functions using Quadratic Functions

# Quadratic Functions example: f(x) = a*x**2 + b*x + c

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax*2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(3, 0, 1)(2) # 3x^2+1 evaluated for x=2
