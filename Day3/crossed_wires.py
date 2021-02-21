import itertools 

class CrossedWires:
  def __init__(self):
    self.wire1 = []
    self.sorted_wire1 = []
    self.wire2 = []
    self.sorted_wire2 = []
    self.intersections = []
    self.closest_intersection = (0,0)

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
    self.sorted_wire1 = sorted(self.wire1, key=lambda tup: (tup[0],tup[1]))
    self.sorted_wire2 = sorted(self.wire2, key=lambda tup: (tup[0],tup[1]))
    
    for elem in self.sorted_wire1:
      for x in self.sorted_wire2:
        if elem == x:
          self.intersections.append(elem)
        #Brute force search not fast enough since coordinate system is huge
        #Need to trim front of second list when possible
        while self.sorted_wire2 and self.sorted_wire2[0][0] < elem[0]:
          self.sorted_wire2.pop(0)
        #Need to stop looking if not needed
        if x[0] > elem[0]:
          break

  def CalculateSteps(self):
    min_steps = 9999999
    for intersection in self.intersections:
      steps = 0
      for i in range(len(self.wire1)):
        if self.wire1[i] == intersection:
          steps = i
      for i in range(len(self.wire2)):
        if self.wire2[i] == intersection:
          steps += i
      if steps < min_steps:
        min_steps = steps
    return min_steps

  def CalculateShortestDistanse(self):
    shortest = 999999999
    #ignore central port
    self.intersections.remove((0,0))
    for intersection in self.intersections:
      distance = abs(intersection[0]) + abs(intersection[1])
      if distance < shortest:
        shortest = distance
        self.closest_intersection = intersection
    return shortest

  def Run(self):
    f = open("input.txt", "r")
    self.FillMap(f.readline().split(','), self.wire1)
    self.FillMap(f.readline().split(','), self.wire2)
    self.GetIntersections()
    print(self.CalculateShortestDistanse())
    print(self.CalculateSteps())

  
if __name__ == "__main__":
  cw = CrossedWires()
  cw.Run()
  