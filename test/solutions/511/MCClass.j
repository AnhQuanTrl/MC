.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_0
	aload_1
	iconst_1
	ldc "1*3+4"
	dup_x2
	aastore
	aastore
	aload_1
	iconst_0
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
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
