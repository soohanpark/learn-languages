package quiz1_2;

public class CarTester2 {

	public static void main(String[] args) {
		Car[] cars = { new Car("KIA", 1000, 13.1),
				   	   new Car("BMW", 5000, 8.7),
				   	   new Car("HYUNDAI", 2000, 21),
				   	   new Car("BENZ", 4000, 3.6)};
		
		PriceMeasurer pm = new PriceMeasurer();
		FuelEfficiencyMeasurer fm = new FuelEfficiencyMeasurer();
		
		Car expensive_car = (Car)Data.max(cars, pm);
		System.out.println("The expensive car is : " + expensive_car.toString());
		
		Car highest_efficiency_car = (Car)Data.max(cars, fm);
		System.out.println("The highest fuel efficiency car is : " + highest_efficiency_car.toString());
	}

}
