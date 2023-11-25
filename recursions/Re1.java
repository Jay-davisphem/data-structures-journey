public class Re1 {
  int cut = 0;
  public static void main(String[] args) {
    System.out.println("Hello");
    Re1 re1 = new Re1();
    re1.f();
  }

  public void f() {
    if (cut == 100) return;
    System.out.println(cut);
    cut++;
    f();
  }
}
