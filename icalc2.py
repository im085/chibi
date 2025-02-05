class Expr( object ):
    @classmethod
    def new(cls , v):
        if isinstance (v, Expr):
            return v
        return Val(v)

class Val(Expr):
    __slot__ = ["value "]
    def __init__(self , value):
        self.value = value
    def __repr__(self):
        return f"Val ({ self . value }) "
    def eval (self , env: dict ):
        return self.value

class Binary(Expr):
    __slot__ = ["left ", "right "]
    def __init__(self , left , right):
        self.left = Expr.new(left)
        self.right = Expr.new(right)
    def __repr__(self):
        classname = self.__class__.__name__
        return f"{ classname }({ self . left },{ self . right }) "

class Add(Binary):
    __slot__ = ["left ", "right "]
    def eval (self , env: dict ):
        return self.left. eval (env) + self.right. eval (env)

class Sub(Binary):
    __slot__ = ["left ", "right "]
    def eval (self , env: dict ):
        return self.left. eval (env) - self.right. eval (env)

class Mul(Binary):
    __slot__ = ["left ", "right "]
    def eval (self , env: dict ):
        return self.left. eval (env) * self.right. eval (env)

class Div(Binary):
    __slot__ = ["left ", "right "]
    def eval (self , env: dict ):
        return self.left. eval (env) // self.right. eval (env)

class Mod(Binary):
    __slot__ = ["left ", "right "]
    def eval (self , env: dict ):
        return self.left. eval (env) % self.right. eval (env)