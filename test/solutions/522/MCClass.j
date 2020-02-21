.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 9
	iconst_0
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	goto Label5
Label4:
	iconst_1
Label5:
	istore_1
	bipush 7
	bipush 8
	imul
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	iconst_1
	dup
	istore_2
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	goto Label13
Label12:
	iconst_0
Label13:
	istore_2
	iload_1
	ifle Label16
	iload_2
	goto Label17
Label16:
	iconst_0
Label17:
	istore_3
	iload_3
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iload_1
	goto Label21
Label20:
	iconst_1
Label21:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 2
.limit locals 4
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
