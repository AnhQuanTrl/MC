.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b [I

.method public static testInt(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	imul
	getstatic MCClass.b [I
	iconst_1
	iaload
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 3
.limit locals 1
.end method

.method public static testFloat(F)F
.var 0 is a F from Label0 to Label1
Label0:
	fload_0
	ldc 0.01
	fdiv
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static testBool(Z)Z
.var 0 is a Z from Label0 to Label1
Label0:
	iload_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	goto Label1
Label1:
	ireturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.b [I
	iconst_1
	iconst_4
	iastore
	getstatic MCClass.b [I
	iconst_2
	bipush 8
	iastore
	iconst_1
	putstatic MCClass.a I
	getstatic MCClass.a I
	invokestatic MCClass/testInt(I)I
	iconst_2
	imul
	getstatic MCClass.b [I
	iconst_2
	iaload
	iconst_1
	isub
	iconst_2
	irem
	isub
	invokestatic MCClass/testInt(I)I
	invokestatic io/putIntLn(I)V
	getstatic MCClass.b [I
	iconst_1
	iaload
	iconst_3
	irem
	i2f
	getstatic MCClass.a I
	i2f
	ldc 0.01
	fadd
	invokestatic MCClass/testFloat(F)F
	fsub
	invokestatic MCClass/testFloat(F)F
	invokestatic io/putFloatLn(F)V
	getstatic MCClass.b [I
	iconst_1
	iaload
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	getstatic MCClass.b [I
	iconst_2
	iaload
	getstatic MCClass.a I
	iconst_1
	iadd
	imul
	i2f
	ldc 4.0
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label8
	getstatic MCClass.a I
	iconst_1
	if_icmple Label10
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
	invokestatic MCClass/testBool(Z)Z
	goto Label9
Label8:
	iconst_1
Label9:
	invokestatic MCClass/testBool(Z)Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
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

.method public static <clinit>()V
Label0:
	iconst_5
	newarray int
	putstatic MCClass.b [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
