import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count=0
    while(n != 1):
        count=count+1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count   # the last print is 1
  
def graph(upperbound=None):
  turtle1=turtle.Turtle()
  turtle2=turtle.Turtle()
  window=turtle.Screen()
  max_so_far=0
  window.setworldcoordinates(0,0,10,10)
  for i in range(1, upperbound+1):
    window.setworldcoordinates(0,0,i+10,max_so_far+10)
    result=seq3np1(i)
    if result>max_so_far:
      max_so_far=result
      turtle1.penup()
      turtle1.goto(x=i,y=result)
      turtle1.write("Max so far:"+str(max_so_far),False)
      turtle2.pendown()
    turtle2.goto(i,result)
  window.exitonclick()

def main():
  start=int(input("enter your number here:"))
  if start<0:
    exit()
  for i in range(1, start+1):
    count=seq3np1(i)
    print("starting number", i)
    print("number of iterations", count)
  graph(upperbound=start)

main()
