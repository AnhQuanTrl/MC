'''
 *   @author Tran Le Anh Quan
 *   @mssv 1712830
 *   18/12/2019
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat",MType([],FloatType()),CName(self.libName)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName(self.libName)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName(self.libName)),
                Symbol("putString",MType([StringType()],VoidType()),CName(self.libName)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName(self.libName)),
                Symbol("putLn",MType([],VoidType()),CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        print(dir_)
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        for x in ast.decl:
            self.process(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), c, Frame("<init>", VoidType))
        self.genMETHOD(FuncDecl(Id("<clinit>"), list(), None, Block(list())), e.sym, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None and consdecl.name.name == "<init>"
        isClinit = consdecl.returnType is None and consdecl.name.name == "<clinit>"
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit or isClinit else consdecl.returnType
        if isInit:
            methodName = "<init>"
        elif isClinit:
            methodName = "<clinit>"
        else:
            methodName=consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)
        glenv = o
        if isClinit and all(isinstance(x.mtype, MType) for x in glenv):
            return
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)
        e = SubBody(frame, glenv)
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            for par in consdecl.param:
                e = self.visit(par,e)
                res = self.lookup(par.variable,e.sym,lambda x: x.name)
                self.emit.printout(self.emit.emitVAR(res.value.value, res.name, res.mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
        body = consdecl.body
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isClinit:
            for decl in glenv:
                if not isinstance(decl.mtype, MType):
                    self.genStatic(decl, e)
        for x in body.member:
            e = self.visitMember(x, e)

        #list(map(lambda x: self.visitMember(x, e) if not isinstance(x, VarDecl) else None, body.member))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.push()
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            self.emit.printout(self.emit.emitRETURN(frame.returnType,frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();
    
    def genStatic(self, sym, o):
        if isinstance(sym.mtype, ArrayType):
            self.emit.printout(self.emit.emitSTATICARRAY(sym.value.value+'.'+sym.name,sym.mtype,o.frame))
    def visitMember(self, ast, o):
        if isinstance(ast, VarDecl):
            return self.visit(ast, o)
        elif isinstance(ast, Expr):           
            self.emit.printout(self.visit(ast, Access(o.frame, o.sym, None, True))[0])
            return o
        else:
            self.visit(ast, o)
            return o
    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        return SubBody(None, [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))] + subctxt.sym)

    def process(self, ast, o):
        if isinstance(ast, FuncDecl):
            subctxt = o
            frame = Frame(ast.name, ast.returnType)
            self.genMETHOD(ast, subctxt.sym, frame)
    
    def visitVarDecl(self, ast, o):
        subctxt = o
        frame = subctxt.frame
        if frame is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable, ast.varType, False))
            return SubBody(frame, [Symbol(ast.variable, ast.varType, CName(self.className))] + subctxt.sym)
        else:
            idx = Index(frame.getNewIndex())
            if isinstance(ast.varType, ArrayType):
                self.emit.printout(self.emit.emitLOCALARRAY(idx.value, ast.varType, frame))
            return SubBody(frame, [Symbol(ast.variable, ast.varType, idx)] + subctxt.sym)
    
    # def visitVarDecl2(self, ast, o):
    #     subctxt = o
    #     frame = subctxt.frame
    #     self.emit.printout(self.emit.emitLABEL(frame.getNewLabel()-1, frame))
    #     return SubBody(frame, subctxt.sym)
  
    def visitId(self, ast, o):
        subctxt = o
        res = self.lookup(ast.name, subctxt.sym, lambda x:x.name)
        
        if subctxt.isLeft == False:
            if isinstance(res.value, CName):
                return self.emit.emitGETSTATIC(res.value.value+'.'+res.name, res.mtype, o.frame), res.mtype
            else:
                return self.emit.emitREADVAR(res.name, res.mtype, res.value.value, o.frame), res.mtype 
        elif not subctxt.isFirst:
            if isinstance(res.value, CName):
                return self.emit.emitPUTSTATIC(res.value.value+'.'+res.name, res.mtype, o.frame), res.mtype
            else:
                return self.emit.emitWRITEVAR(res.name, res.mtype, res.value.value, o.frame), res.mtype
        else:
            return "", res.mtype

    def visitUnaryOp(self, ast, o):
        in_ = ""
        operand = self.visit(ast.body, o)
        if o.isLeft is None:
            return operand[0], None
        in_ = in_ + operand[0]
        if ast.op == "-":
            in_ = in_ + self.emit.emitNEGOP(operand[1], o.frame)
            return in_, operand[1]
        else:
            return in_ + self.emit.emitNOT(IntType(), o.frame), operand[1]
    def visitBinaryOp(self, ast, o):
        subctxt = o
        in_ = ""
        if ast.op in ['+','-','*','/','%','>','>=','==','!=','<=','<']:
            left = self.visit(ast.left, o)
            right = self.visit(ast.right, o)
            if o.isLeft is None:
                return left[0] + right[0], None
            if isinstance(left[1], FloatType) or isinstance(right[1], FloatType):
                op_type = FloatType()
                in_ = in_ + left[0]
                if isinstance(left[1], IntType):
                    in_ = in_ + self.emit.emitI2F(o.frame)
                in_ = in_ + right[0]
                if isinstance(right[1], IntType):
                    in_ = in_ + self.emit.emitI2F(o.frame)
            else:
                op_type = IntType()
                in_ = in_ + left[0]
                in_ = in_ + right[0]
            if ast.op in ['+','-']:
                return in_ + self.emit.emitADDOP(ast.op, op_type, o.frame), op_type
            elif ast.op in ['*','/']:
                return in_ + self.emit.emitMULOP(ast.op, op_type, o.frame), op_type
            elif ast.op in ['>','>=','==','!=','<=','<']:
                return in_ + self.emit.emitREOP(ast.op, op_type, o.frame), BoolType()
            else:
                return in_ + self.emit.emitMOD(o.frame), op_type
        elif ast.op in ['&&','||']:
            in_ = ""
            in_ = in_ + self.visit(ast.left, Access(o.frame,o.sym,False,True))[0]
            #short circut here
            bybassLabel = o.frame.getNewLabel()
            exitLabel = o.frame.getNewLabel()
            if ast.op == '&&':
                in_ = in_ + self.emit.emitIFFALSE(bybassLabel, o.frame)
            else:
                in_ = in_ + self.emit.emitIFTRUE(bybassLabel, o.frame)
            in_ = in_ + self.visit(ast.right, Access(o.frame,o.sym,False,True))[0]
            in_ = in_ + self.emit.emitGOTO(exitLabel,o.frame)
            in_ = in_ + self.emit.emitLABEL(bybassLabel, o.frame)
            o.frame.pop()
            if ast.op == '&&':
                in_ = in_ + self.emit.emitPUSHICONST("false", o.frame)
            else:
                in_ = in_ + self.emit.emitPUSHICONST("true", o.frame)
            in_ = in_ + self.emit.emitLABEL(exitLabel, o.frame)
            if o.isLeft is None:
                in_ = in_ + self.emit.emitPOP(o.frame)
            return in_, BoolType()
        else:
            in_ = in_ + self.visit(ast.left, Access(o.frame, o.sym, True, True))[0]
            right = self.visit(ast.right, Access(o.frame, o.sym, False, True))
            in_ = in_ + right[0]
            dup = "" #store the dup or dupx2 command for using after i2f
            if subctxt.isLeft == False: 
                if isinstance(ast.left, ArrayCell):
                    dup = self.emit.emitDUPX2(o.frame)
                else:
                    dup = self.emit.emitDUP(o.frame)
            #emit dup before left to guarantee right stack value
            left = self.visit(ast.left, Access(o.frame, o.sym, True, False))
            if isinstance(right[1], IntType) and isinstance(left[1], FloatType):
                in_ = in_ + self.emit.emitI2F(o.frame)
            in_ = in_ + dup
            in_ = in_ + left[0]
            return in_, left[1]

    
    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any
        
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ""
        for i,x in enumerate(ast.param):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = in_ + str1
            if isinstance(ctype.partype[i], FloatType) and isinstance(typ1, IntType):
                in_ = in_ + self.emit.emitI2F(o.frame)
        ret = in_ + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        if o.isLeft is None and not type(sym.mtype.rettype) is VoidType:
            ret = ret + self.emit.emitPOP(o.frame)
        return ret, sym.mtype.rettype


    def visitArrayCell(self, ast, o):
        subctxt = o
        if o.isLeft is None:
            return self.visit(ast.arr,o)[0] + self.visit(ast.idx, o)[0], None
        if subctxt.isLeft and not subctxt.isFirst :
            res = self.lookup(ast.arr.name, o.sym, lambda x:x.name)
            return self.emit.emitASTORE(res.mtype.eleType, o.frame), res.mtype.eleType
        arr = self.visit(ast.arr, Access(o.frame, o.sym, False, True))
        in_ = arr[0]
        in_ = in_ + self.visit(ast.idx, Access(o.frame, o.sym, False, True))[0]
        if not subctxt.isLeft:
            return in_ + self.emit.emitALOAD(arr[1].eleType, o.frame), arr[1].eleType
        else:
            return in_,arr[1]
        
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        if o.isLeft is None:
            return "", None
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        if o.isLeft is None:
            return "", None
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        if o.isLeft is None:
            return "", None
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()

    def visitStringLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any

        ctxt = o
        if o.isLeft is None:
            return "", None
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

    
    def visitBlock(self, ast, o):
        frame = o.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        e = o
        for x in ast.member:
            e = self.visitMember(x, e)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    def visitIf(self, ast, o):
        self.emit.printout(self.visit(ast.expr, Access(o.frame, o.sym, False, True))[0])
        label1 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(label1,o.frame))
        self.visitMember(ast.thenStmt, o)
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(label1, o.frame))
            return
        label2 = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitGOTO(label2, o.frame))
        self.emit.printout(self.emit.emitLABEL(label1, o.frame))
        self.visitMember(ast.elseStmt, o)
        self.emit.printout(self.emit.emitLABEL(label2, o.frame))

    def visitFor(self, ast, o):
        self.visitMember(ast.expr1,o)
        o.frame.enterLoop()
        loopLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(loopLabel, o.frame))
        self.emit.printout(self.visit(ast.expr2,Access(o.frame,o.sym,False,True))[0])
        self.emit.printout(self.emit.emitIFFALSE(o.frame.getBreakLabel(),o.frame))
        self.visitMember(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        self.visitMember(ast.expr3,o)
        self.emit.printout(self.emit.emitGOTO(loopLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitDowhile(self, ast, o):
        loopLabel = o.frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(loopLabel, o.frame))
        o.frame.enterLoop()
        for x in ast.sl:
            self.visitMember(x, o)
        self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(), o.frame))
        self.emit.printout(self.visit(ast.exp,Access(o.frame,o.sym,False,True))[0])
        self.emit.printout(self.emit.emitIFTRUE(loopLabel,o.frame))
        self.emit.printout(self.emit.emitLABEL(o.frame.getBreakLabel(), o.frame))
        o.frame.exitLoop()

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(),o.frame))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))

    def visitReturn(self, ast, o):
        if ast.expr:
            ret = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            self.emit.printout(ret[0])
            if isinstance(ret[1], IntType) and isinstance(o.frame.returnType, FloatType):
                self.emit.printout(self.emit.emitI2F(o.frame))
            o.frame.pop()
        self.emit.printout(self.emit.emitGOTO(o.frame.endLabel[0], o.frame))
