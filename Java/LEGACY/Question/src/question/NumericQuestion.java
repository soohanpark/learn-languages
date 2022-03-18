package question;

public class NumericQuestion extends Question{
	
	String answer;
	
	public NumericQuestion() {
		super();
	}
	
	public NumericQuestion(String text) {
		super(text);
	}
	
	@Override
	public boolean checkAnswer(String response) {
		double res = Double.parseDouble(response);
		double ans = Double.parseDouble(answer);
		
		if (Math.abs(ans-res)<0.01)
			return true;
		else
			return false;
	}
	
	@Override
	public void setAnswer (String correctResponse) {
		super.setAnswer(correctResponse);
		answer = correctResponse;
	}
	
}
