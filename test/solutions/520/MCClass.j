.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 9.5
	fstore_1
	ldc 2.3
	fneg
	fstore_2
	fload_1
	ldc 9.5
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	fload_2
	iconst_3
	ineg
	i2f
	fcmpl
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	goto Label5
Label4:
	iconst_0
Label5:
	istore_3
	iload_3
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
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
