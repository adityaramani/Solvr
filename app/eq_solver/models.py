
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