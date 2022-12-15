import sys
sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")

def gen_bin_helper(i, s, n, bin):
    if i == n:
        bin.append(s)
    else:
        gen_bin_helper(i+1, s+'0', n, bin)
        gen_bin_helper(i+1, s+'1', n, bin)

def gen_bin(n):
    bin = []
    gen_bin_helper(0, "", n, bin)
    return bin

def square_it(n):
    return n**2

def cube_it(n):
    return n**3

def main():
    n = int(input())
    bin = gen_bin(n)
    for b in bin:
        print(b)


main()
