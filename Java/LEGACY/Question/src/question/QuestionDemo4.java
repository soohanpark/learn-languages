package question;

import java.util.Scanner;

public class QuestionDemo4 {

	public static void main(String[] args) {
		NumericQuestion nu = new NumericQuestion();
		nu.setText("(182+45.2)/4 = ?");
		nu.setAnswer("56.8");
		
		presentQuestion(nu);

	}
	
	public static void presentQuestion(Question q) {
		q.display();
		System.out.println("Your answer : ");
		Scanner scan = new Scanner(System.in);
		String response = scan.nextLine();
		System.out.println(q.checkAnswer(response));
		scan.close();
	}
}
