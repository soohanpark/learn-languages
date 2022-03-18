package question;

import java.util.Scanner;

public class QuestionDemo3 {
	
	static Scanner scan = new Scanner(System.in);
	
	public static void main(String[] args) {
		Question first = new Question();
		first.setText("Who was the inventor of Java?");
		first.setAnswer("James Gosling");
		
		ChoiceQuestion second = new ChoiceQuestion();
		second.setText("In which country was the inventor of Java born?");
		second.addChoice("Australia", false);
		second.addChoice("Canada", true);
		second.addChoice("Denmark", false);
		second.addChoice("U.S.A.", false);
		/*
		NumericQuestion third = new NumericQuestion();
		third.setText("(182+45.2)/4 = ?");
		third.setAnswer("56.8");
		
		presentQuestion(first);
		presentQuestion(second);
		presentQuestion(third);*/
	}
	
	public static void presentQuestion(Question q) {
		q.display();
		System.out.println("Your answer : ");
		String response = scan.nextLine();
		System.out.println(q.checkAnswer(response));
		scan.close();
	}
}
