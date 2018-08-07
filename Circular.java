package physics.mechanics.motion.generic;

import physics.mechanics.object.Object;

public class Circular {
	
	private Object object;
	private double radius, velocity, cfAcc;
	private double cfForce, cpForce;
	
	public void initiate(Object o, double r, double v) {
		this.object = o;
		this.radius = r;
		this.velocity = v;
	}
	
	public double calculateCentrifugalAcceleration() {
		cfAcc = Math.pow(velocity,2)/radius;
		return cfAcc;
	}
	
	public double calculateCentrifugalForce() {
		if(cfAcc==0D)
			calculateCentrifugalAcceleration();
		cfForce = object.getMass()*cfAcc;
		return cfForce;
	}
	
	public double calculateCentripetalForce() {
		if(cfForce==0d)
			calculateCentrifugalForce();
		cpForce = -cfForce;
		return cpForce;
	}
	
	public String getDistanceEquation() {
		String s = String.format("s(@) = %.2d*cos(@)+%.2d*sin(@)", radius);
		return s;
	}

}
