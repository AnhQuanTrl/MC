.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()[I
Label0:
	iconst_3
	newarray int
	astore_0
	aload_0
	iconst_1
	iconst_2
	iastore
	aload_0
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MCClass/foo()[I
	pop
Label1:
	return
.limit stack 1
.limit locals 1
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
