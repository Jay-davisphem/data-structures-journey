public class Re3 {
  public static void main(String[] args) {
    // runtime stack size is (15k integer == 60Kb)
    System.out.println(sumRe(20000));
    System.out.println(fact(30L));
  }

  public static int sum(int n, int sum) {
    if (n < 1) return sum;
    return sum(n - 1, sum + n);
  }
  public static int sum(int n){
    if (n < 1) return n;
    return n + sum(n - 1);
  }
  public static int sumRe(int n) {
    return sum(n)+sum(n, 2);
  }

  public static long fact(long n){
    if (n < 0) return -1;
    else if (n == 0 || n == 1) return 1;
    else{
      return n * fact(n - 1);
    }
  }
}

