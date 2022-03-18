package question;

import java.util.Scanner;

public class QuestionDemo1 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		Question q = new Question();
		q.setText("Who was the inventor of Java?");
		q.setAnswer("James Gosling");
		
		q.display();
		System.out.println("Your answer : ");
		String response = scan.nextLine();
		System.out.println(q.checkAnswer(response));
		scan.close();
	}

}
