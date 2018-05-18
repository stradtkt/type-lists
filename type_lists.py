def type(listType):
  #global variables for the functions to be used later
  string = ""
  sumOfList = 0
  for i in listType:
    if isinstance(i, str):
      string+= i + " "
      #isinstance(i, int) is checking to see if the item is an instance of int
    elif isinstance(i, int) or isinstance(i, float):
      sumOfList+=i
 #checking to see if there are strings and ints
  if len(string) > 0 and sumOfList > 0:
    print("The list you entered is of mixed type")
    print("String: ", string)
    print("Sum: ", sumOfList)
    #checking to see if there are only strings
  elif len(string) > 0:
    print("The list you entered is of string type")
    print("String: ", string)
    #checking to see if there are only ints
  else:
    print("The list you entered is of integer type")
    print("Sum: ", sumOfList)

list_1 = ['magical unicorns',19,'hello',98.98,'world']
type(list_1)

#output
# The list you entered is of mixed type
# String:  magical unicorns hello world
# Sum:  117.98

list_2 = [2,3,1,7,4,12]
type(list_2)

#output
# The list you entered is of integer type
# Sum:  29

list_3 = ['magical','unicorns']
type(list_3)

#ouput
# The list you entered is of string type
# String:  magical unicorns
