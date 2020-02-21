.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	ineg
	istore_1
	iload_1
	iconst_0
	imul
	iconst_1
	ineg
	iconst_2
	idiv
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc 2.99
	fstore_2
	goto Label5
Label4:
	ldc 1.0
	fstore_2
Label5:
	fload_2
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 3
.limit locals 3
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
