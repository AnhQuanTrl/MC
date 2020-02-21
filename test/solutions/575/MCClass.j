.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_0
	ldc "HelloWorld\n"
	aastore
	aload_1
	iconst_1
	ldc "BotHere\n"
	aastore
	aload_1
	iconst_2
	ldc "Decoded\n"
	aastore
	aload_1
	iconst_3
	invokestatic MCClass/printStringArray([Ljava/lang/String;I)V
Label1:
	return
.limit stack 3
.limit locals 2
.end method

.method public static printStringArray([Ljava/lang/String;I)V
.var 0 is bs [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
Label0:
	iconst_0
	istore_2
Label4:
	iload_2
	iload_1
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	aload_0
	iload_2
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
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
