.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I
.field static y F
.field static z Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.x I
	invokestatic io/putIntLn(I)V
	getstatic MCClass.y F
	invokestatic io/putFloatLn(F)V
	getstatic MCClass.z Z
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 1
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
Label1:
	return
.limit stack 1
.limit locals 0
.end method
