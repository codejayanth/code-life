public class Main {
  static void myMethod () {
    System.out.println("This is method kingdom");
  }

  static void myAddMethod (int a, int b) {
    System.out.println("The result is: "+ (a + b));
  }

  static int myMulMethod (int num1, int num2) {
    return num1 * num2;
  } 
    public static void main(String[] args) {
      myMethod();
      myAddMethod(123, 345);
      System.out.println("The multiplication of 23, 46 is: "+ myMulMethod(23, 46));
      String name = "John", lname = "Reddy";
      System.out.println(name + " " + lname);
      System.out.println(Math.max(20, 89));
      System.out.println(Math.sqrt(23));
      System.out.println("The data is \"going bonkers\" when i deal with it");
      System.out.println(Math.random());
      int x = 40, y = 40;
      if (x > y) {
        System.out.println("The value x is greater than y");
      } else if (x == y) {
        System.out.println("The value x is equal to y");
      } else {
        System.out.println("The value x is smaller than y");
      }
      int a = 40, b = 60;
      String result = (a > b) ? "A is greater than B" : "A is lesser than B";
      System.out.println("The result is" + result);

      int i = 0;
      while (i < 5) {
        System.out.println("The value is: " + i);
        i ++;
      }

      for (i=0; i <=5; i++) {
        System.out.println("The value: " + i);
      }

      for (i= 0; i <= 100; i+=10) {
        System.out.println("The value of tens is: "+ i);
      }

      String[] names = {"Jayanth", "reddy"};
      System.out.println("The names are: "+ names[0]);
      System.out.println("The length is: "+ names.length);

      for (String j : names) {
        System.out.println(j);
      }
    }
  }