.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/looping()F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static looping()F
Label0:
	iconst_3
	istore_0
Label2:
Label5:
Label7:
	iconst_4
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
	iconst_3
	i2f
	goto Label1
Label8:
Label6:
	iload_0
	iconst_1
	iadd
	istore_0
Label3:
	iload_0
	bipush 10
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label2
Label4:
Label1:
	freturn
.limit stack 2
.limit locals 2
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
