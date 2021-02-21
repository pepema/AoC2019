class SecureContainer:
  def __init__(self):
    self.valid_passwords = []

  def Valid(self,pw):
    password = list(str(pw))
    adjacent = []
    if password != sorted(password):
      return False

    for i in range(len(password)-1):
      if password[i] == password[i+1]:
        adjacent.append(password[i])

    for elem in adjacent:
      #swap to >= for Part 1
      if adjacent.count(elem) == 1:
        return True

    return False

  def Passwords(self,min,max):
    for i in range(min,max+1):
      if self.Valid(i):
        self.valid_passwords.append(i)

  def Run(self):
    self.Passwords(246515,739105)
    print(len(self.valid_passwords))
  
if __name__ == "__main__":
  sc = SecureContainer()
  sc.Run()