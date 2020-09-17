import sys

def handle(req):
    print("Hello: " + req)

def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf

if __name__ == "__main__":
    st = get_stdin()
    ret = handle(st)
    if ret != None:
        print(ret)
