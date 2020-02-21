.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.a F
	invokestatic io/putFloatLn(F)V
Label2:
Label4:
	ldc 4.5
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
Label6:
	ldc 10.0
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label7:
Label8:
	ldc 9.0
	fstore_2
	fload_2
	invokestatic io/putFloatLn(F)V
Label9:
Label5:
	ldc 1.0
	putstatic MCClass.a F
Label3:
	getstatic MCClass.a F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
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

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
