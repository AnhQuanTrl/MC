.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static insertSort([II)V
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iconst_1
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_0
	iload_2
	iaload
	istore_3
	iload_2
	iconst_1
	isub
	istore 4
Label9:
Label12:
	iload 4
	iconst_0
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	aload_0
	iload 4
	iaload
	iload_3
	if_icmpgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	goto Label17
Label16:
	iconst_1
Label17:
	ifle Label20
	goto Label11
Label20:
	aload_0
	iload 4
	iconst_1
	iadd
	aload_0
	iload 4
	iaload
	iastore
	iload 4
	iconst_1
	isub
	istore 4
Label13:
Label10:
	iload 4
	iconst_0
	if_icmplt Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
	aload_0
	iload 4
	iaload
	iload_3
	if_icmple Label25
	iconst_1
	goto Label26
Label25:
	iconst_0
Label26:
	goto Label24
Label23:
	iconst_0
Label24:
	ifgt Label9
Label11:
	aload_0
	iload 4
	iconst_1
	iadd
	iload_3
	iastore
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
Label1:
	return
.limit stack 4
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
	invokestatic MCClass/insertSort([II)V
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
