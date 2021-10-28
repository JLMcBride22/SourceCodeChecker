package com.stc.cc;
/**
 *
 * @author Aparajita
 *
 */
 
public class CyclomaticComplexityDemo {
 
       public static void main(String[] args) {
 
             // TODO Auto-generated method stub
 
             int var1 = 10;
             int var2 = 9;
             int var3 = 8;
             int var4 = 7;
           
             if (var1 == 10){
 
                    if(var2 > var3){
 
                           var2 = var3;
 
                    }
 
                    else{
 
                           if (var3 > var4){
 
                                 var3 = var4;
 
                           }
 
                           else{
 
                                 var4 = var1;
 
                           }
 
                    }
 
             }
 
             else{
 
                    var1=var4;
 
             }
 
             System.out.println("Printing value for var1, var2, var3, and var4"+var1+" "+var2+" "+var3+" "+var4); 
 
       }
 
}








