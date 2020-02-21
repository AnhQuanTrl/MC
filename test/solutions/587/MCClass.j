.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)Z
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iconst_1
	ifgt Label2
	iload_1
	invokestatic MCClass/foo(I)Z
	goto Label3
Label2:
	iconst_1
Label3:
	ifle Label4
Label5:
Label6:
Label4:
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
