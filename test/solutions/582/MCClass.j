.source MCClass.java
.class public MCClass
.super java.lang.Object

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
	iconst_3
	newarray int
	astore_2
	aload_2
	iconst_0
	iconst_1
	iastore
	aload_2
	iconst_1
	bipush 55
	iastore
	aload_2
	iconst_2
	bipush 9
	iastore
	aload_1
	aload_2
	iconst_5
	iconst_3
	invokestatic MCClass/isSubset([I[III)Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public static isSubset([I[III)Z
.var 0 is arr1 [I from Label0 to Label1
.var 1 is arr2 [I from Label0 to Label1
.var 2 is m I from Label0 to Label1
.var 3 is n I from Label0 to Label1
Label0:
	iconst_0
	istore 4
Label4:
	iload 4
	iload_3
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	istore 5
Label11:
	iload 5
	iload_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_1
	iload 4
	iaload
	aload_0
	iload 5
	iaload
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label10
Label18:
Label15:
Label9:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label11
Label10:
	iload 5
	iload_2
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	iconst_0
	goto Label1
Label21:
Label8:
Label2:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label4
Label3:
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 6
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
