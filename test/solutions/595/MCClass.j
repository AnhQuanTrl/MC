.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static linearSearch([III)I
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is find I from Label0 to Label1
Label0:
	iconst_0
	istore_3
Label2:
	iload_1
	iconst_0
	if_icmpne Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label7
	goto Label4
Label7:
	aload_0
	iload_3
	iaload
	iload_2
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iload_3
	goto Label1
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
Label3:
	iload_3
	iload_1
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label2
Label4:
	iconst_1
	ineg
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 4
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
	aload_1
	bipush 10
	bipush 46
	invokestatic MCClass/linearSearch([III)I
	invokestatic io/putIntLn(I)V
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
