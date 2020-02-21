.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static binary_conversion(I)I
.var 0 is num I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iconst_0
	goto Label1
Label6:
	goto Label7
Label4:
Label8:
	iload_0
	iconst_2
	irem
	bipush 10
	iload_0
	iconst_2
	idiv
	invokestatic MCClass/binary_conversion(I)I
	imul
	iadd
	goto Label1
Label9:
Label7:
Label1:
	ireturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 78
	istore_1
	bipush 78
	invokestatic MCClass/binary_conversion(I)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
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
