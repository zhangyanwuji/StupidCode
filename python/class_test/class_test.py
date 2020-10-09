import json

def class_test():
    class Complex_number:
        """A simple class"""
        def __init__(self, real, imaginary):
            self.r = real
            self.i = imaginary


    x = Complex_number(4, 5)
    print(x.r, x.i)


def class_var_test():
    class dog:

        have_fur = 'yes'


        def __init__(self, name):
            self.name = name
            self.tricks = []


        def learn_a_trick(self, trick):
            self.tricks.append(trick)


    my_dog = dog('Fib')
    my_dog.learn_a_trick('hand shake')
    print(my_dog.tricks, my_dog.have_fur,  my_dog.name)


def Income_calc():
    class mnth:


        def __init__(self, month,  actual_in, basic_in, bounus, insurance_cost, tax):
            self.month = month
            self.actual_in = actual_in
            self.basic_in = basic_in
            self.bounus = bounus
            self.insurance_cost = insurance_cost
            self.tax = tax


        def show_income(self):
            print()
            print("Month:", self.month)
            print("actual_in:", self.actual_in)
            print("basic_in:", self.basic_in)
            print("bounus:", self.bounus)
            print("insurance_cost:", self.insurance_cost)
            print("tax:", self.tax)


        def store(self):
            data = {
                "month": self.month,
                "actual_in": self.actual_in,
                "basic_in": self.basic_in,
                "bounus": self.bounus,
                "insurance_cost": self.insurance_cost,
                "tax": self.tax
            }

            with open("data_file.json", "w") as write_file:
                json.dump(data, write_file)


        def load(self):
            with open("data_file.json", "r") as read_file:
                data = json.load(read_file)


    Jul_in = mnth(month = "Jul", actual_in = 17745, basic_in = 13600, bounus = 7521, insurance_cost = -2967, tax = -394)
    Jul_in.show_income()
    Jul_in.store()

    Aug_in = mnth(month = "Aug", actual_in = 17745, basic_in = 13600, bounus = 7521, insurance_cost = -2967, tax = -394)
    Aug_in.show_income()
    Aug_in.store()

    Sep_in = mnth(month = "Sep", actual_in = 17745, basic_in = 13600, bounus = 7521, insurance_cost = -2967, tax = -394)
    Sep_in.show_income()
    Sep_in.store()


def json_test():
    data = {
        "Jul": {
            "actual_in": 16924.82,
            "basic_in": 13600,
            "bounus": 7372.75,
            "insurance_cost": -3227.0,
            "tax": 214.63
        },
        "Aug": {
            "actual_in": 18919.06,
            "basic_in": 13600,
            "bounus": 8746.7,
            "insurance_cost": -2967.0,
            "tax": 445.64
        },
        "Sep": {
            "actual_in": 17745,
            "basic_in": 13600,
            "bounus": 7521,
            "insurance_cost": -2967.0,
            "tax": 394
        }
    }


    with open('data_file.json') as f:
        data = json.load(f)
        print(json.dumps(data, indent = 4, sort_keys=True))

#    with open("data_file.json", "w") as write_file:
#        json.dump(data, write_file)
