.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	newarray boolean
	astore_1
	iconst_0
	istore_2
Label2:
Label5:
	iload_2
	istore_3
	aload_1
	iload_3
	iconst_1
	bastore
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
Label3:
	iload_2
	iconst_4
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label2
Label4:
	aload_1
	invokestatic MCClass/returnBool([Z)[Z
	iconst_2
	baload
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public static returnBool([Z)[Z
.var 0 is bs [Z from Label0 to Label1
Label0:
	aload_0
	iconst_2
	iconst_0
	bastore
	aload_0
	goto Label1
Label1:
	areturn
.limit stack 3
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
