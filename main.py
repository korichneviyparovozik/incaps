class Company:
    money = 50000
    age_yrs = 10

    def company(self):
        pass


class Office(Company):
    materials = 15000

    def office(self):
        pass


class Worker(Office):
    budget = 15000
    age = 25

    def worker(self):
        print(self.budget)
        print(self.age)
