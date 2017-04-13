def READ(a):
    return a
def EVAL(a):
    return a
def PRINT(a):
    return a
def rep(i):
    r = READ(i)
    e = EVAL(r)
    p = PRINT(e)
    return p
def main():
    while True:
        try:
            line = raw_input('user> ')
            print rep(line)
        except EOFError:
            # probably Ctrl+D
            return

if __name__ == '__main__': main()
