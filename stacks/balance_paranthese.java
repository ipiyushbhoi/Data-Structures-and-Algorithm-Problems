import java.util.*;
public class MyClass {
    public static boolean check(String s)
    {
        int i;
       Stack<Character> st=new Stack<>();
      
      for(i=0;i<s.length();i++)
      {
          if(s.charAt(i)!=')')
          {
              st.push(s.charAt(i));
          }
          else
          {
              if(st.peek()=='(')
              {
                   return true;
              }
              while(st.peek()!='(')
              {
                  st.pop();
              }
              st.pop();
              
          }
          
      }
       return false;
     
    }
    public static void main(String args[]) {
     
      
      String expr="((a+b))";
      if(check(expr))
      {
        System.out.print("True");  
      }
      else
      {
      System.out.print("False");
      }
    }
}