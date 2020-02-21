.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	istore_1
	iconst_4
	dup
	istore 6
	dup
	istore 5
	dup
	istore 4
	dup
	istore_3
	dup
	istore_2
	istore_1
	iload_1
	iload_2
	imul
	iload_3
	imul
	iload 4
	imul
	iload 5
	imul
	iload 6
	imul
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 7
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
