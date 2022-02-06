import pandas as pd 

df = pd.read_excel('shourya.xlsx')

class User:
  @staticmethod
  def login():
    welcome = input("Do you have an acount? y/n: ")
    if welcome == "n":
      while True:
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(username + ".txt", "w")
            file.write(username + ":" + password)
            file.close()
            welcome = "y"
            break
        print("Passwords do not match!")
 
    if welcome == "y":
      while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(login1 + ".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1 + ":" + login2:
            print("Welcome")
            break
        print("Incorrect username or password.")

class Orderbook:
  buy_order = []
  sell_order = []
  feeLadder = 0
  total = 0
  completeorders = []
  partialorders = []

  def init_(self , buy_order ,sell_order ):
    for value in df.values.tolist():
        if value[5] == -1:
          self.buy_order.append(value)
        elif value[5] == 1:
          self.sell_order.append(value)

    print(self.b_order)
    print(self.s_order)


    print("Enter your choice:")
    print("1. Add order:")
    print("2. Delete order:")
    while True:
      try:
          x = int(input("Please enter a number: "))
          break
      except ValueError:
          print("Oops!  That was no valid number.  Try again...")

  def neworder(self,b_order,s_order):
      self.b_order.append(b_order)
      self.s_order.append(s_order)

  def cancelorder(self,b_order,s_order):
      self.b_order.delete(b_order)
      self.s_order.delete(s_order)

  def tradeValue():
    for value in df.values.tolist():
      if value[3] > 100:
        feeLadder = value[3] * 0.10
        print("Fee Ladder :" + feeLadder)
      
      elif value[3] <= 100:
        feeLadder = value[3] * 0.20
        print(feeLadder)

  def orderstatus(self):
    for value in df.values.tolist():
      if value[1] == 5:
        self.completeorsers.append(value)
      elif value[1] !=5:
        self.partialorders.append(value)

    print("Completely Fulfilled Orders:" + self.completeorders)
    print("Partially Fulfilled Orders:" + self.partialorders)



    ob = Orderbook()
    ob.tradeValue() 
    ob.orderstatus()


class Sort:
  msft_list = [] 
  amzn_list = []
  goog_list = []
  aapl_list = []
  intc_list = []

  def startorders(self):
    for value in df.values.tolist():
        if value[6] == 'MSFT':
            self.msft_list.append(value)
        elif value[6] == 'AMZN':
            self.amzn_list.append(value)
        elif value[6] == 'GOOG':
            self.goog_list.append(value)
        elif value[6] == 'AAPL':
            self.aapl_list.append(value)
        elif value[6] == 'INTC':
            self.intc_list.append(value)

    print(self.msft_list)
    print(self.amzn_list)
    print(self.goog_list)
    print(self.aapl_list)
    print(self.intc_list)

so = Sort()
so.startorders()