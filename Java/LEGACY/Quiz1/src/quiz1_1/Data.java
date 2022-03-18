package quiz1_1;

public class Data {
	public static Measurable min (Measurable[] objects) {
		int ans=0;
		
		for (int i=0; i<objects.length;i++) {
			if (objects[ans].getMeasure() > objects[i].getMeasure()) {
				ans = i;
			}
		}
		
		return objects[ans];
	}
}
