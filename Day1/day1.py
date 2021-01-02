def RecursiveFuelCalc(mass):
  fuel = int(int(mass)/3)-2
  return fuel + RecursiveFuelCalc(fuel) if fuel > 0 else 0

def RocketEquation(part):
  data = open("input.txt","r")
  sum = 0
  for mass in data:
    if part == 1:
      sum += int(int(mass)/3)-2
    elif part == 2:
      sum += RecursiveFuelCalc(mass)
  return sum

if __name__ == "__main__":
  print(RocketEquation(1))
  print(RocketEquation(2))