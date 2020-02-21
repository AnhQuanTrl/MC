.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore 4
	iconst_1
	istore_1
Label2:
	iconst_1
	istore_2
Label5:
	iload_2
	istore_3
Label8:
	iload_3
	iconst_1
	iadd
	istore_3
	iload_1
	iload_2
	imul
	iload_3
	imul
	iconst_3
	irem
	iconst_0
	if_icmpne Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
Label14:
	goto Label9
Label15:
Label13:
	iload 4
	iconst_1
	iadd
	istore 4
	iload_3
	iconst_5
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label10
Label18:
Label9:
	iload_3
	iload_1
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifgt Label8
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_1
	iload_2
	imul
	iconst_5
	irem
	iconst_0
	if_icmpne Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifle Label23
Label24:
	goto Label6
Label25:
Label23:
	iload 4
	iconst_1
	isub
	istore 4
	iload_2
	iload_3
	iconst_4
	isub
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label28
	goto Label7
Label28:
Label6:
	iload_2
	iload_1
	if_icmpge Label29
	iconst_1
	goto Label30
Label29:
	iconst_0
Label30:
	ifgt Label5
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
Label3:
	iload_1
	bipush 10
	if_icmpge Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifgt Label2
Label4:
	iload 4
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
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
