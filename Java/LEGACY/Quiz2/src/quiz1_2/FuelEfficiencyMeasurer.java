package quiz1_2;

public class FuelEfficiencyMeasurer implements Measurer{
	
	public double measure(Object anObject) {
		Car obj = (Car) anObject;
		return obj.getFuelEfficiency();
	}
}
