#Ask user for a number, print out the number as even or odd

class number_checker:
    def __init__(self):

        pass

    def ask_number(self):
        num = int(float(input("Give me a number: ")))
        self.num = num

    def check_number(self):

        if self.num % 2 == 0:
            print("Even")
        else:
            print("Odd")

        #additional logic"
        # Is a negative and zero taken into account as valid numbers? 
        #if num > 0:
        #What is the user inputs a string? 
        #if isnumeric(num):
        #What is the user doesn't eventer anything? 
        #if num: -- i think this works, test it
        #WHat is the number is a float?
        #if isinstance(num, int) or isinstance(num, float):

if __name__ == "__main__":

    nc = number_checker()
    nc.ask_number()
    nc.check_number()