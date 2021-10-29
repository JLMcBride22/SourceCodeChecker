public class CyclomaticComplexityDemo {
    //https://dev.to/designpuddle/coding-concepts---cyclomatic-complexity-3blk
       public static void main(String[] args) {
       
       int[][]A;
       int p,x;
       x = 0;
       while(x < 100){
           if(A[x] % 2 == 0){
               p = 0;
           }else{
               p = 1;
           }
           switch(p){
               case 0:
               System.out.println("even");
               break;
               case 1:
               System.out.println("odd");
               break;
               default:
               System.out.println("not good");
               break;


           }



           x++;
       }

       
       }
       }