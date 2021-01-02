def IntcodeOutput(noun,verb):
  with open("input.txt","r") as file:
    data = list(map(int,file.read().replace('\n','').split(",")))
    data[1]=noun
    data[2]=verb
    for index,x in enumerate(data[0::4]):
      x = data[index*4]
      if x == 1:
        data[data[index*4+3]] = data[data[index*4+1]] + data[data[index*4+2]]
      elif x == 2:
        data[data[index*4+3]] = data[data[index*4+1]] * data[data[index*4+2]]
      elif x == 99:
        break
    return data[0]

def FindNounVerb(expected_ouput):
  for noun in range(99):
    for verb in range(99):
      if(IntcodeOutput(noun,verb)==expected_ouput):
        return 100*noun+verb

if __name__ == "__main__":
  print(IntcodeOutput(12,2))
  print(FindNounVerb(19690720))