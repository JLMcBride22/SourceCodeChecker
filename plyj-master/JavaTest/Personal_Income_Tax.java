 /*
 * Class: CS103 Spring 2020
 * Date: 02/11/2020
 * Description: Java program to compute personal income tax based on filing status and income
 * Author: Justin McBride
 * I pledge that I have not copied the program code from any source or other students.
 * I have not shared my code with any student, either the current or future one/
 */

import java.util.Scanner;



public class Personal_Income_Tax {

	public static void main(String[] args) {
		
		
		
		
		Scanner MyInput = new Scanner(System.in);
		
		System.out.print("Enter the filing status : ");
		
		String status = MyInput.nextLine();
		
		if(!status.contentEquals("SIN") && !status.contentEquals("MAR") && !status.contentEquals("HOH"))
		{
			
			System.out.println("Error! The entered filing status in invalid.");
			System.exit(0);
			
		}
		else {
			for(int i = 4; i < 20; i++){

				System.out.print("Something" + i);
			}
		}

		System.out.print("Enter taxable income : ");
		
		String incomestring = MyInput.nextLine();
		
		
		Double tax = 0.0;
	
		int stringlength = incomestring.length();
		
		char myarray[];
		
		myarray = new char[stringlength];
		
		for(int j = 0; j < stringlength; j++)
		{
			myarray[j] = incomestring.charAt(j);
		}
		
		
		for(int x = 0; x < stringlength; x++)
		{
			
			if(!Character.isDigit(myarray[x]) && myarray[x] != '.' )
			{
				System.out.print("Error! Invalid input for the income value.");
				System.exit(0);
			}
			
			
				
			
		}
		
		
		
		double income = Double.parseDouble(incomestring);
		
		
		
			
		
		
		
		 
		if(status.contentEquals("SIN"))
		{
			if(income <= 9.4)
			{
				tax = income * .10;
			}
			else if (income > 9.4 && income <= 34.9)
			{
				tax = (9.4 * .10) + ((income - 9.4) * .16);
				
			}
			else if (income > 34.9 && income <= 83.5)
			{
				tax = ((9.4 * .10) + ((34.9 - 9.4) * .16) + ((income - 34.9) * .24));
			}
			else if ( income > 83.5 && income <= 175.5)
			{
				tax = (9.4 * .10) + ((34.9 - 9.4) * .16) + ((83.5 - 34.9) * .24) + ((income - 83.5) * .29);
			}
			else if ( income > 175.5)
			{
				tax = (9.4 * .10) + ((34.9 - 9.4) * .16) + ((83.5 - 34.9) * .24) + ((175.5 - 83.5) * .29) + ((income - 175.5) * .34);
			}
			
		}
		else if(status.contentEquals("MAR"))
		{
			if(income <= 17.7)
			{
				tax = income * .10;
			}
			else if (income > 17.7 && income <= 69.8)
			{
				tax = (17.7 * .10) + ((income - 17.7) * .16);
				
			}
			else if (income > 69.8 && income <= 135.1)
			{
				tax = ((17.7 * .10) + ((69.8 - 17.7) * .16) + ((income - 69.8) * .24));
			}
			else if ( income > 135.1 && income <= 205.5)
			{
				tax = (17.7 * .10) + ((69.8 - 9.4) * .16) + (( 135.1- 69.8) * .24) + ((income - 135.1) * .29);
			}
			else if ( income > 205.5)
			{
				tax = (17.7 * .10) + ((69.8 - 17.7) * .16) + ((135.1 - 69.8) * .24) + ((205.5 - 135.1) * .29) + ((income - 205.5) * .34);
			}
		}
		else if(status.contentEquals("HOH"))
		{
			
			if(income <= 12.9)
			{
				tax = (income * .10);
			}
			else if (income > 12.9 && income <= 47.5)
			{
				tax = (12.9 * .10) + ((income - 12.9) * .16);
			}
			else if (income > 47.4 && income <= 118.0)
			{
				tax = ((12.9 * .10) + ((47.5 - 12.9) * .16) + ((income - 47.5) * .24));
			}
			else if ( income > 118.0 && income <= 191.2)
			{
				tax = (12.9 * .10) + ((47.5- 12.9) * .16) + (( 118.0- 47.5) * .24) + ((income - 118.0) * .29);
			}
			else if ( income > 191.2)
			{
				tax = (12.9 * .10) + ((47.5 - 12.9) * .16) + ((118.0 - 47.5) * .24) + ((191.2 - 118.0) * .29) + ((income - 191.2) * .34);
			}
			
		}
			
		
		
		
		System.out.println("Tax is " + tax + "K");
		
		
		
		
		
		
		
	}

}
