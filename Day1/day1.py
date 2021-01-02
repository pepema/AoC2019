def RecursiveFuelCalc(mass):
  fuel = int(int(mass)/3)-2
  return fuel + RecursiveFuelCalc(fuel) if fuel > 0 else 0

def Second():
  masses = open("input.txt","r")
  sum = 0
  for mass in masses:
    sum += RecursiveFuelCalc(mass)
  return sum

def First():
  data = open("input.txt","r")
  sum = 0
  for elem in data:
    sum += int(int(elem)/3)-2
  return sum

if __name__ == "__main__":
  print(First())
  print(Second())