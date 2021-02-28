#You are painting a wall. The instructions on the paint can says that
#1 can of paint can cover 5 square meters of wall. Given a random height and
#width of wall, calculate how many cans of paint you'll need to buy.


import math
def paint_calc(height,width,cover):
   #eval_this=round((height*width)/cover)
   print(f'{math.ceil((height*width)/cover)} cans are required')


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
# below parameters are keyword arguments
paint_calc(height=test_h, width=test_w, cover=coverage)
