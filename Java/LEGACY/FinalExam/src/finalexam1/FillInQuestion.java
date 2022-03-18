package finalexam1;

public class FillInQuestion extends Question{
	
	private String ans1;
	private String ans2;

	public void setAnswer(String correctResponse1, String correctResponse2) {
		this.ans1 = correctResponse1;
		this.ans2 = correctResponse2;
	}
	
	public boolean checkAnswer(String response) {
		
		String[] corans = response.split(" ");
		
		if (corans[0].equals(ans1) && corans[1].equals(ans2))
			return true;
		else
			return false;
	}
}
