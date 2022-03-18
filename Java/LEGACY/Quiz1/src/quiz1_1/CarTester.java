package quiz1_1;

import java.util.Arrays;

public class CarTester {

	public static void main(String[] args) {
		Car[] cars = { new Car("KIA", 1000),
					   new Car("BMW", 5000),
					   new Car("HYUNDAI", 2000),
					   new Car("BENZ", 4000)};
		
		
		Measurable lowest_car = Data.min(cars);
		System.out.println("The lowest car is : " + lowest_car.toString());
		
		Arrays.sort(cars);
		for (int i=0;i<cars.length;i++)
			System.out.println(cars[i].toString());
	}

}
