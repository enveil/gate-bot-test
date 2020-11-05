import time

print("Hello world!")

def foo2(text):
    print("foo " + text)

if __name__ == "__main__":
    time.sleep(30)
    foo2("baz")
    foo2("bar")
    foo2("yes")
