.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	sipush 200
	istore_1
	sipush 400
	istore_2
Label2:
	iconst_0
	istore 4
	iconst_2
	istore_3
Label7:
	iload_3
	iload_1
	iconst_2
	idiv
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
Label10:
	iload_1
	iload_3
	irem
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
Label15:
	iconst_1
	istore 4
	goto Label6
Label16:
Label14:
Label11:
Label5:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label7
Label6:
	iload 4
	iconst_0
	if_icmpne Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label19
Label20:
	iload_1
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label21:
Label19:
	iload_1
	iconst_1
	iadd
	istore_1
Label3:
	iload_1
	iload_2
	if_icmpge Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifgt Label2
Label4:
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
