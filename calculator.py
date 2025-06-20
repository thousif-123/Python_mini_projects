from functools import reduce
import math
class calc:
    def __init__(self):
        print("Welcome to the calculator!")
        print("What operation do you want to perform:")
        choice={1:'Addition',2:'Subtraction',3:'Multiplication',4:'Division',5:'Square',6:'Cube',7:'Square-root',8:'cube-root',9:'Power',10:'Factorial',11:'Modulo',12:'Exponential',13:'Sine',14:'Cosine',15:'Tangent',16:'Mean',17:'Median',18:'Mode'}
        print(choice)
        
        self.choice=int(input("enter a choice: "))
       
    
    def addition(self):
        if(self.choice==1):
            a=[]
        
            choose=int(input("Enter how many numbers :"))
                
            for i in range(choose):
                s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                try:
                    numbers=int(input("enter numbers :"))
                    if(numbers!=s):
                        a.append(numbers)
                except ValueError:
                    print("enter number not string!")
                except Exception as e:
                    print(e)
                    
                
            print(f"Your entered numbers :{a}")
            print(f"Addition of the entered numbers :{sum(a)}")

    #subtraction
    def subtraction(self):
        if(self.choice==2):
            a=[]
            choose=int(input("enter how many numbers do you want to perform subtraction :"))
            for i in range(choose):
                try:
                    numbers=int(input("enter numbers: "))
                except ValueError:
                    print("enter numbers not string value!")
                except Exception as e:
                    print(e)
                a.append(numbers)
            print(f"Your entered numbers: {a}")
            
        #new subtraction function to use in "reduce-function".
            def new(x,y):
                return x-y
        
            sub=reduce(new,a)
            print(f"subtraction of entered numbers :{sub}")

    #mulitplication
    def multiplication(self):
        if(self.choice==3):
            a=[]
            choose=int(input("enter how many numbers do you want to perform Mulitiplication :"))
            for i in range(choose):
                try:
                    numbers=int(input("enter numbers: "))
                except ValueError:
                    print("enter numbers not string value!")
                except Exception as e:
                    print(e)
                a.append(numbers)
            print(f"Your entered numbers: {a}")
            
        #new subtraction function to use in "reduce-function".
            def new(x,y):
                return x*y
        
            multiply=reduce(new,a)
            print(f"Multiplication of entered numbers :{multiply}")
    
    #division
    def division(self):
        if(self.choice==4):
            try:
                a=int(input("enter first number :"))
                b=int(input("enter second number :"))
                print(f"division of {a} and {b} is :{a/b}")
            except ValueError:
                print("Enter number not string!")
            except ZeroDivisionError:
                print("Do not enter zero for division!")

    #squaring of numbers
    def square(self):
        if(self.choice==5):
            try:
                a=int(input("enter a number :"))
                print(f"the squaring of a number {a} is :{a**2}")
            except ValueError:
                print("enter number not string!")
            except Exception as e:
                print(e)

    #cube
    def cube(self):
        if(self.choice==6):
            try:
                a=int(input("enter a number :"))
                print(f"the cube of a number {a} is {a**3}")
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #square root
    def square_root(self):
        if(self.choice==7):
            try:
                number=int(input('enter a number :'))
                print(f'the square root of a {number} is :{number**0.5}')
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #cube root
    def cube_root(self):
        if(self.choice==8):
            try:
                number=int(input('enter a number :'))
                print(f'the cube root of a {number} is :{number**(1/3)}')
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #power
    def power(self):
        if(self.choice==9):
            try:
                x=int(input('enter a first number :'))
                y=int(input('enter a second number :'))

                print(f'the number {x} is raised to the power of{y} :{x**y}')
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #factorial
    def factorial(self):
        if(self.choice==10):
            try:
                x=int(input('enter a first number :'))
                if(x>=0):
                    print(f'the factorial of a {x} is {math.factorial(x)}')
                else:
                    print("Error: Factorial is not defined for negative numbers")
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)

    #modulo
    def modulo(self):
        if(self.choice==11):
            try:
                x=int(input('enter a first number :'))
                y=int(input('enter second number :'))
                print(f"modulo division of {x,y} is :{x%y}")
        
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #Exponential
    def exponential(self):
        if(self.choice==12):
            try:
                x=int(input('enter a first number :'))
                print(f'the exponential of a {x} is {math.exp(x)}')
            except ValueError:
                print("enter number not string !")
            except Exception as e:
                print(e)
    
    #Sine
    def trgno_sine(self):
        if(self.choice==13):
            try:
                number=int(input('enter a number :'))
                print(f"sine of the number {number} is :{math.sin(number)}")
            except ValueError:
                print("enter number not string!")
            except Exception as e:
                print(e)
    #cosine
    def trigno_cosine(self):
        if(self.choice==14):
            try:
                number=int(input('enter a number :'))
                print(f"cosine of the number {number} is :{math.cos(number)}")
            except ValueError:
                print("enter number not string!")
            except Exception as e:
                print(e)
    #tangent
    def trigno_tangent(self):
        if(self.choice==15):
            try:
                number=int(input('enter a number :'))
                print(f"tan of the number {number} is :{math.tan(number)}")
            except ValueError:
                print("enter number not string!")
            except Exception as e:
                print(e)
    #Mean
    def mean(self):
        if(self.choice==16):
            choose=int(input("enter how many numbers do you want to take :"))
            numbers=[]
            for i in range(choose):
                x=int(input("enter numbers :"))
                numbers.append(x)
            print(f"original list of numbers :{numbers}")
            s_of_numbers=sum(numbers)
            print(f"Mean Value :{s_of_numbers/len(numbers)}")
    
    


            
            
            
    


    



                                
            
obj=calc()
obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()
obj.square()
obj.cube()
obj.square_root()
obj.cube_root()
obj.power()
obj.factorial()
obj.modulo()
obj.exponential()
obj.trgno_sine()
obj.trigno_cosine()
obj.trigno_tangent()
obj.mean()


       