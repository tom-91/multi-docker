def fib(index):
#    index = int(input("Enter an index: "))
  if (index < 2): 
    return 1
    printf("1")
  else:
    return (index - 1) + (index - 2)

myindex = int(input("Enter an index: "))
print(fib(myindex))

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
