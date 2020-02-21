.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	newarray int
	astore_1
	aload_1
	iconst_0
	iconst_1
	iastore
	aload_1
	iconst_1
	iconst_2
	iastore
	aload_1
	iconst_2
	bipush 10
	iastore
	aload_1
	iconst_3
	bipush 77
	iastore
	aload_1
	iconst_4
	bipush 88
	iastore
Label2:
	bipush 77
	aload_1
	iconst_5
	invokestatic MCClass/binsearch(I[II)I
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label4:
	bipush 9
	aload_1
	iconst_5
	invokestatic MCClass/binsearch(I[II)I
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label5:
Label1:
	return
.limit stack 3
.limit locals 3
.end method

.method public static binsearch(I[II)I
.var 0 is x I from Label0 to Label1
.var 1 is v [I from Label0 to Label1
.var 2 is n I from Label0 to Label1
Label0:
	iconst_0
	istore_3
	iload_2
	iconst_1
	isub
	istore 4
Label2:
Label5:
	iload_3
	iload 4
	iadd
	iconst_2
	idiv
	istore 5
	iload_0
	aload_1
	iload 5
	iaload
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	iload 5
	iconst_1
	isub
	istore 4
	goto Label10
Label9:
	iload_0
	aload_1
	iload 5
	iaload
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label13
	iload 5
	iconst_1
	iadd
	istore_3
	goto Label14
Label13:
	iload 5
	goto Label1
Label14:
Label10:
Label6:
Label3:
	iload_3
	iload 4
	if_icmpgt Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label2
Label4:
	iconst_1
	ineg
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 6
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
