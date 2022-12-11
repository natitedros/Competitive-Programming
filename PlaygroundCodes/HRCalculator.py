class Lit:
    def __init__(self, ex):
        # return string value and evaluated value
        self.value = [str(ex), ex]
        
    def Add(self, ex):
        x = "(" + self.value[0] + " + " + ex.value[0] + ")"
        y = self.value[1] + ex.value[1]
        
        res = Lit(y)
        res.value[0] = x
        return res
    
    def Sub(self, ex):
        x = "(" + self.value[0] + " - " + ex.value[0] + ")"
        y = self.value[1] - ex.value[1]
        
        res = Lit(y)
        res.value[0] = x
        return res
    
    def Mul(self, ex):
        x = "(" + self.value[0] + " * " + ex.value[0] + ")"
        y = self.value[1] * ex.value[1]
        
        res = Lit(y)
        res.value[0] = x
        return res
    
    def toString(self):
        return self.value[0]
        
    def simplify(self):
        return Lit(self.value[1])
    
class Var:
    def __init__(self, ex):
        # return string value and evaluated value
        self.value = [ex, ex]
        
    def Add(self, ex):
        x = "(" + self.value[0] + " + " + ex.value[0] + ")"
        y = "(" + self.value[1] + " + " +  str(ex.value[1]) + ")"
        
        res = Var(y)
        res.value[0] = x
        return res
        
    def Sub(self, ex):
        x = "(" + self.value[0] + " - " + ex.value[0] + ")"
        y = "(" + self.value[1] + " - " +  str(ex.value[1]) + ")"
        
        res = Var(y)
        res.value[0] = x
        return res
        
    
    def Mul(self, ex):
        x = "(" + self.value[0] + " * " + ex.value[0] + ")"
        y = "(" + self.value[1] + " * " +  str(ex.value[1]) + ")"
        
        res = Var(y)
        res.value[0] = x
        return res
        
    
    def toString(self):
        return self.value[0]
        
    def simplify(self):
        return Lit(self.value[1])

# Insert code here
class Lit:
    def __init__(self, num):
        self.value = num
        self.display = str(num)
    
    def Add(self, exp):
        disp = "(" + self.display + " + " + exp.display + ")"
        val = self.value + exp.value
        ans = Lit(val)
        ans.display = disp
        return ans
        
    def Sub(self, exp):
        disp = "(" + self.display + " - " + exp.display + ")"
        val = self.value - exp.value
        ans = Lit(val)
        ans.display = disp
        return ans
        
    def Mul(self, exp):
        disp = "(" + self.display + " * " + exp.display + ")"
        val = self.value * exp.value
        ans = Lit(val)
        ans.display = disp
        return ans
        
    def toString(self):
        return self.display
        
    def simplify(self):
        return Lit(self.value)
    
class Var:
    def __init__(self, exp):
        self.display = exp
    
    def Add(self, exp):
        disp = "(" + self.display + " + " + exp.display + ")"
        ans = Var(disp)
        return ans
        
    def Sub(self, exp):
        disp = "(" + self.display + " - " + exp.display + ")"
        ans = Var(disp)
        return ans
        
    def Mul(self, exp):
        disp = "(" + self.display + " * " + exp.display + ")"
        ans = Var(disp)
        return ans
        
    def toString(self):
        return self.display
        
    def simplify(self):
        return Lit(self.display)