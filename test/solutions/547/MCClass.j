.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore_2
	sipush 4532
	istore_1
Label2:
Label5:
	iload_1
	bipush 10
	irem
	istore_3
	iload_2
	bipush 10
	imul
	iload_3
	iadd
	istore_2
	iload_1
	bipush 10
	idiv
	istore_1
Label6:
Label3:
	iload_1
	iconst_0
	if_icmpeq Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label2
Label4:
	iload_2
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
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
