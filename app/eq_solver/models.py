
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
        ans['x'] = self.variables['RHS'] / self.variables['x']['coeff']
        if self.variables['x']['exponent'] == 0 and ans['x'] != 1:
            self.solution = None
        else:
            self.solution = ans

class Simultaneous(Equation):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def solve(self, other):
        this = self.variables
        other = other.variables

        a = this['y']['coeff'] * other['RHS'] - other['y']['coeff'] * this['RHS']
        b = -this['x']['coeff'] * other['RHS'] + other['x']['coeff'] * this['RHS']
        c = this['x']['coeff'] * other['y']['coeff'] - other['x']['coeff'] * this['y']['coeff']

        if c == 0:
            self.solution = None
        else:
            self.solution = {}
            self.solution['x'] = a/c
            self.solution['y'] = b/c


class Quadratic(Equation):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def solve(self):
        this = self.variables

        D = this['x']['coeff']**2  - 4*this['x2']['coeff'] * this['c']

        if D < 0 :
            this.solution = None
        else:
            D = D**0.5
            x1 = (-this['x'] + D) / 2*this['x2']
            x2 = (-this['x'] - D) / 2*this['x2']

            this.solution = {}
            this.solution['x1'] = x1
            this.solution['x2'] = x2
