public class Re2 {
  public static void main(String[] args) {
    Re2 re2 = new Re2();    
    re2.printNameN("Oluwafemi David", 5);

    re2.printNum(9);
  }

  public void printNameN(String name, int n) {
    /*
     * printNameN(name, n) 
     * |
     * V 
     * printNameN(name, n - 1) 
     * |
     * V 
     * printNameN(name, n - 2) 
     * ...
     * |
     * V
     * printNameN(name, 0)
     * */
    if (n == 0) return;
    System.out.println(name);
    printNameN(name, --n);
  }

  public void printNum(int n) {
    /*
     let printNum == f
     In runtime stack: f(n) -> f(n - 1) -> f(n - 2) ... -> f(0)
     popping begins since n is now 0
     f(0) popped out and print 0 + 1 = 1
     f(1) popped out and print 1 + 1 = 2
     hence the sequence 1,2,3,..., n
     */
    if (n == 0) return;
    printNum(--n);
    System.out.println(n+1);
  }
}

