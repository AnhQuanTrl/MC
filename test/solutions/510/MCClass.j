.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	newarray float
	astore_1
	aload_1
	iconst_0
	aload_1
	iconst_1
	iconst_1
	iconst_3
	imul
	iconst_4
	iadd
	i2f
	dup_x2
	fastore
	fastore
	aload_1
	iconst_0
	faload
	iconst_2
	i2f
	fdiv
	aload_1
	iconst_1
	faload
	bipush 10
	i2f
	fsub
	iconst_2
	i2f
	fmul
	fadd
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
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
