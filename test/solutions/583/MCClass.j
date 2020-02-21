.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static abs(F)F
.var 0 is x F from Label0 to Label1
Label0:
	fload_0
	iconst_0
	i2f
	fcmpl
	iflt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_0
	goto Label1
	goto Label5
Label4:
	fload_0
	fneg
	goto Label1
Label5:
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	i2f
	fstore_1
	fload_1
	invokestatic MCClass/findSqrt(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static Square(FFF)F
.var 0 is n F from Label0 to Label1
.var 1 is i F from Label0 to Label1
.var 2 is j F from Label0 to Label1
Label0:
	fload_1
	fload_2
	fadd
	iconst_2
	i2f
	fdiv
	fstore_3
	fload_3
	fload_3
	fmul
	fstore 4
	fload 4
	fload_0
	fsub
	invokestatic MCClass/abs(F)F
	ldc 0.0001
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_3
	goto Label1
	goto Label5
Label4:
	fload 4
	fload_0
	fcmpl
	ifge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	fload_0
	fload_3
	fload_2
	invokestatic MCClass/Square(FFF)F
	goto Label1
	goto Label9
Label8:
	fload_0
	fload_1
	fload_3
	invokestatic MCClass/Square(FFF)F
	goto Label1
Label9:
Label5:
Label1:
	freturn
.limit stack 3
.limit locals 5
.end method

.method public static findSqrt(F)V
.var 0 is n F from Label0 to Label1
Label0:
	iconst_1
	i2f
	fstore_1
	iconst_0
	istore_2
Label2:
Label5:
	fload_1
	fload_1
	fmul
	fload_0
	fsub
	invokestatic MCClass/abs(F)F
	ldc 0.0001
	fcmpl
	ifge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
Label10:
	fload_1
	invokestatic io/putFloat(F)V
	iconst_1
	istore_2
Label11:
	goto Label12
Label9:
	fload_1
	fload_1
	fmul
	fload_0
	fcmpl
	ifle Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
Label16:
	fload_0
	fload_1
	iconst_1
	i2f
	fsub
	fload_1
	invokestatic MCClass/Square(FFF)F
	fstore_3
	fload_3
	invokestatic io/putFloat(F)V
	iconst_1
	istore_2
Label17:
Label15:
Label12:
	fload_1
	iconst_1
	i2f
	fadd
	fstore_1
Label6:
Label3:
	iload_2
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label2
Label4:
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label0:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
