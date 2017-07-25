def get_input():
    return input("How many sandwiches can you eat?")
    
def you_lose(count, bro):
    if count <= 4:
        print "You said, ", count, " but my brother can eat ", bro
    else:
        print "You will get sick if you eat", count, "sandwiches!"
    print "Therefore, you lost!!!:("
def baby_message():
    print "You will get sick if you eat", count, "sandwiches!"
while True:   
    count = get_input()
    if count < 0:
      my_brother = count + 1
      you_lose(count, my_brother)
baby_message()     
  
  