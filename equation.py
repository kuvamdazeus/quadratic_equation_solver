import re, sys
"""the equation should follow the rules written here:
1. form of equation should be: a*x^2+b*x+c
2. causes error if invalid equation is given"""

# example: if a = +1, b = 0, c = +10 then, you would write "+1*x^2+0*x+10"
# same goes for others too

def extract_coef(string):
    a_pattern = r"(^[\+\-][0-9]+)\*x"
    b_pattern = r"([\+\-][0-9]+)\*x[\+\-]"
    c_pattern = r"([\+\-][0-9]+$)"
    a = re.search(a_pattern, string)
    b = re.search(b_pattern, string)
    c = re.search(c_pattern, string)
    coefs = []
    coefs.append(a.group(1))
    coefs.append(b.group(1))
    coefs.append(c.group(1))
    return coefs

def calculate_zeros(coefs):
    a, b, c = coefs
    a = int(a)
    b = int(b)
    c = int(c)
    D = b**2 - 4*a*c
    if D < 0:
        print("No real roots")
        sys.exit(0)
    x1 = (-b + (D)**(1/2))/(2*a)
    x2 = (-b - (D)**(1/2))/(2*a)
    print(x1, x2)
    return (x1, x2)

def main():
    string = input().strip().replace(" ", "")
    calculate_zeros(extract_coef(string))
if __name__ == "__main__":
    main()
