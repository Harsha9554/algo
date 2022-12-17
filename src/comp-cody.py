import sys

sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def gen_bin_helper(i, s, n, bin):
    if i == n:
        bin.append(s)
    else:
        gen_bin_helper(i + 1, s + "0", n, bin)
        gen_bin_helper(i + 1, s + "1", n, bin)


def gen_bin(n):
    bin = []
    gen_bin_helper(0, "", n, bin)
    return bin


def main():
    n = int(input())
    items = list(map(str, input().split()))
    res = []
    bin = gen_bin(n)
    for b in bin:
        # b = '1000'
        temp = []
        for i in range(n):
            if b[i] == "1":
                temp.append(items[i])
        res.append(temp)
    for item in res:
        print(item)


main()
