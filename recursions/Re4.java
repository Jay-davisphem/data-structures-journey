public class Re4 {
  public static void main(String[] args) {
    // runtime stack size is (15k integer == 60Kb)
    int[] arr = {2,3,4,6};
    printS(reverseArray(arr));
  }

  public static int[] reverseArray(int[] arr) {
    if (arr.length < 2) return arr;
    
    return reverseArray(arr[0]);
  }

  public static void printS(int[] arr) {
    System.out.print("{ ");
    for(int num:arr){
      System.out.print(num + " ");
    }
    System.out.println("}");
    
  }
}
