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
	iconst_5
	invokestatic MCClass/shellsort([II)V
	aload_1
	iconst_5
	invokestatic MCClass/printArr([II)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static shellsort([II)V
.var 0 is v [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iload_1
	iconst_2
	idiv
	istore_2
Label4:
	iload_2
	iconst_0
	if_icmple Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iload_2
	istore_3
Label9:
	iload_3
	iload_1
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	iload_3
	iload_2
	isub
	istore 4
Label14:
	iload 4
	iconst_0
	if_icmplt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	aload_0
	iload 4
	iaload
	aload_0
	iload 4
	iload_2
	iadd
	iaload
	if_icmple Label19
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
	aload_0
	iload 4
	iaload
	istore 5
	aload_0
	iload 4
	aload_0
	iload 4
	iload_2
	iadd
	iaload
	iastore
	aload_0
	iload 4
	iload_2
	iadd
	iload 5
	iastore
Label22:
Label12:
	iload 4
	iload_2
	isub
	istore 4
	goto Label14
Label13:
Label7:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label9
Label8:
Label2:
	iload_2
	iconst_2
	idiv
	istore_2
	goto Label4
Label3:
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
