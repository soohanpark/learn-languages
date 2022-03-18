package finalexam1;

import java.util.ArrayList;

public class ChoiceQuestion extends Question {
	private ArrayList<String> choices;
	
	public ChoiceQuestion() {
		choices = new ArrayList<String>();
	}
	
	public void addChoice(String choice, boolean correct) {
		choices.add(choice);
		if (correct) {
			// convert choices.size() to string
			String choiceString = "" + choices.size();
			setAnswer(choiceString);
		}
	}
	
	public void display() {
		super.display();
		
		// display choices
		for (int i=0; i < choices.size(); i++) {
			int choiceNumber = i+1;
			System.out.println(choiceNumber + ": " + choices.get(i));
		}
	}
}