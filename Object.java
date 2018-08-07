package physics.mechanics.object;

public final class Object {
	
	private static final double g = 9.86; //in m/s2
	
	private double mass; //in grams
	private double volume; //in ml(cc)
	private double density; //in g/cc
	private double weight; //in N
	
	public Object(double m, double v) {
		mass = m;
		volume = v;
		density = mass/volume;
		weight = mass*g/1000;
	}
	
	public double getMass() {
		return mass;
	}
	
	public double getVolume() {
		return volume;
	}
	
	public double getDensity() {
		return density;
	}
	
	public double getWeight() {
		return weight;
	}

}
