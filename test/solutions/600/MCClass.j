.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static f()I
Label0:
	sipush 200
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/f()I
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label2:
	bipush 100
	dup
	istore_2
	dup
	istore 4
	istore_3
	iload_2
	invokestatic io/putIntLn(I)V
	iload_3
	invokestatic io/putIntLn(I)V
	iload 4
	invokestatic io/putIntLn(I)V
Label3:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 5
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
