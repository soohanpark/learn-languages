package finalexam2;

import java.io.File;
import java.util.Scanner;

public class Findpopulation {

	public static void main(String[] args) {
		File input = new File("data.txt");
		Scanner scan_file;
		Scanner scan;
		
		try {
			scan_file = new Scanner(input);
			scan = new Scanner(System.in);
			String countryName;
		
			System.out.print("인구수를 알고 싶은 나라 이름을 적으시오. >>");
			countryName = scan.nextLine();
			
			while (scan_file.hasNextLine()) {
				if (countryName.equals(scan_file.nextLine())) 
					System.out.println(scan_file.nextLine());
			}
		}
		catch (Exception e) {
			System.out.println("찾는 나라가 없습니다!");
		}
	}

}
