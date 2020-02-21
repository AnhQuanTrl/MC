.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	newarray int
	astore_1
	aload_1
	iconst_0
	aload_1
	iconst_1
	iconst_1
	dup_x2
	iastore
	iastore
	aload_1
	iconst_0
	iaload
	aload_1
	iconst_1
	iaload
	iconst_2
	imul
	iadd
	invokestatic io/putIntLn(I)V
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
