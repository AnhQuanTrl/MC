.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static c [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	dup
	istore_2
	istore_1
	iload_2
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
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

.method public static <clinit>()V
Label0:
	iconst_5
	newarray int
	putstatic MCClass.c [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
