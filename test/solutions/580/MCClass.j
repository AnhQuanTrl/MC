.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static printArr([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iload_2
	iload_1
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	goto Label1
Label6:
Label4:
Label7:
	aload_0
	iload_2
	iaload
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label8:
	iload_2
	iload_1
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label7
Label9:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_4
	iastore
	aload_1
	iconst_1
	iconst_1
	iastore
	aload_1
	iconst_2
	bipush 55
	iastore
	aload_1
	iconst_3
	bipush 9
	iastore
	aload_1
	iconst_4
	bipush 49
	iastore
	aload_1
	iconst_0
	invokestatic MCClass/printArr([II)V
Label1:
	return
.limit stack 3
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
