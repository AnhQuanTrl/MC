.source MCClass.java
.class public MCClass
.super java.lang.Object

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
	bipush 26
	iastore
	aload_1
	iconst_4
	bipush 95
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
	bipush 95
	iastore
	aload_1
	bipush 9
	bipush 78
	iastore
	bipush 10
	istore_2
	iconst_0
	istore_3
Label4:
	iload_3
	iload_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_3
	iconst_1
	iadd
	istore 4
Label11:
	iload 4
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
	aload_1
	iload_3
	iaload
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
Label19:
	iload 4
	istore 5
Label23:
	iload 5
	iload_2
	iconst_1
	isub
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
Label26:
	aload_1
	iload 5
	aload_1
	iload 5
	iconst_1
	iadd
	iaload
	iastore
Label27:
Label21:
	iload 5
	iconst_1
	iadd
	istore 5
	goto Label23
Label22:
	iload_2
	iconst_1
	isub
	istore_2
Label20:
	goto Label28
Label18:
Label29:
	iload 4
	iconst_1
	iadd
	istore 4
Label30:
Label28:
Label15:
Label9:
	goto Label11
Label10:
Label8:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
	aload_1
	iload_2
	invokestatic MCClass/printArr([II)V
Label1:
	return
.limit stack 5
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
