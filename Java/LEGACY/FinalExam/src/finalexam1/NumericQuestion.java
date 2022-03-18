package finalexam1;

public class NumericQuestion extends Question{
	private double answerValue;
	
	public void setAnswer(String correctResponse) {
		answerValue = Double.parseDouble(correctResponse);
	}
	public boolean checkAnswer(String response) {
		double responseValue;
		responseValue = Double.parseDouble(response);
		double difference = Math.abs(answerValue-responseValue);
		if (difference <= 0.01) return true;
		else return false;
	}

}