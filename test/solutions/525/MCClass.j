.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static c()I
Label0:
	invokestatic io/putLn()V
	iconst_2
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	istore_1
	invokestatic MCClass/c()I
	pop
Label1:
	return
.limit stack 1
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
