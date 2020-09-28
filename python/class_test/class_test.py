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
