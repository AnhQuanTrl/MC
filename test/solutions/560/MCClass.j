.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	newarray float
	astore_1
	aload_1
	iconst_4
	iconst_1
	bipush 100
	imul
	bipush 99
	idiv
	isub
	ldc 4.0
	fastore
	aload_1
	iconst_3
	iconst_2
	idiv
	bipush 9
	iconst_2
	ineg
	imul
	iconst_4
	idiv
	i2f
	fastore
	aload_1
	iconst_3
	iconst_0
	imul
	sipush 10000
	imul
	iconst_0
	i2f
	fastore
	aload_1
	iconst_2
	aload_1
	iconst_4
	aload_1
	iconst_3
	faload
	aload_1
	iconst_1
	faload
	fmul
	bipush 9
	i2f
	fsub
	dup_x2
	fastore
	fastore
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_5
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
	faload
	invokestatic io/putFloat(F)V
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
.limit stack 7
.limit locals 3
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
