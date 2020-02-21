.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	dup
	istore_1
	iconst_4
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_1
	bipush 100
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label8
Label9:
	iload_1
	invokestatic io/putIntLn(I)V
Label10:
Label8:
Label1:
	return
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
