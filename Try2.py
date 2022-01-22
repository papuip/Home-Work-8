class Shop():
    name = None
    item = None
    q = None
    product = None
    choice = None
    sum = None
    def __init__(self,prod):
        self.product=prod

    def sayhi(self):
        while not bool(self.name):
            self.name=input("გამარჯობა ძვირფასო მომხარებელო,გთხოვთ მოგვწეროთ თქვენი სახელი:")

    def showmenu(self):
        print(self.product)

    def getchoice(self):
        while self.choice not in self.product:
            self.choice = input("რომელ პროდუქტს ინებებთ:")
            if self.choice not in self.product:
                print("აღნიშნული პროდუქტი არ გვაქვს")


    def getq(self):
        while not bool(self.q):
            self.q=((input("რამდენი გნებავთ:")))

    def calculatedsum(self):
        return self.product.get(self.choice)*int(self.q)

    def calculation(self):
        print(f"{self.name},თქვენი შეკვეთის ღირებულება არის: {self.calculatedsum()} ლარი")

    def BB(self):
        print(f"{self.name} მადლობთ რომ სარგებლობთ ჩვენი მომსახურებით, ნახვამდის")

products_list={"ბრაუნი":5,"ჩისკეიკი":4.2,"ლიმნის ნამცხვარი":3.5,"კოკა-კოლა":2.2}

shop=Shop(products_list)



shop.sayhi()
shop.showmenu()
shop.getchoice()
shop.getq()
shop.calculation()
shop.BB()

