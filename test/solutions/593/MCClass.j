.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static bubbleSort([II)V
.var 0 is number [I from Label0 to Label1
.var 1 is count I from Label0 to Label1
Label0:
	iload_1
	iconst_2
	isub
	istore_2
Label4:
	iload_2
	iconst_0
	if_icmplt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	istore_3
Label11:
	iload_3
	iload_2
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_0
	iload_3
	iaload
	aload_0
	iload_3
	iconst_1
	iadd
	iaload
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
Label19:
	aload_0
	iload_3
	iaload
	istore 4
	aload_0
	iload_3
	aload_0
	iload_3
	iconst_1
	iadd
	iaload
	iastore
	aload_0
	iload_3
	iconst_1
	iadd
	iload 4
	iastore
Label20:
Label18:
Label15:
Label9:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label11
Label10:
Label8:
Label2:
	iload_2
	iconst_1
	isub
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 5
.limit locals 5
.end method

.method public static printArr([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iconst_0
	istore_2
Label2:
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
Label3:
	iload_2
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifgt Label2
Label4:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	newarray int
	astore_1
	aload_1
	iconst_0
	bipush 95
	iastore
	aload_1
	iconst_1
	bipush 26
	iastore
	aload_1
	iconst_2
	bipush 45
	iastore
	aload_1
	iconst_3
	iconst_0
	iastore
	aload_1
	iconst_4
	bipush 99
	iastore
	aload_1
	iconst_5
	iconst_3
	ineg
	iastore
	aload_1
	bipush 6
	bipush 78
	iastore
	aload_1
	bipush 7
	bipush 9
	ineg
	iastore
	aload_1
	bipush 8
	bipush 9
	iastore
	aload_1
	bipush 9
	bipush 25
	iastore
	aload_1
	bipush 10
	invokestatic MCClass/bubbleSort([II)V
	aload_1
	bipush 10
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
