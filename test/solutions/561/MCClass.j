.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
Label5:
	iconst_5
	istore_1
	iconst_0
	istore_2
Label7:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iconst_3
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	goto Label15
Label14:
	iconst_1
Label15:
	ifle Label18
Label19:
	goto Label8
Label20:
Label18:
	iload_2
	invokestatic io/putInt(I)V
Label11:
Label8:
	iload_2
	bipush 10
	if_icmpeq Label21
	iconst_1
	goto Label22
Label21:
	iconst_0
Label22:
	ifgt Label7
Label9:
	iload_2
	bipush 10
	if_icmplt Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label25
	goto Label4
Label25:
Label6:
Label3:
	iconst_1
	ifgt Label2
Label4:
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
