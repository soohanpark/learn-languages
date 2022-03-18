package quiz1_2;

public class Data {
	public static Object max (Object[] objects, Measurer meas) {
		int ans=0;
		
		for (int i=0; i<objects.length;i++) {
			if (meas.measure(objects[i]) > meas.measure(objects[ans])) {
				ans = i;
			}
		}
		
		return objects[ans];
	}
}
