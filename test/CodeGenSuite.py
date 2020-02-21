import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putIntLn(3);}"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_float(self):
        """Simple program: int main() {} """
        input = """void main() {putFloatLn(9.0);}"""
        expect = "9.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_global_variable(self):
        """Simple program: int main() {} """
        input = """int x; float y; boolean z; void main() {putIntLn(x); putFloatLn(y); putBoolLn(z);}"""
        expect = "0\n0.0\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_int_array_global_variables(self):
        input = """int a[3]; void main() {putIntLn(a[1]);}"""
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_bool_array_global_variables(self):
        input = """boolean a[3]; void main() {putBoolLn(a[1]);}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_simple_assignment(self):
        """Simple program: int main() {} """
        input = """void main() {int a; a=2; putIntLn(a);}"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_nested_assignment(self):
        """Simple program: int main() {} """
        input = """void main() {int a, b; a=b=2; putIntLn(a+b);}"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_array_cell(self):
        """Simple program: int main() {} """
        input = """void main() {int a[2]; a[0]=1; putIntLn(a[0]); }"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_array_cell_nested_assignment(self):
        """Simple program: int main() {} """
        input = """void main() {int a[2]; a[0]=a[1]=1; putIntLn(a[0]+a[1]*2); }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_int_arithmetic_expression(self):
        """Simple program: int main() {} """
        input = """void main() {int a[2]; a[0]=a[1]=1*3+4; putIntLn(a[0]/2+(a[1]-10)*2); }"""
        expect = "-3\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_float_arithmetic_expression(self):
        """Simple program: int main() {} """
        input = """void main() {float a[2]; a[0]=a[1]=1*3+4; putFloatLn(a[0]/2+(a[1]-10)*2); }"""
        expect = "-2.5\n"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_string_nested_assignment(self):
        """Simple program: int main() {} """
        input = """void main() {string a[2]; a[0]=a[1]="1*3+4"; putStringLn(a[0]);  putStringLn(a[1]); }"""
        expect = "1*3+4\n1*3+4\n"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_int_arithmetic_expression_with_modulo(self):
        """Simple program: int main() {} """
        input = """void main() {int a[2]; a[0]=a[1]=1*3+4; putIntLn(a[0]%2+(a[1]-10)/2); }"""
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_relational_expression_single_type_equal(self):
        """Simple program: int main() {} """
        input = """void main() {int a; int b; a=b=2; putBoolLn(a==b); }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_relational_expression_single_type_not_equal(self):
        """Simple program: int main() {} """
        input = """void main() {int a; int b; a=2*15-1; b=a+0; putBoolLn(a!=b); }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    
    def test_relational_expression_single_type_greater_than(self):
        """Simple program: int main() {} """
        input = """void main() {float a; float b; a=0.9; b=0.2*0.25; boolean c;  c=a>b; putBoolLn(c);}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test_relational_expression_float_and_int_less_than_or_equal(self):
        """Simple program: int main() {} """
        input = """void main() {float a; int b; a=1.0; b=1; boolean c;  c=a<=b; putBoolLn(c);}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_relational_expression_float_and_int_with_unaryop_less_than(self):
        """Simple program: int main() {} """
        input = """void main() {float a; int b; a=-1.0*2; b=3-5; boolean c;  c=a<b; putBoolLn(c);}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    
    def test_boolean_expression_and(self):
        """Simple program: int main() {} """
        input = """void main() {float a; float b; boolean c; a=9.5; b=-2.3; c=a>=9.5 && b>-3; putBoolLn(c);}"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_boolean_expression_or(self):
        """Simple program: int main() {} """
        input = """void main() {float a; float b; boolean c; a=9.5; b=-2.3; c=a<9.5 && b<=-3; putBoolLn(c);}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_boolean_expression_not(self):
        """Simple program: int main() {} """
        input = """void main() {float a; float b; boolean c; a=9.5; b=-2.3; c=a<9.5 && b<=-3; putBoolLn(!!!!!!c);}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_boolean_expression_multiple_combined_0(self):
        """Simple program: int main() {} """
        input = """void main() {float a; float b; boolean c; a=9.5; b=-2.3; c=a<9.5 && b<=-3 || !(a > 5.5); putBoolLn(c);}"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_boolean_expression_multiple_combined_1(self):
        """Simple program: int main() {} """
        input = """void main() {
            boolean a;
            boolean b;
            boolean c;
            a = 9 > 0 || !(1!= 0);
            b = 7 * 8 < 10 && !(b = true);
            c = a && b;
            putBoolLn(!c || a);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_equality_op_on_boolean(self):
        """Simple program: int main() {} """
        input = """void main() {
            boolean a;
            boolean b;
            boolean c;
            a = true;
            b = false;
            putBoolLn(a == b);
        }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_inequality_op_on_boolean(self):
        """Simple program: int main() {} """
        input = """void main() {
            boolean a;
            boolean b;
            boolean c;
            a = true || false;
            b = false && true;
            putBoolLn(a != b);
        }"""
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_call_expr_in_ungenerated_arithmetic_expr(self):
        """Simple program: int main() {} """
        input = """
        int c() {
            putLn();
            return 2;
        }
        void main() {
            int a;
            a = 5;
            a + 4 - a * 3 - c();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_callexpr_in_ungenerated_boolean_expr(self):
        """Simple program: int main() {} """
        input = """
        boolean  c() {
            putLn();
            return true;
        }
        void main() {
            (false || true) && c();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_callexpr_in_ungenerated_arraycell_expr(self):
        """Simple program: int main() {} """
        input = """
        int c() {
            putLn();
            return 1;
        }
        void main() {
            int arr[3];
            arr[c()];
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_callexpr_in_ungenerated_unary_op(self):
        """Simple program: int main() {} """
        input = """
        int c() {
            putLn();
            return 1;
        }
        void main() {
            int arr[3];
            -c();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_callexpr_in_ungenerated_relational_op(self):
        """Simple program: int main() {} """
        input = """
        int c() {
            putLn();
            return 1;
        }
        void main() {
            int arr[3];
            3 > -c();
        }"""
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_ungenerated_statement_with_assignment_inside(self):
        """Simple program: int main() {} """
        input = """void main() {int a; 3+(a=4); putIntLn(a);}"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_ungenerated_statement_with_assignment_inside2(self):
        """Simple program: int main() {} """
        input = """void main() {int a; (a=4)*(a=5); putIntLn(a);}"""
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    def test_ungenerated_statement_with_assignment_inside3(self):
        """Simple program: int main() {} """
        input = """void main() {int a; (a=4)==4||(a=5)==5; putIntLn(a);}"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test_ungenerated_statement_with_assignment_inside4(self):
        """Simple program: int main() {} """
        input = """void main() {int a; -(a=5); putIntLn(a);}"""
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test_assignment_inside_araycell(self):
        """Simple program: int main() {} """
        input = """int c[5]; void main() {int a;int b; c[a=b=3]; putIntLn(b);putIntLn(a);}"""
        expect = "3\n3\n"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_assignment_inside_callexpr(self):
        """Simple program: int main() {} """
        input = """int c(int b) { return b;}void main() {int a; c(a=4); putIntLn(a);}"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_ungenerated_statement_with_assignment_inside_rela_op(self):
        """Simple program: int main() {} """
        input = """void main() {int a; (a=5)>10; putIntLn(a);}"""
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_block_statement_scope(self):
        """Simple program: int main() {} """
        input = """void main() {int a; a = 2; {int a; a = 3; putIntLn(a);} putIntLn(a);}"""
        expect = "3\n2\n"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    
    def test_if_statement_simple_without_else(self):
        """Simple program: int main() {} """
        input = """void main() {int a; a = 2; float c; c = 1.0; if (a > 1) c=2.0; putFloatLn(c);}"""
        expect = "2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_if_statement_simple_without_else_assignment_expr(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = 2; boolean b; float c; c = 1.0; 
        if (b=(a > 1)) 
            c=2.99; 
        putFloatLn(c); putBoolLn(b);
        }"""
        expect = "2.99\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_if_statement_simple_with_else_complex_expr(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = 2;  float c; 
        if (a % 99 > 1.0 * 2) 
            c=2.99; 
        else
            c = 1.0; 
        putFloatLn(c); 
        }"""
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_if_statement_simple_with_else_complex_expr2(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = -2;  float c;
        if (a * 0 >= -1/2) 
            c=2.99; 
        else 
            c = 1.0; 
        putFloatLn(c); 
        }"""
        expect = "2.99\n"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_if_statement_simple_with_else_with_block(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = -2;  float c;
        if (a % 99 > 1.0 * 2) 
            c=2.99;
        else {
            int a; a = 10;
            putIntLn(a);
            c = 4.0*a;
        }
        putFloatLn(c); 
        }"""
        expect = "10\n40.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_for_statement_simple(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a[3]; int i;
        for (i = 0; i < 3; i=i+1) {
            a[i] = i;
        }
        putIntLn(a[2]); 
        }"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_for_statement_more_complex(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a[3]; int i;
        for (i = 0; i < 3; i=i+1) {
            a[i] = i;
        }
        int j, sum; sum = 0;
        for (j = 3; j > 0; j = j - 1) 
            sum = sum + a[j-1];
        putIntLn(sum);
        }"""
        expect = "3\n"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_for_statement_nested_for(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int rows, i, j; rows = 3;
        for (i=1; i<=rows; i=i+1) {
            for (j=1; j<=i; j=j+1)
            { putString("* "); }
            putLn();
        }
        }"""
        expect = "* \n* * \n* * * \n"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_for_statement_ungenerated_expr(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i; 
        for (1%(i=1); i<=4; 3*i-2) {
            putInt(i);
            i = i * 2;
        }
        }"""
        expect = "124"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_dowhile_statement_simple(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int n, rev; rev = 0;
        n = 4532; 
        do  {
            int remainder;       
            remainder = n % 10;
            rev = rev * 10 + remainder;
            n = n / 10;
        } while (n != 0);
        putIntLn(rev);
        }"""
        expect = "2354\n"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_dowhile_statement_complex_with_nested_for_and_break(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int low, high, i, flag;
        low = 200;
        high = 400;
        do 
            flag = 0;   
            for (i = 2; i <= low / 2; i=i+1) {
                if (low % i == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                putInt(low);
                putString(" ");
            }
            low=low+1;
        while (low < high);
        }"""
        expect = "211 223 227 229 233 239 241 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 "
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_simple_continue_in_while(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int j; j = 0; 
        do {
            {
                if (j == 7) {
                    j = j+1;
                    continue;
                }
                 putInt(j);
            }
            j = j+1;
        } while (j < 10);
        }"""
        expect = "012345689"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test_nested_break_in_nested_for(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int j; j = 0; 
        for (1; true; j=j+1) {
            int i;
            for (i = 0; true; i=i+1) {
                if (i >= j) {
                    break;
                }
                putInt(i);
                putString(" ");
            } 
            if (j  >= 10) {
                putStringLn("END");
                break;
            }
            putLn();
        }
        }"""
        expect = "\n0 \n0 1 \n0 1 2 \n0 1 2 3 \n0 1 2 3 4 \n0 1 2 3 4 5 \n0 1 2 3 4 5 6 \n0 1 2 3 4 5 6 7 \n0 1 2 3 4 5 6 7 8 \n0 1 2 3 4 5 6 7 8 9 END\n"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_nested_continue_in_nested_for(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int j; j = 0; 
        for (1; j<6; j=j+1) {
            int i;
            for (i = 0; i<j; i=i+1) {
                if (i % 2 == 0) {
                    continue;
                }
                putInt(i);
                putString(" ");
            } 
            if (j * 3 <= 3) {
                continue;
            }
            putLn();
        }
        }"""
        expect = "1 \n1 \n1 3 \n1 3 \n"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_nested_continue_in_nested_for_and_assignment_in_for_condition(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int j; j = 0; 
        for (1; j<6; j=j+1) {
            int i; boolean b;
            for (i = 0; b=(i<j); i=i+1) {
                if (i % 2 == 0) {
                    continue;
                }
                putInt(i);
                putString(" ");
            } 
            if (j * 3 <= 3) {
                continue;
            }
            putLn();
        }
        }"""
        expect = "1 \n1 \n1 3 \n1 3 \n"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    
    def test_return_in_nested_for(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int j; j = 0; 
        for (1; j<6; j=j+1) {
            int i; boolean b;
            for (i = 0; b=(i<j); i=i+1) {
                if (i % 2 == 0) {
                    return;
                }
                putInt(i);
                putString(" ");
            } 
            if (j * 3 <= 3) {
                continue;
            }
            putLn();
        }
        }"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test_triple_dowhile(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i, j, k, s;
        s = 0;
        i = 1;
        do  j = 1;
        do  k = j;
        do 
            k = k + 1;
            s = s + 1;
        while (k < i);
        j = j + 1;
        while (j < i);
        i = i + 1;
        while (i < 10);
        putIntLn(s);
        }
        """
        expect = "121\n"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_triple_dowhile_mix_with_break(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i, j, k, s;
        s = 0;
        i = 1;
        do  j = 1;
        do  k = j;
        do 
            k = k + 1;
            s = s + 1;
            if (k == 5) break;
        while (k < i);
        j = j + 1;
        if (j == k - 4) break;
        while (j < i);
        i = i + 1;
        while (i < 10);
        putIntLn(s);
        }
        """
        expect = "81\n"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test_triple_dowhile_mix_with_break_and_continue(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i, j, k, s;
        s = 0;
        i = 1;
        do  j = 1;
        do  k = j;
        do 
            k = k + 1;
            if (i*j*k % 3 == 0) {
                continue;
            }
            s = s + 1;
            if (k == 5) break;
        while (k < i);
        j = j + 1;
        if (i*j % 5 == 0) {
                continue;
        } s = s - 1;
        if (j == k - 4) break;
        while (j < i);
        i = i + 1;
        
        while (i < 10);
        putIntLn(s);
        }
        """
        expect = "0\n"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_similar_to_539_but_using_for(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i, j, k, s;
        s = 0;
        for (i = 0; i < 10; i=i+1) {
            for (j = 0; j < i; j=j+1) {
                for (k = j; k < i; k=k+1) {
                    if (i*j*k % 3 == 0) {
                        continue;
                    }
                    s = s + 1;
                    if (k == 5) break;
                }
                if (i*j % 5 == 0) {
                continue;
                } s = s - 1;
                if (j == k - 4) break;
            }
        }
        putIntLn(s);
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test_if_then_if_then_else_stmt_in_nested__triplefor(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int i, j, k, s;
        s = 0;
        for (i = 0; i < 10; i=i+1) {
            for (j = 0; j < i; j=j+1) {
                for (k = j; k < i; k=k+1) {
                    if (i*j % 2 == 0) 
                        if (k % 3 == 0)
                            s = s + 2 ;
                        else
                            s = s - 1;
                }
            }
        }
        putIntLn(s);
        }
        """
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_complex_relational_boolean_expression(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        boolean a;
        a = true && false || !false && (true || false);
        boolean b;
        b = 4 * -1 > -5.0 + 100;
        if (a && b) 
            putString("True");
        else
            putString("False");
        }
        """
        expect = "False"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_arithmetic_expression_in_arraycell(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            float arr[5];
            arr[4-1*100/99] = 4.0;
            arr[3/2] = 9 * -  2 / 4;
            arr[3*0*10000] = 0;
            arr[2] = arr[4] = arr[3] * arr[1] - 9;
            int i;
            for (i = 0; i < 5; i=i+1) {
                putFloat(arr[i]);
            } 
        }
        """
        expect = "0.0-4.0-25.04.0-25.0"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    
    def test_block_scope_in_nested_dowhile(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a;
        a = 0;
        do {
            a = 5;
            int a; a = 0;
            do {
                a = a + 1;
                if (a % 3 == 0 || a % 2 == 0) {
                    continue;
                }
                putInt(a);
            }  while (a != 10);
            if (a >= 10) break;
        } while (true);
        }"""
        expect = "157"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_scope_complex(self):
        """Simple program: int main() {} """
        input = """
        int i;
        int f() {
            return 200;
        }
        void main() {
            int main;
            main = f();
            putIntLn(main);
            {
                int i, main, f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = "200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_scope_complex_and_global_variable_appear_after_any_function(self):
        """Simple program: int main() {} """
        input = """
        int f() {
            return i;
        }
        void main() {
            int main;
            main = f();
            putIntLn(main);
            {
                int i, main, f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        int i;
        """
        expect = "0\n100\n100\n100\n0\n"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_scope_for_global_variable_nested_complex_block(self):
        input = """
        float a;
        void main()
        {
            putFloatLn(a);
            {
                {
                    float a;
                    a =4.5;
                    putFloatLn(a);
                    {
                        float a;
                        a =10.0;
                        putFloatLn(a);
                    }
                    {
                        float a;
                        a=9.0;
                        putFloatLn(a);
                    }
                }
                a = 1.0;
            }
            putFloatLn(a);
        }
        """
        expect = """0.0\n4.5\n10.0\n9.0\n1.0\n"""
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_if_statement_wrong_without_short_circuit(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = 0; boolean c; c=false;
        if (a != 0 && (c = !(a==1))) {
            putStringLn("here");
        }
        putBoolLn(c);
        }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    def test_if_statement_wrong_without_short_circuit2(self):
        """Simple program: int main() {} """
        input = """
        void main() {
        int a; a = 0;
        if (!(a <- 1) || 5 / a == 2) {
            putStringLn("here");
        }
        }"""
        expect = "here\n"
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_nested_nested_call_expr(self):
        """Simple program: int main() {} """
        input = """
        int foo(int a) {
            return -a;
        }
        void main() {
            int a;
            a = 4;
            putIntLn(foo(foo(foo(foo(a)))));
        }"""
        expect = "4\n"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_multiple_assigment(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int a;
            a = 4;
            int b, c, d, e, f;
            a = b = c = d = e = f = 4;
            putInt(a*b*c*d*e*f);
        }"""
        expect = "4096"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_multiple_assigment_arraycell(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int arr[5];
            arr[0] =  arr[1] =  arr[2] =  arr[3] =  arr[4] = 4;
            putInt(arr[0]*arr[1]*arr[2]*arr[3]*arr[4]);
        }"""
        expect = "1024"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_return_statement_for_simple_function_add(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int b,c;
            b = 9;
            c = 10;
            putIntLn(add(b,c));
        }
        int add(int a, int b) {
            return a + b;
        }"""
        expect = "19\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_return_statement_for_simple_function_float_pass_by_value(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int b,c;
            b = 9;
            c = 10;
            swap(b,c);
            putFloatLn(b);
        }
        void swap(float a, float b) {
            float tmp;
            tmp = a;
            a = b;
            b = tmp;
        }"""
        expect = "9.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_return_statement_for_simple_function_return_float_type_coercion(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            float b;
            b = intToFloat(5);
            putFloatLn(b);
        }
        float intToFloat(int a) {
            return a;
        }"""
        expect = "5.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_return_statement_for_simple_function_return_array_pointer(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            putFloatLn(returnFloat()[2]);
        }
        float[] returnFloat() {
            float a[3]; int i;
            for (i  = 0; i < 3; i=i+1)
                a[i] = (i+1) * 0.25;
            return a;
        }"""
        expect = "0.75\n"
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_return_statement_for_simple_function_param_array_pointer(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            boolean bs[4];
            int i;
            i = 0;
            do {
                int j;
                j = i;
                bs[j] = true;
            } i = i + 1; while (i < 4);
            putBoolLn(returnBool(bs)[2]);
        }
        boolean[] returnBool(boolean bs[]) {
            bs[2] = false;
            return bs;
        }"""
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_return_statement_for_simple_function_param_string_array(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            string arr[3];
            arr[0]="HelloWorld\\n";
            arr[1]="BotHere\\n";
            arr[2]="Decoded\\n";
            printStringArray(arr, 3);
        }
        void printStringArray(string bs[], int n) {
            int i;
            for (i = 0; i < n; i=i+1) {
                putString(bs[i]);
            }
        }"""
        expect = "HelloWorld\nBotHere\nDecoded\n"
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_complex_function_gcd_recursive_return_in_both_ifelse(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int n1, n2;
            n1 = 366;
            n2 = 60;
            putIntLn(gcd(366, 30));
        }
        int gcd(int n1,int n2) {
            if (n2 != 0)
                return gcd(n2, n1 % n2);
            else
                return n1;
        }"""
        expect = "6\n"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_function_return_in_for_loop(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            putIntLn(looping());
        }
        int looping() {
            for (1; true; 2) {
                return 2;
            }
            return 3;
        }"""
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_function_return_in_dowhile_loop(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            putFloatLn(looping());
        }
        float looping() {
            int i;
            i = 3;
            do {
                {
                    int a; 
                    a = 4;
                    putIntLn(a);
                    return 3;
                }
                
            } i = i + 1;while (i  < 10);
        }"""
        expect = "4\n3.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,578))
    def test_complex_function_binary_search_test_elseif_in_while_infunction(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int a[5];
            a[0] =  1;
            a[1] =  2;
            a[2] =  10;
            a[3] =  77;
            a[4] =  88;
            {
                int b;
                b = binsearch(77, a, 5);
                putIntLn(b);
            }
            {
                int c;
                c = binsearch(9, a, 5);
                putIntLn(c);
            }
        }
        int binsearch(int x, int v[], int n)
        {
            int low, high;
            low = 0;
            high = n - 1;
            do {
                int mid;
                mid = (low+high)/2;
                if (x < v[mid])
                    high = mid - 1;
                else if (x > v[mid])
                    low = mid + 1;
                else 
                    return mid;
            } while (low <= high);
            return -1;
        }
        """
        expect = "3\n-1\n"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_complex_function_print_array_return_early_in_if_stmt(self):
        """Simple program: int main() {} """
        input = """
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            if (i >= n) {
                return;
            }
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int a[5];
            a[0] =  4;
            a[1] =  1;
            a[2] =  55;
            a[3] =  9;
            a[4] =  49;
            printArr(a, 0);
        }
        
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_complex_function_shell_sort_nested_for_in_function_change_array_in_place(self):
        """Simple program: int main() {} """
        input = """
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            if (i >= n) {
                return;
            }
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int a[5];
            a[0] =  4;
            a[1] =  1;
            a[2] =  55;
            a[3] =  9;
            a[4] =  49;
            shellsort(a, 5);
            printArr(a, 5);
        }
        void shellsort(int v[], int n)
        {
            int gap, i, j;
            for (gap = n/2; gap > 0; gap = gap / 2)
            for (i = gap; i < n; i=i+1)
            for (j=i-gap; j>=0 && v[j]>v[j+gap]; j=j-gap) {
                int temp;
                temp = v[j];
                v[j] = v[j+gap];
                v[j+gap] = temp;
            }
        }
        """
        expect = "1 4 9 49 55 "
        self.assertTrue(TestCodeGen.test(input,expect,581))
    def test_complex_function_is_subset(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int a[5];
            a[0] =  4;
            a[1] =  1;
            a[2] =  55;
            a[3] =  9;
            a[4] =  49;
            int b[3];
            b[0] = 1;
            b[1]= 55;
            b[2] = 9;
            putBoolLn(isSubset(a, b, 5, 3));
        }
        boolean isSubset(int arr1[], int arr2[],  
                        int m, int n) 
        { 
            int i;
            int j; 
            for (i = 0; i < n; i=i+1) 
            { 
                for (j = 0; j < m; j=j+1) 
                { 
                    if(arr2[i] == arr1[j]) 
                        break; 
                } 
                if (j == m) 
                    return 0; 
            } 
            return 1; 
        } 
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_complex_function_find_sqrt(self):
        """Simple program: int main() {} """
        input = """
        float abs(float x) {
            if (x >= 0) 
                return x;
            else
                return -x;
        }
        void main() {
            float n;
            n= 3;
            findSqrt(n);
        }
        float Square(float n, float i, float j) 
        { 
            float mid;
            mid = (i + j) / 2; 
            float mul;
            mul = mid * mid; 

            if ((abs(mul - n) < 0.0001)) 
                return mid; 
            else if (mul < n) 
                return Square(n, mid, j); 
            else
                return Square(n, i, mid); 
        } 
        

        void findSqrt(float n) 
        { 
            float i;
            i = 1; 
            boolean found;
            found = false; 
            do {
                if (abs(i * i - n) < 0.0001) { 
                    putFloat(i);
                    found = true; 
                } 
                else if (i * i > n) { 
                    float res;
                    res = Square(n, i - 1, i); 
                    putFloat(res);
                    found = true; 
                }
                i=i+1;
            } while (!found);
        } 
        """
        expect = "1.7320557"
        self.assertTrue(TestCodeGen.test(input,expect,583))
   
    def test_callexpr_in_arraycell(self):
        """Simple program: int main() {} """
        input = """
        int c() {
            return 9;
        }
        void main() {
            float arr[5];
            arr[4-1*100/99] = 4.0;
            arr[3/2] = 9 * -  2 / 4;
            arr[3*0*10000] = 0;
            arr[2] = arr[c()/2] = arr[3] * arr[1] - 9;
            int i;
            for (i = 0; i < 5; i=i+1) {
                putFloat(arr[i]);
            } 
        }
        """
        expect = "0.0-4.0-25.04.0-25.0"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_all_kind_of_expression_on_call_expr(self):
        """Simple program: int main() {} """
        input = """
        void testInt(int a) {
            putIntLn(a*2+b[1]);
        }
        void testFloat(float a) {
            putFloatLn(a/0.01);
        }
        void testBool(boolean a) {
            putBoolLn(!a);
        }
        int a; int b[5];
        void main() {
            b[1] = 4; b[2] = 8;
            testInt((a+1) * 2 - (b[2]-1)%2);
            testFloat(b[1] % 3);
            testBool(b[1] > 5 && b[2]*(a+1) > 4.0 || !(b[1]*b[2] <= 32));
        }
        """
        expect = "6\n100.0\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_callexpr_on_call_expr(self):
        """Simple program: int main() {} """
        input = """
        int testInt(int a) {
            return a*2+b[1];
        }
        float testFloat(float a) {
            return a/0.01;
        }
        boolean testBool(boolean a) {
            return !a;
        }
        int a; int b[5];
        void main() {
            b[1] = 4; b[2] = 8; a=1;
            putIntLn(testInt(testInt(a) * 2 - (b[2]-1)%2));
            putFloatLn(testFloat(b[1] % 3 - testFloat(a+0.01)));
            putBoolLn(testBool(b[1] > 5 && b[2]*(a+1) > 4.0 || testBool(!!!(a > 1))));
        }
        """
        expect = "26\n-10000.0\ntrue\n"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_expression_that_have_side_effect_shortcurcuit(self):
        """Simple program: int main() {} """
        input = """

        boolean foo(int a) {
            putIntLn(a);
            return true;
        }
        void main() {
            int b;
            b = 5;
            if (true || foo(b)) {

            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_expression_that_have_side_effect_shortcurcuit_ungenerated_expr(self):
        """Simple program: int main() {} """
        input = """

        boolean foo(int a) {
            putIntLn(a);
            return true;
        }
        void main() {
            int b;
            b = 5;
            true && (b=3)>5 && foo(b);
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_expression_that_have_side_effect_assignment(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int b;
            b = 5;
            a + b - 1 % 10 / (b = 2);
            putIntLn(b);
        } int a;
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_expression_that_have_side_effect_assignment_in_callexpr(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int b;
            b = 5; boolean c;
            putBoolLn(c=(b>100));
        }
        """
        expect = "false\n"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_expression_that_have_side_effect_assignment_in_relationalop(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            int c;
            if ((c = 100) > 4 && c == 100) {
                putIntLn(c);
            }    
        }
        """
        expect = "100\n"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_full_program_quick_sort(self):
        """Simple program: int main() {} """
        input = """
        void quicksort(int number[],int first,int last){
            int i, j, pivot, temp;

            if(first<last){
                pivot=first;
                i=first;
                j=last;

                do {
                    for (0; number[i]<=number[pivot]&&i<last; i=i+1) {

                    }
                    for (1; number[j]>number[pivot]; j=j-1) {

                    }
                    if(i<j){
                        temp=number[i];
                        number[i]=number[j];
                        number[j]=temp;
                    }
                } while(i<j);

                temp=number[pivot];
                number[pivot]=number[j];
                number[j]=temp;
                quicksort(number,first,j-1);
                quicksort(number,j+1,last);
            }
        }
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int arr[10];
            arr[0] = 95;
            arr[1] = 26;
            arr[2] = 45;
            arr[3] = 0;
            arr[4] = 99;
            arr[5] = -3;
            arr[6] = 78;
            arr[7] = -9;
            arr[8] = 9;
            arr[9] = 25;
            quicksort(arr, 0, 9);
            printArr(arr, 10);
        }
        """
        expect = "-9 -3 0 9 25 26 45 78 95 99 "
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_full_program_bubble_sort(self):
        """Simple program: int main() {} """
        input = """
        void bubbleSort(int number[],int count){
            int i, j;
            for(i=count-2;i>=0;i=i-1){
                for(j=0;j<=i;j=j+1){
                    if(number[j]>number[j+1]){
                        int temp;
                        temp=number[j];
                        number[j]=number[j+1];
                        number[j+1]=temp;
                    }
                }
            }
        }
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int arr[10];
            arr[0] = 95;
            arr[1] = 26;
            arr[2] = 45;
            arr[3] = 0;
            arr[4] = 99;
            arr[5] = -3;
            arr[6] = 78;
            arr[7] = -9;
            arr[8] = 9;
            arr[9] = 25;
            bubbleSort(arr, 10);
            printArr(arr, 10);
        }
        """
        expect = "-9 -3 0 9 25 26 45 78 95 99 "
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_full_program_remove_duplicate_element(self):
        """Simple program: int main() {} """
        input = """
       
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int arr[10];
            arr[0] = 95;
            arr[1] = 26;
            arr[2] = 45;
            arr[3] = 26;
            arr[4] = 95;
            arr[5] = -3;
            arr[6] = 78;
            arr[7] = -9;
            arr[8] = 95;
            arr[9] = 78;
            int n;
            n = 10;
            int i;
            for(i = 0; i < n; i=i+1)
            {   
                int j;
                for(j = i+1; j < n; 0)
                {
                    if(arr[j] == arr[i])
                    {
                        int k;
                        for(k = j; k < n-1; k=k+1)
                        {
                            arr[k] = arr[k+1];
                        }
                        n=n-1;
                    }
                    else
                    {
                        j=j+1;
                    }
                }
            }
            printArr(arr, n);
        }
        """
        expect = "95 26 45 -3 78 -9 "
        self.assertTrue(TestCodeGen.test(input,expect,594))
    def test_full_program_linear_search(self):
        """Simple program: int main() {} """
        input = """
        int linearSearch(int arr[], int n, int find) {
            int i; i = 0;
            do if (n == 0) break;
            if (arr[i] == find)
                return i;
            i = i + 1; 
            while (i < n);
            return -1;
        }
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int arr[10];
            arr[0] = 95;
            arr[1] = 26;
            arr[2] = 45;
            arr[3] = 26;
            arr[4] = 95;
            arr[5] = -3;
            arr[6] = 78;
            arr[7] = -9;
            arr[8] = 95;
            arr[9] = 78;
            putIntLn(linearSearch(arr, 10, 46));
            
        }
        """
        expect = "-1\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    def test_full_program_insertion_sort(self):
        """Simple program: int main() {} """
        input = """
        void insertSort(int arr[],int n){
            int i, key, j;  
            for (i = 1; i < n; i=i+1) 
            {  
                key = arr[i];  
                j = i - 1;  
                do 
                {  if (j < 0 || arr[j] <= key) break;
                    arr[j + 1] = arr[j];  
                    j = j - 1;  
                }  while (j >= 0 && arr[j] > key);
                arr[j + 1] = key;  
            }  
        }
        void printArr(int arr[], int n) {
            int i;
            i = 0;
            do 
                putInt(arr[i]);
                putString(" " );
             i = i + 1; while (i<n);
        }
        void main() {
            int arr[10];
            arr[0] = 95;
            arr[1] = 26;
            arr[2] = 45;
            arr[3] = 0;
            arr[4] = 99;
            arr[5] = -3;
            arr[6] = 78;
            arr[7] = -9;
            arr[8] = 9;
            arr[9] = 25;
            insertSort(arr, 10);
            printArr(arr, 10);
        }
        """
        expect = "-9 -3 0 9 25 26 45 78 95 99 "
        self.assertTrue(TestCodeGen.test(input,expect,596))
    def test_full_program_binary_conversion(self):
        """Simple program: int main() {} """
        input = """
        int binary_conversion(int num)
        {
            if (num == 0)
            {
                return 0;
            }
            else
            {
                return (num % 2) + 10 * binary_conversion(num / 2);
            }
        }
        void main() {
            int a;
            a = 78;
            putIntLn(binary_conversion(78));
            
        }
        """
        expect = "1001110\n"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_return_early(self):
        """Simple program: int main() {} """
        input = """
        boolean leap(int year) {
            if (year % 400 == 0) return true;
            if (year % 100 == 0) return false;
            if (year % 4 == 0) return true;
            return false;
        }
        void main() {
            putBoolLn(leap(2012));
            putBoolLn(leap(2000));
            putBoolLn(leap(1900));
            putBoolLn(leap(1901));
        }
        """
        expect = "true\ntrue\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    def test_array_pointer_function_ungenerated_array_cell(self):
        """Simple program: int main() {} """
        input = """
        int[] foo() {
            int a[3];
            a[1] = 2;
            putIntLn(a[1]);
            return a;
        }
        void main() {
            foo()[2];
        }
        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input,expect,599))
    