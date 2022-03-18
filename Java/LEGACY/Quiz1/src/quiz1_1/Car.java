package quiz1_1;

public class Car implements Measurable, Comparable<Object>{
	private String model;
	private double price; //만원 단위
	
	public Car(String model, double price){
		this.model = model;
		this.price = price;
	}
	
	public int compareTo(Object otherObject) {
		Car other = (Car) otherObject;
		if (this.price > other.price)
			return 1;
		else if (this.price < other.price)
			return -1;
		else
			return 0;
	}
	
	public double getMeasure() {
		return this.price;
	}
	
	public String toString() {
		return "model : " + this.model +"   price : " + this.price ;
	}
}
