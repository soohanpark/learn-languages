package question;

import java.util.Scanner;
 

public class QuestionDemo2{
	static Scanner scan = new Scanner(System.in);
	
	public static void main(String[] args) {
		ChoiceQuestion first = new ChoiceQuestion("What was the original name of the Java language?");
		//first.setText("What was the original name of the Java language?");
		first.addChoice("*7", false);
		first.addChoice("Duke", false);
		first.addChoice("Oak", true);
		first.addChoice("Gosling", false);

		ChoiceQuestion second = new ChoiceQuestion("In which country was the inventor of Java born?");
		//second.setText("In which country was the inventor of Java born?");
		second.addChoice("Australia", false);
		second.addChoice("Canada", true);
		second.addChoice("Denmark", false);
		second.addChoice("U.S.A.", false);
		
		presentQuestion(first);
		presentQuestion(second);
	}
	
	public static void presentQuestion(ChoiceQuestion q) {
		q.display();
		System.out.println("Your Answer : ");
		String response = scan.nextLine();
		System.out.println(q.checkAnswer(response));
	}
}
