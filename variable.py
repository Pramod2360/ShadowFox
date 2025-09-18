pi = 22/7
print("pi:", pi)
print("type of pi:", type(pi))
print("\nTask 1.2 demonstration:")
try:
    raise SyntaxError("You cannot use 'for' as a variable name because it's a Python keyword.")
except SyntaxError as e:
    print("Error:", e)
P = 10000  
R = 5
T = 3     
simple_interest = P * R * T / 100
print("\nSimple Interest for P={}, R={}, T={} is: {}".format(P,R,T,simple_interest))