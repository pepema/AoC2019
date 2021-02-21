import itertools 

class CrossedWires:
  def __init__(self):
    self.wire1 = []
    self.wire2 = []
    self.intersections = []

  def FillMap(self, input, wire):
    x = px = y = py = 0
    #don't forget to add the central station aswell
    wire.append((x,y))
    for element in input:
      if 'U' in element:
        py = y
        y += int(element.replace('U',''))
        while py < y:
          py += 1
          wire.append((x,py))
      if 'D' in element:
        py = y
        y -= int(element.replace('D',''))
        while py > y:
          py -= 1
          wire.append((x,py))
      if 'R' in element:
        px = x
        x += int(element.replace('R',''))
        while px < x:
          px += 1
          wire.append((px,y))
      if 'L' in element:
        px = x
        x -= int(element.replace('L',''))
        while px > x:
          px -= 1
          wire.append((px,y))
    return wire

  def GetIntersections(self):
    self.wire1.sort(key=lambda tup: (tup[0],tup[1]))
    self.wire2.sort(key=lambda tup: (tup[0],tup[1]))
    
    for elem in self.wire1:
      for x in self.wire2:
        if elem == x:
          self.intersections.append(elem)
        #Brute force search not fast enough since coordinate system is huge
        #Need to trim front of second list when possible
        while self.wire2 and self.wire2[0][0] < elem[0]:
          self.wire2.pop(0)
        #Need to stop looking if not needed
        if x[0] > elem[0]:
          break

  def CalculateShortestDistanse(self):
    shortest = 999999999
    #ignore central port
    self.intersections.remove((0,0))
    for intersection in self.intersections:
      distance = abs(intersection[0]) + abs(intersection[1])
      if distance < shortest:
        shortest = distance
    return shortest

  def Run(self):
    f = open("input.txt", "r")
    self.FillMap(f.readline().split(','), self.wire1)
    self.FillMap(f.readline().split(','), self.wire2)
    self.GetIntersections()
    print(self.CalculateShortestDistanse())

  
if __name__ == "__main__":
  cw = CrossedWires()
  cw.Run()
  