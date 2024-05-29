class Test1:
     def __init__(self):
        print("Create")
def fun1():
     print("__name__:"+__name__)
     print("func1")

if __name__ == "__main__":
     print("========Start Test!!=====")
     fun1()
     test1 = Test1()
     print("========End Test!!=====")
