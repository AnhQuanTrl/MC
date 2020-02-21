.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifle Label2
	iconst_0
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_0
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	ifgt Label10
	iconst_0
	goto Label11
Label10:
	iconst_1
Label11:
	goto Label9
Label8:
	iconst_0
Label9:
	goto Label5
Label4:
	iconst_1
Label5:
	istore_1
	iconst_4
	iconst_1
	ineg
	imul
	i2f
	ldc 5.0
	fneg
	bipush 100
	i2f
	fadd
	fcmpl
	ifle Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	istore_2
	iload_1
	ifle Label14
	iload_2
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	ldc "True"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label17
Label16:
	ldc "False"
	invokestatic io/putString(Ljava/lang/String;)V
Label17:
Label1:
	return
.limit stack 3
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
