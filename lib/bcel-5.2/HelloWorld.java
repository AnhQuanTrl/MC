public class HelloWorld {
    public static void main(String[] args) {
	
    }
	public static void findSqrt(float n) 
        { 
            float i;
            i = 1; 
            boolean found;
            found = false; 
            do {
                if (i * i == n) { 
                    found = true; 
                } 
                else if (i * i > n) { 
                    float res;
                    res = 3; 
                    found = true; 
                }
                i=i+1;
            } while (!found);
        } 
  }