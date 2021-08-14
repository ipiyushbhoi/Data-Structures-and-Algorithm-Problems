import java.util.*;
public class MyClass {
    public static void main(String args[]) {
      
      
      ArrayList<Integer> result=new ArrayList<Integer>();
      
    
      int[][] matrix={{1,2,3},{4,5,6},{7,8,9}};
      int m=matrix.length;
      int n=matrix[0].length;
      
      int x,y;
      x=0;
      y=0;
      int i;
      while(m>0 && n>0)
      {
          if(m==1){
            for(i=0;i<n;i++)
                result.add(matrix[x][y++]);
            break;}
          else if(n==1){
            for(i=0;i<m;i++)
                result.add(matrix[x++][y]);
            break;}
                
        for(i=0;i<n-1;i++)
            result.add(matrix[x][y++]);
            
        for(i=0;i<m-1;i++)
            result.add(matrix[x++][y]);
            
        for(i=0;i<n-1;i++)
            result.add(matrix[x][y--]);
            
        for(i=0;i<m-1;i++)
            result.add(matrix[x--][y]);
            
        x++;
        y++;
        m-=2;
        n-=2;
      }
     

      System.out.println(result);
    }
}