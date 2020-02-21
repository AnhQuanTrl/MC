.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static c()Z
Label0:
	invokestatic io/putLn()V
	iconst_1
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_1
Label3:
	ifle Label4
	invokestatic MCClass/c()Z
	goto Label5
Label4:
	iconst_0
Label5:
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
