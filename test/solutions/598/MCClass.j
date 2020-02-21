.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static leap(I)Z
.var 0 is year I from Label0 to Label1
Label0:
	iload_0
	sipush 400
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	goto Label1
Label4:
	iload_0
	bipush 100
	irem
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	iconst_0
	goto Label1
Label7:
	iload_0
	iconst_4
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_1
	goto Label1
Label10:
	iconst_0
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 2012
	invokestatic MCClass/leap(I)Z
	invokestatic io/putBoolLn(Z)V
	sipush 2000
	invokestatic MCClass/leap(I)Z
	invokestatic io/putBoolLn(Z)V
	sipush 1900
	invokestatic MCClass/leap(I)Z
	invokestatic io/putBoolLn(Z)V
	sipush 1901
	invokestatic MCClass/leap(I)Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 1
.limit locals 1
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
