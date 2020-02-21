.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label4:
	iconst_1
	ifle Label3
Label5:
	iconst_0
	istore_2
Label9:
	iconst_1
	ifle Label8
Label10:
	iload_2
	iload_1
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
Label15:
	goto Label8
Label16:
Label14:
	iload_2
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label11:
Label7:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label8:
	iload_1
	bipush 10
	if_icmplt Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label19
Label20:
	ldc "END"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label3
Label21:
Label19:
	invokestatic io/putLn()V
Label6:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
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
