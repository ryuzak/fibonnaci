import sys

def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('missing arg')
    else:
        print(f'the fibonnaci value for index {sys.argv[1]} is {fib(int(sys.argv[1]))}')