.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	newarray int
	astore_1
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_1
	iload_2
	iload_2
	iastore
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iconst_0
	istore 4
	iconst_3
	istore_3
Label11:
	iload_3
	iconst_0
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	iload 4
	aload_1
	iload_3
	iconst_1
	isub
	iaload
	iadd
	istore 4
Label9:
	iload_3
	iconst_1
	isub
	istore_3
	goto Label11
Label10:
	iload 4
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
.limit locals 5
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
