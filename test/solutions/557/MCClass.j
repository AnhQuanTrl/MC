.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore 4
	iconst_0
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_0
	istore_2
Label11:
	iload_2
	iload_1
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iload_2
	istore_3
Label18:
	iload_3
	iload_1
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label17
Label21:
	iload_1
	iload_2
	imul
	iload_3
	imul
	iconst_3
	irem
	iconst_0
	if_icmpne Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label25
Label26:
	goto Label16
Label27:
Label25:
	iload 4
	iconst_1
	iadd
	istore 4
	iload_3
	iconst_5
	if_icmpne Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifle Label30
	goto Label17
Label30:
Label22:
Label16:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label18
Label17:
	iload_1
	iload_2
	imul
	iconst_5
	irem
	iconst_0
	if_icmpne Label31
	iconst_1
	goto Label32
Label31:
	iconst_0
Label32:
	ifle Label33
Label34:
	goto Label9
Label35:
Label33:
	iload 4
	iconst_1
	isub
	istore 4
	iload_2
	iload_3
	iconst_4
	isub
	if_icmpne Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	ifle Label38
	goto Label10
Label38:
Label15:
Label9:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label10:
Label8:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
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
