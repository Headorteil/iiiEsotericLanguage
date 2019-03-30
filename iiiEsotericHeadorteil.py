#!/usr/bin/env python

from __future__ import print_function
import argparse
import sys

def encode(a, code):
    n = len(a)
    result = 0
    j = 0
    for i in range(len(code)):
        if code[i] in a:
            result += (1 + a.index(code[i]))*(n ** j)
            j += 1
    return result

def decode(a, code):
    n = len(a)
    result = []
    while code > 0:
        temp = (code-1) % n
        result.append(a[temp])
        code -= temp
        code //= n
    result = ''.join(result)
    return result

def bf(src, left, right, data, idx):
    # Thanks to DoctotLai, I found his code here : https://github.com/DoctorLai/PyUtils/blob/master/bf.py
    if len(src) == 0: return
    if left < 0: left = 0
    if left >= len(src): left = len(src) - 1
    if right < 0: right = 0
    if right >= len(src): right = len(src) - 1
    arr = [0] * 30000
    ptr = 0
    i = left
    while i <= right:
        s = src[i]
        if s == '>':
            ptr += 1
            if ptr >= len(arr):
                ptr = 0
        elif s == '<':
            ptr -= 1
            if ptr < 0:
                ptr = len(arr) - 1
        elif s == '+':
            arr[ptr] += 1
        elif s == '-':
            arr[ptr] -= 1
        elif s == '.':
            print(chr(arr[ptr]), end="")
        elif s == ',':
            if idx >= 0 and idx < len(data):
                arr[ptr] = ord(data[idx])
                idx += 1
            else:
                arr[ptr] = 0
        elif s =='[':
            if arr[ptr] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = src[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = src[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1

def executebf(code, data):
    a = "><+-.,[]"
    intelligible = decode(a,code)
    bf(intelligible, 0, len(intelligible) - 1, data, 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='iii Encoder/Decoder/Executer (deals with BrainFuck)', epilog='Examples : \n$ ./iiiEsotericHeadorteil.py -c -a"++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." -n"yes"\n$ ./iiiEsotericHeadorteil.py -d -n11394260736961616017478696325142642241587016089942641935756584435039981423330228839638374655156139739 -o"./file"\n$ ./iiiEsotericHeadorteil.py -e -n11394260736961616017478696325142642241587016089942641935756584435039981423330228839638374655156139739\n$ ./iiiEsotericHeadorteil.py -e -n12250030 -b"yay"')
    parser.add_argument('-a', help='Specify/Print the string of your BrainFuck program (input or output) give this option "yes" if it is use for an output')
    parser.add_argument('-n', help='Specify/Print the number of i your programm would contain (if you don\'precise this option in -c mode, be careful, iii programms can be really huge and you may have an overflow error) (input or output) give this option "yes" if it is use for an output')
    parser.add_argument('-p', help='Specify the path of your iii file (input or output)')
    parser.add_argument('-o', help='Specify the path of your BrainFuck file(input or output)')
    parser.add_argument('-b', help='Specify the input of your iii programm')
    parser.add_argument('-e', help='Execute your programm', action='store_true')
    parser.add_argument('-d', help='Convert your iii program to BrainFuck', action='store_true')
    parser.add_argument('-c', help='Convert your BrainFuck program to iii', action='store_true')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if not args.e and not args.d and not args.c:
        print("You must choose an action : decode, encode or execute")
        sys.exit(1)

    if (args.e and args.d) or (args.e and args.c) or (args.d and args.c):
        print("You must choose between decode, encode or execute")
        sys.exit(1)

    if args.n is not None and args.p is not None:
        print("You must choose either you iii program is/will output in a file or under the form of the number of i your file would contain")
        sys.exit(1)

    if args.a is not None and args.o is not None:
        print("You must choose either you BrainFuck program is in a file or in a string argument")
        sys.exit(1)

    if args.e and (args.a is not None or args.o is not None):
        print("This program can only execute iii program")
        sys.exit(1)

    if args.e and (args.n is None and args.p is None):
        print("You must specify a iii program to execute")
        sys.exit(1)

    if args.b is not None and not args.e:
        print("You can't give arguments to your iii program if you don't want to execute it")
        sys.exit(1)


    if args.d and (args.n is None and args.p is None):
        print("You must specify a iii program in input")
        sys.exit(1)

    if args.d and (args.a is None and args.o is None):
        print("You must specify an output method for your BrainFuck")
        sys.exit(1)

    if args.d and args.a is not None and args.a != "yes":
        print("You must give the a option : \"yes\" value")
        sys.exit(1)

    if args.c and (args.a is None and args.o is None):
        print("You must specify an output method for your iii")
        sys.exit(1)

    if args.c and (args.n is None and args.p is None):
        print("You must specify a BrainFuck program in input")
        sys.exit(1)

    if args.c and args.n is not None and args.n != "yes":
        print("You must give the n option : \"yes\" value")
        sys.exit(1)


    if args.e:
        if args.p is not None:
            f = open(args.p, 'r')
            code = len(f.read())
            f.close()
        else:
            code = int(args.n)
        if args.b is not None:
            data = args.b
        else:
            data = ""
        executebf(code, data)

    if args.d:
        if args.p is not None:
            f = open(args.p, 'r')
            code = len(f.read())
            f.close()
        else:
            code = int(args.n)
        res = decode("><+-.,[]", code)
        if args.o is not None:
            f = open(args.o, 'w')
            f.write(res)
            f.close()
            print("File was correctly edited")
            sys.exit(1)
        print(res)
        sys.exit(1)

    if args.c:
        if args.o is not None:
            f = open(args.o, 'r')
            code = f.read()
            f.close()
        else:
            code = args.a
        res = encode("><+-.,[]", code)
        if args.p is not None:
            f = open(args.p, 'w')
            f.write(res*"i")
            f.close()
            print("File was correctly edited") # If this line is print one day I would be really surprised xD
            sys.exit(1)
        print(res)
        sys.exit(1)
