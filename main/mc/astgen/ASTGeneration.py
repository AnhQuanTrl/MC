#1712830
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import reduce

class ASTGeneration(MCVisitor):
    def flatten(self, lst):
        return (i for e in lst for i in (self.flatten(e) if isinstance(e, list) else [e])) 
    #program:  (var_dec | func_dec)+ EOF
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return Program(list(self.flatten(self.visit(decl) for decl in list(ctx.getChildren())[:-1])))     
    #var_dec: primitive_type variable (CM variable)* SM;
    def visitVar_dec(self, ctx:MCParser.Var_decContext):
        return [VarDecl(var, ArrayType(dimension,self.visit(ctx.primitive_type()))) if dimension != -1 else VarDecl(var, self.visit(ctx.primitive_type())) for (var, dimension) in [self.visit(item) for item in ctx.variable()]]
    #variable: ID (LS INTLIT RS)?;
    def visitVariable(self, ctx:MCParser.VariableContext):
        return ctx.ID().getText(), (int(ctx.INTLIT().getText()) if ctx.INTLIT() else -1)
    #primitive_type: BOOLEAN | INT | FLOAT | STRING;
    def visitPrimitive_type(self, ctx:MCParser.Primitive_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()
    #func_dec: mctype ID LB (par_dec (CM par_dec)*)? RB block_statement;
    def visitFunc_dec(self, ctx:MCParser.Func_decContext):
        return FuncDecl(Id(ctx.ID().getText()), [self.visit(par) for par in ctx.par_dec()], self.visit(ctx.mctype()), self.visit(ctx.block_statement()))
    #par_dec: primitive_type ID (LS RS)?;
    def visitPar_dec(self, ctx:MCParser.Par_decContext):
        return VarDecl(ctx.ID().getText(), ArrayPointerType(self.visit(ctx.primitive_type())) if ctx.LS() else self.visit(ctx.primitive_type()))
    #mctype: primitive_type (LS RS)? | VOID; 
    def visitMctype(self, ctx:MCParser.MctypeContext):
        if ctx.VOID():
            return VoidType()
        elif ctx.LS():
            return ArrayPointerType(self.visit(ctx.primitive_type()))
        else: 
            return self.visit(ctx.primitive_type())
    #block_statement: LP (var_dec | statement)* RP;
    def visitBlock_statement(self, ctx:MCParser.Block_statementContext):
        return Block(list(self.flatten(self.visit(stm) for stm in list(ctx.getChildren())[1:-1])))  
    #statement: matched_statement| unmatched_statment;
    def visitStatement(self, ctx:MCParser.StatementContext):
        return self.visit(ctx.getChild(0))
    #matched_statement: IF LB expression RB matched_statement ELSE matched_statement| other_statement;
    def visitMatched_statement(self, ctx:MCParser.Matched_statementContext):
        if ctx.other_statement():
            return self.visit(ctx.other_statement())
        else:
            return If(self.visit(ctx.expression()),self.visit(ctx.matched_statement(0)),self.visit(ctx.matched_statement(1)))
    #unmatched_statment: IF LB expression RB statement | IF LB expression RB matched_statement ELSE unmatched_statment;
    def visitUnmatched_statment(self, ctx:MCParser.Unmatched_statmentContext):
        return If(self.visit(ctx.expression()), self.visit(ctx.statement())) if not ctx.ELSE() else If(self.visit(ctx.expression()), self.visit(ctx.matched_statement()), self.visit(ctx.unmatched_statment()))
    #other_statement: for_statement | dowhile_statement | break_statement | continue_statement | return_statment | expression_statement | block_statement;
    def visitOther_statement(self, ctx:MCParser.Other_statementContext):
        return self.visit(ctx.getChild(0))
    #dowhile_statement: DO statement+ WHILE expression SM;
    def visitDowhile_statement(self, ctx:MCParser.Dowhile_statementContext):
        return Dowhile([self.visit(stm) for stm in ctx.statement()],self.visit(ctx.expression()))
    #for_statement: FOR LB expression SM expression SM expression RB statement;
    def visitFor_statement(self, ctx:MCParser.For_statementContext):
        return For(*[self.visit(exp) for exp in ctx.expression()], self.visit(ctx.statement()))
    #break_statement: BREAK SM;
    def visitBreak_statement(self, ctx:MCParser.Break_statementContext):
        return Break()
    #continue_statement: CONTINUE SM;
    def visitContinue_statement(self, ctx:MCParser.Continue_statementContext):
        return Continue()
    #return_statment: RETURN (expression)? SM;
    def visitReturn_statment(self, ctx:MCParser.Return_statmentContext):
        return Return(self.visit(ctx.expression()) if ctx.expression() else None)
    #expression_statement: expression SM;
    def visitExpression_statement(self, ctx:MCParser.Expression_statementContext):
        return self.visit(ctx.expression())
    #expression: or_expression ASSIGN expression | or_expression;
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return BinaryOp(ctx.ASSIGN().getText(), self.visit(ctx.or_expression()), self.visit(ctx.expression())) if ctx.ASSIGN() else self.visit(ctx.or_expression())
    #or_expression: or_expression OR and_expression | and_expression;
    def visitOr_expression(self, ctx:MCParser.Or_expressionContext):
        return BinaryOp(ctx.OR().getText(), self.visit(ctx.or_expression()), self.visit(ctx.and_expression())) if ctx.OR() else self.visit(ctx.and_expression())
    #and_expression: and_expression AND eq_expression | eq_expression;
    def visitAnd_expression(self, ctx:MCParser.And_expressionContext):
        return BinaryOp(ctx.AND().getText(), self.visit(ctx.and_expression()), self.visit(ctx.eq_expression())) if ctx.AND() else self.visit(ctx.eq_expression())
    #eq_expression: rel_expression ((EQ | NE) rel_expression)?;
    def visitEq_expression(self, ctx:MCParser.Eq_expressionContext):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.rel_expression(0)), self.visit(ctx.rel_expression(1))) if ctx.getChildCount() == 3 else self.visit(ctx.rel_expression(0))
    #rel_expression: arithmetic_expression ((LT | LTE | GT | GTE) arithmetic_expression)?;    
    def visitRel_expression(self, ctx:MCParser.Rel_expressionContext):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.arithmetic_expression(0)), self.visit(ctx.arithmetic_expression(1))) if ctx.getChildCount() == 3 else self.visit(ctx.arithmetic_expression(0))
    #arithmetic_expression: arithmetic_expression (ADD | SUB) factor | factor;
    def visitArithmetic_expression(self, ctx:MCParser.Arithmetic_expressionContext):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.arithmetic_expression()), self.visit(ctx.factor())) if ctx.getChildCount() == 3 else self.visit(ctx.factor())
    #factor: factor (DIV | MUL | MOD) term | term;
    def visitFactor(self, ctx:MCParser.FactorContext):
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.factor()), self.visit(ctx.term())) if ctx.getChildCount() == 3 else self.visit(ctx.term())
    #term: (SUB | NOT) term | index_expression;
    def visitTerm(self, ctx:MCParser.TermContext):
        return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.term())) if ctx.getChildCount() == 2 else self.visit(ctx.index_expression())
    #index_expression: basic_expression (LS expression RS)?;
    def visitIndex_expression(self, ctx:MCParser.Index_expressionContext):
        return ArrayCell(self.visit(ctx.basic_expression()), self.visit(ctx.expression())) if ctx.LS() else self.visit(ctx.basic_expression()) 
    #basic_expression: ID | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | LB expression RB | invo_expression;
    def visitBasic_expression(self, ctx:MCParser.Basic_expressionContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        elif ctx.invo_expression():
            return self.visit(ctx.invo_expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return BooleanLiteral(True if ctx.BOOLLIT().getText() == 'true' else False)
    #ID LB (expression (CM expression)*)? RB;
    def visitInvo_expression(self, ctx:MCParser.Invo_expressionContext):
        return CallExpr(Id(ctx.ID().getText()), [self.visit(exp) for exp in ctx.expression()])
            
    

