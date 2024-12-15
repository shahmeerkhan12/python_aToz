# if __name__ = "__main__"
# *******************************

# python interpreter sets special variables, one of which is ' __name__ '
# python interpreter will assign it a value of '__main__' if it is the initial module being run

def main():
   print("hello!")
# now by the including the statement if __name__ = "__main__", we want to check that if the current 
# module is running direclty or indirectly
if __name__ == '__main__':
   pass
else:
   print("running other modules indirectly")
 
