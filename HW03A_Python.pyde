diamSmall = 10
diamLarge = 3 * diamSmall

def setup():
  size(800, 600)
  
def draw():
  background(255,215,0)
  stroke(0)

  fill(0)
  for x in range(0, 800, 5 * diamSmall):
    print(x)                                                
    for y in range(0, 600, 5 * diamSmall):
        print(y)
        ellipse(x, y, diamSmall, diamSmall)
    
  for x in range(0, 800, 2 * 5 * diamSmall):
    print(x)
    for y in range(0, 600, 2 * 5 * diamSmall):
        print(y)
        ellipse(x, y, diamLarge, diamLarge)
    
  pushMatrix()
  translate(5 * diamSmall, 5 * diamSmall)
  for x in range(0, width, 2 * 5 * diamSmall):
    print(x)
    for y in range(0, height, 2 * 5 * diamSmall):
        print(y)     
        ellipse(x, y, diamLarge, diamLarge)
  popMatrix()
