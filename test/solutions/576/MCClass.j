.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 366
	istore_1
	bipush 60
	istore_2
	sipush 366
	bipush 30
	invokestatic MCClass/gcd(II)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static gcd(II)I
.var 0 is n1 I from Label0 to Label1
.var 1 is n2 I from Label0 to Label1
Label0:
	iload_1
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MCClass/gcd(II)I
	goto Label1
	goto Label5
Label4:
	iload_0
	goto Label1
Label5:
Label1:
	ireturn
.limit stack 3
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
