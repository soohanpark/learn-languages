//14010855
//นฺผ๖วั

public class Sequence {
	private int[] values;
	public Sequence (int size) {values=new int[size];}
	public void set(int i, int n) {values[i]=n;}
	
	public int get(int i) {
		return this.values[i];
	}
	
	public int size() {
		return values.length;
	}
	
	public Sequence reverse() {
		Sequence temp =new Sequence(this.values.length);
		
		for (int i=0; i<this.values.length;i++) {
			temp.values[i]=this.values[this.values.length-1-i];
		}
		
		return temp;
	}
	
	public boolean sameValues(Sequence other)
}
