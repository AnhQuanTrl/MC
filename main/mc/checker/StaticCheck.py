#1712830
"""
 * @author tlaquan
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None, isCheck=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isCheck = isCheck

class StaticChecker(BaseVisitor,Utils):

    global_envi = [[
    Symbol("getInt",MType([],IntType())),
    Symbol("putInt",MType([IntType()],VoidType())),
    Symbol("putIntLn",MType([IntType()],VoidType())),
    Symbol("getFloat",MType([],FloatType())),
    Symbol("putFloat",MType([FloatType()],VoidType())),
    Symbol("putFloatLn",MType([FloatType()],VoidType())),
    Symbol("putBool",MType([BoolType()],VoidType())),
    Symbol("putBoolLn",MType([BoolType()],VoidType())),
    Symbol("putString",MType([StringType()],VoidType())),
    Symbol("putStringLn",MType([StringType()],VoidType())),
    Symbol("putLn",MType([],VoidType()))
    ],[]]
    
    
    def __init__(self,ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def flatten(self, lst):
        return [i for x in lst for i in x]
    def visitParDecl(self, ast, c):
        if self.lookup(ast.variable, c[0], lambda x: x.name):
            raise Redeclared(Parameter(), ast.variable)
        return [Symbol(ast.variable, ast.varType, isCheck=True)]
    def process(self, ast, c, index):
        if isinstance(ast, FuncDecl):
            temp = c[:-1] + [c[-1] + [c[0][index]]]
            envi_table = reduce(lambda x,y: [x[0] + self.visitParDecl(y,x)] + x[1:],ast.param,[[]]+temp)
            for i,x in enumerate(ast.body.member):
                temp = self.visitMember(x, envi_table)
                if temp and isinstance(temp[0], Symbol) and temp[0].name == "return":
                    for y in ast.body.member[i+1:]:
                        if isinstance(y, Stmt):
                            raise UnreachableStatement(y)
                envi_table = [envi_table[0] + temp] + envi_table[1:]
            #envi_table = reduce(lambda x,y: [x[0] + self.visit(y,x)] + x[1:],ast.body.member, envi_table)[0]
            if not isinstance(ast.returnType, VoidType):
                if not self.lookup("return", envi_table[0], lambda x: x.name):
                    raise FunctionNotReturn(ast.name.name)
    

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        builtin_length = len(c[0])
        t = c[:]
        for x in t[0]:
            x.isCheck = True
        envi_table = reduce(lambda x,y: [x[0]+self.visit(y, x)] + x[1:],ast.decl,t)
        for x in envi_table[0]:
            if not isinstance(x.mtype, MType):
                x.isCheck = True
        if all(not (x.name == "main" and isinstance(x.mtype, MType)) for x in envi_table[0]):
            raise NoEntryPoint()
        for i,x in enumerate(ast.decl):
            self.process(x,envi_table,builtin_length + i)
        for x in envi_table[0][builtin_length:]:
            if isinstance(x.mtype, MType) and x.name != "main":
                if x.isCheck != True:
                    raise UnreachableFunction(x.name)

    def visitFuncDecl(self,ast, c): 
        if self.lookup(ast.name.name, c[0], lambda x: x.name):
            raise Redeclared(Function(), ast.name.name)
        return [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType))]
    
    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable, c[0], lambda x: x.name):
            raise Redeclared(Variable(), ast.variable)
        if isinstance(ast.varType, (ArrayType, ArrayPointerType)):
            return [Symbol(ast.variable, ast.varType, isCheck=True)]
        return [Symbol(ast.variable, ast.varType)]

    def visitBlock(self, ast, c):
        #env = reduce(lambda x,y: [x[0] + self.visit(y,x)] + x[1:], ast.member, [[]]+c)
        env = [[]] + c
        for i,x in enumerate(ast.member):
            temp = self.visitMember(x,env)
            if temp and isinstance(temp[0], Symbol) and (temp[0].name in ["return","break","continue"]) and i != len(ast.member) - 1:
                for y in ast.member[i+1:]:
                        if isinstance(y, Stmt):
                            raise UnreachableStatement(y)
            env = [env[0] + temp] + env[1:]
        return list(filter(lambda x: x.name in ["return", "break", "continue"],env[0]))
        

    def visitId(self, ast, c):
        res = self.lookup(ast.name, self.flatten(c[:-1]), lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        if not c[-1][-1] == "left" and not isinstance(res.mtype, MType) and res.isCheck is None:
            raise UninitializedVariable(ast.name)
        return [(res.mtype,None)]
    
    def visitUnaryOp(self, ast, c):
        type_body = self.visit(ast.body,c)[0]
        if ast.op == "-":
            if isinstance(type_body[0], (IntType, FloatType)):
                if type_body[1] is None: 
                    return [(type_body[0], None)]
                else:
                    return [(type_body[0], -type_body[1])]
        if ast.op == "!":
            if isinstance(type_body[0], BoolType):
                return [(type_body[0], None)]
        raise TypeMismatchInExpression(ast)

    def visitBinaryOp(self, ast, c):
        if ast.op in ["="]:
            type_right = self.visit(ast.right,c)[0]
            type_left = self.visit(ast.left,c[:-1] + [c[-1] +["left"]])[0]
            if not isinstance(ast.left, (Id, ArrayCell)):
                raise NotLeftValue(ast.left)
            if isinstance(ast.left, Id):
                res = self.lookup(ast.left.name, self.flatten(c[:-1]), lambda x: x.name)
                res.isCheck = True
            if isinstance(type_left[0], FloatType):
                if isinstance(type_right[0], (IntType, FloatType)):
                    return [(type_left[0],None)]
            elif isinstance(type_left[0], (IntType, BoolType, StringType)):
                if type(type_right[0]) is type(type_left[0]):
                    return [(type_left[0],None)]
        else:
            type_left = self.visit(ast.left,c)[0]
            type_right = self.visit(ast.right,c)[0]
            if ast.op in ["+", "-", "*", "/"]:
                if isinstance(type_left[0], FloatType) and isinstance(type_right[0], FloatType):
                    return [(FloatType(), None)]
                elif isinstance(type_left[0], FloatType) and isinstance(type_right[0], IntType):
                    return [(FloatType(), None)]
                elif isinstance(type_left[0], IntType) and isinstance(type_right[0], FloatType):
                    return [(FloatType(), None)]
                elif isinstance(type_left[0], IntType) and isinstance(type_right[0], IntType):
                    if type_left[1] is None or type_right[1] is None:
                        return [(IntType(),None)]
                    if ast.op == "+":
                        return [(IntType(), type_left[1] + type_right[1])]
                    elif ast.op == "-":
                        return [(IntType(), type_left[1] - type_right[1])]
                    elif ast.op == "*":
                        return [(IntType(), type_left[1] * type_right[1])]
                    elif ast.op == "/":
                        return [(IntType(), type_left[1] // type_right[1])]
            elif ast.op == "%":
                if isinstance(type_left[0], IntType) and isinstance(type_right[0], IntType):
                    if type_left[1] is None or type_right[1] is None:
                        return [(IntType(),None)]
                    else:
                        return [(IntType(), type_left[1] % type_right[1])]
            elif ast.op in ["<", "<=", ">=", ">"]:
                if isinstance(type_left[0], (IntType, FloatType)) and isinstance(type_right[0], (IntType, FloatType)):
                    return [(BoolType(),None)]
            elif ast.op in ["==", "!="]:
                if isinstance(type_left[0], IntType) and isinstance(type_right[0], IntType):
                    return [(BoolType(),None)]
                elif isinstance(type_left[0], BoolType) and isinstance(type_right[0], BoolType):
                    return [(BoolType(),None)]
            elif ast.op in ["||", "&&"]:
                if isinstance(type_left[0], BoolType) and isinstance(type_right[0], BoolType):
                    return [(BoolType(),None)]

        raise TypeMismatchInExpression(ast)
    
    def visitIntLiteral(self, ast, c):
        return [(IntType(), ast.value)]

    def visitFloatLiteral(self, ast, c):
        return [(FloatType(),None)]

    def visitBooleanLiteral(self, ast, c):
        return [(BoolType(),None)]

    def visitStringLiteral(self, ast, c):
        return [(StringType(),None)]

    def visitArrayCell(self, ast, c):
        type_arr = self.visit(ast.arr, c)[0]
        type_idx = self.visit(ast.idx, c)[0]
        if not (isinstance(type_arr[0], (ArrayType, ArrayPointerType)) and isinstance(type_idx[0], IntType)):
            raise TypeMismatchInExpression(ast)
        if not type_idx[1] is None and (type_idx[1] < 0 or isinstance(type_arr[0], ArrayType) and type_idx[1] >= type_arr[0].dimen):
            raise IndexOutOfRange(ast)
        return [(type_arr[0].eleType,None)]
        
    
    def visitCallExpr(self, ast, c):
        par = [self.visit(x,c)[0][0] for x in ast.param]
        res = self.lookup(ast.method.name, self.flatten(c[:-1]),lambda x: x.name)
        if res is None:
            raise Undeclared(Function(), ast.method.name)
        if not type(res.mtype) is MType:
            raise TypeMismatchInExpression(ast)
        if len(par) != len(res.mtype.partype):
            raise TypeMismatchInExpression(ast)
        for i in range(len(par)):
            if isinstance(res.mtype.partype[i], ArrayPointerType) and isinstance(par[i], (ArrayType, ArrayPointerType)):
                if not type(par[i].eleType) is type(res.mtype.partype[i].eleType):
                    raise TypeMismatchInExpression(ast)
            elif isinstance(res.mtype.partype[i], FloatType):
                if not isinstance(par[i], (FloatType,IntType)):
                    raise TypeMismatchInExpression(ast)
            else:
                if not type(res.mtype.partype[i]) is type(par[i]):
                    raise TypeMismatchInExpression(ast) 
        if not c[-1][0].name == ast.method.name:
            res.isCheck = True
        return [(res.mtype.rettype,None)]
        
    def visitIf(self, ast, c):
        type_expr = self.visit(ast.expr,c)[0][0]
        if not isinstance(type_expr,BoolType):
            raise TypeMismatchInStatement(ast)
        then = self.visitMember(ast.thenStmt,c)
        if ast.elseStmt:
            elseCheck =self.visitMember(ast.elseStmt,c)
            if self.lookup("return", then, lambda x: x.name) and self.lookup("return", elseCheck, lambda x: x.name):
                return [Symbol("return", None)]
            if any(self.lookup(x, then, lambda x: x.name) for x in ["return", "continue", "break"]) and any(self.lookup(x, elseCheck, lambda x: x.name) for x in ["return", "continue", "break"]):
                return [Symbol("break", None)]
        return []
        
    def visitMember(self, ast, c):
        if isinstance(ast, Expr):
            self.visit(ast, c)
            return []
        elif isinstance(ast, (VarDecl, Stmt)):
            return self.visit(ast, c)

    def visitFor(self, ast, c):
        type_expr1 = self.visit(ast.expr1,c)[0][0]
        type_expr2 = self.visit(ast.expr2,c)[0][0]
        type_expr3 = self.visit(ast.expr3,c)[0][0]
        temp = c[:-1] + [c[-1] + ["loop"]]
        self.visit(ast.loop,temp)
        if isinstance(type_expr1, IntType) and isinstance(type_expr2, BoolType) and isinstance(type_expr3, IntType):
            return []
        raise TypeMismatchInStatement(ast)
    
    def visitDowhile(self, ast, c):
        temp = c[:-1] + [c[-1] + ["loop"]]
        lst = []
        for i,x in enumerate(ast.sl):
            tmp = self.visitMember(x, temp)
            if tmp and isinstance(tmp[0], Symbol) and tmp[0].name in ["return", "break", "continue"] and i != len(ast.sl) - 1:
                raise UnreachableStatement(ast.sl[i+1])
            if tmp and isinstance(tmp[0],Symbol) and tmp[0].name == "return":
                lst = lst + tmp
        type_expr = self.visit(ast.exp,c)[0][0]
        if not isinstance(type_expr, BoolType):
            raise TypeMismatchInStatement(ast)
        return lst
        

    def visitReturn(self, ast, c):
        type_ret = c[-1][0].mtype.rettype
        if isinstance(type_ret, VoidType):
            if ast.expr:
                raise TypeMismatchInStatement(ast)
        else:
            if not ast.expr:
                raise TypeMismatchInStatement(ast)
            type_expr = self.visit(ast.expr,c)[0][0]
            if isinstance(type_ret, ArrayPointerType) and isinstance(type_expr,(ArrayType, ArrayPointerType)):
                if not type(type_expr.eleType) is type(type_ret.eleType):
                    raise TypeMismatchInStatement(ast)
            elif isinstance(type_ret, FloatType):
                if not isinstance(type_expr, (IntType, FloatType)):
                    raise TypeMismatchInStatement(ast)
            else:
                if not type(type_expr) is type(type_ret):
                    raise TypeMismatchInStatement(ast)
        return [Symbol("return", None)]
    
    def visitBreak(self, ast, c):
        if c[-1][-1] == "loop":
            return [Symbol("break", None)]
        raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        if c[-1][-1] == "loop":
            return [Symbol("continue", None)]
        raise ContinueNotInLoop()

    # def visitCallExpr(self, ast, c): 
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
        
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype
    
    
    
    

