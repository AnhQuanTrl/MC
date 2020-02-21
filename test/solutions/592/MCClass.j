.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static quicksort([III)V
.var 0 is number [I from Label0 to Label1
.var 1 is first I from Label0 to Label1
.var 2 is last I from Label0 to Label1
Label0:
	iload_1
	iload_2
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iload_1
	istore 5
	iload_1
	istore_3
	iload_2
	istore 4
Label7:
Label10:
Label14:
	aload_0
	iload_3
	iaload
	aload_0
	iload 5
	iaload
	if_icmpgt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	iload_3
	iload_2
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label13
Label21:
Label22:
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label14
Label13:
Label25:
	aload_0
	iload 4
	iaload
	aload_0
	iload 5
	iaload
	if_icmple Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label24
Label28:
Label29:
Label23:
	iload 4
	iconst_1
	isub
	istore 4
	goto Label25
Label24:
	iload_3
	iload 4
	if_icmpge Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifle Label32
Label33:
	aload_0
	iload_3
	iaload
	istore 6
	aload_0
	iload_3
	aload_0
	iload 4
	iaload
	iastore
	aload_0
	iload 4
	iload 6
	iastore
Label34:
Label32:
Label11:
Label8:
	iload_3
	iload 4
	if_icmpge Label35
	iconst_1
	goto Label36
Label35:
	iconst_0
Label36:
	ifgt Label7
Label9:
	aload_0
	iload 5
	iaload
	istore 6
	aload_0
	iload 5
	aload_0
	iload 4
	iaload
	iastore
	aload_0
	iload 4
	iload 6
	iastore
	aload_0
	iload_1
	iload 4
	iconst_1
	isub
	invokestatic MCClass/quicksort([III)V
	aload_0
	iload 4
	iconst_1
	iadd
	iload_2
	invokestatic MCClass/quicksort([III)V
Label6:
Label4:
Label1:
	return
.limit stack 4
.limit locals 7
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
	iconst_0
	bipush 9
	invokestatic MCClass/quicksort([III)V
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
