package quiz1_2;

public class Car {
	private String model;
	private double price;
	private double fuelEfficiency;
	
	public Car(String model, double price,double fuelEfficiency) {
		this.model = model;
		this.price = price;
		this.fuelEfficiency = fuelEfficiency;
	}

	public double getFuelEfficiency() {
		return fuelEfficiency;
	}

	public double getPrice() {
		return price;
	}
	
	public String toString() {
		return "model : " + this.model +"   price : " + this.price + "   F/E : " + this.fuelEfficiency ;
	}
}
