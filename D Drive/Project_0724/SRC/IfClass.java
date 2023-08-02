
public class IfClass {

	public static void main(String[] args) {

		int myAge = 25;
		int voteingAge = 18; 

		if (myAge >= voteingAge) {
			System.out.println("Old Enought to Vote!");
		}
		else {
			System.out.println("Not old enought to vote");
		}
		
		System.out.println("=========================");
		
		int time = 22; 
		
		if (time < 10) {
			System.out.println("Good Morning");
		}
		else if(time <18) {
			 System.out.println("Good day");
		}
		else {
			System.out.println("Good evening");
		}
	} 
}
