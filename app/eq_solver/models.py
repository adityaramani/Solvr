import math
class Equation():


    def __init__(self,**kwargs):
        '''
        self.variables = {}
        self.variables['x'] = {}
        self.variables['x']['coeff'] = kwargs['x']['coeff']
        self.variables['x']['exponent'] = kwargs['x']['exponent']
        '''
        self.variables = kwargs


class Simple(Equation):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def solve(self):
        ans = {}
        if self.variables["x_coeff"] == 0:
            self.solution =  {"x" : ":("}
        else:
            ans['x'] = round(self.variables['rhs'] / self.variables['x_coeff'],3)
            if self.variables['x_expo'] == 0 and ans['x'] != 1:
                self.solution =  {"x" : ":("}
            else:
                self.solution = ans

class Simultaneous(Equation):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def solve(self, other):
        this = self.variables
        other = other.variables

        a = this['y_coeff'] * -other['rhs'] - other['y_coeff'] * -this['rhs']
        b = -this['x_coeff'] * -other['rhs'] + other['x_coeff'] * -this['rhs']
        c = this['x_coeff'] * other['y_coeff'] - other['x_coeff'] * this['y_coeff']
        print(a,b,c)
        if c == 0:
            self.solution = {'x': ":(" , "y" : ":("}
        else:
            self.solution = {}
            self.solution['x'] = round(a/c,3)
            self.solution['y'] = round(b/c,3)


class Quadratic(Equation):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def solve(self):
        this = self.variables
        D = this['x_coeff']**2  - 4*this['x2_coeff'] * -this['rhs']
        print(D)
        if D < 0 :
            self.solution = {'x1': ":( " , "x2" : ":("}

        else:
            D = int(D**0.5)
            print(D)
            print(this['x_coeff'], "Coeff ")
            x1 = (-this['x_coeff'] + D) / (2*this['x2_coeff'])
            x2 = (-this['x_coeff'] - D) / (2*this['x2_coeff'])

            self.solution = {}
            self.solution['x1'] = round(x1,3)
            self.solution['x2'] = round(x2,3)
