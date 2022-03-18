package quiz1_2;

public class PriceMeasurer implements Measurer{
	public double measure(Object anObject) {
		Car obj = (Car) anObject;
		return obj.getPrice();
	}
}
