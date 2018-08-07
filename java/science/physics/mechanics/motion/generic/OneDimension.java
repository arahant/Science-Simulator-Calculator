package physics.mechanics.motion.generic;

import physics.mechanics.object.Object;

public class OneDimension {
	
	private Object object;
	private double distance, acc, iVelocity;
	private double force;
	
	public void initiate(Object o, double u) {
		this.object = o;
		this.iVelocity = u;
	}
	
	public double calculateAcceleration(double v2, double t) {
		acc = (v2-iVelocity)/t;
		return acc;
	}
	
	public double calculateDistance(double v2, float t) {
		if(acc==0d)
			calculateAcceleration(v2, t);
		distance = iVelocity*t + (double)1/2*acc*t*t;
		return distance;
	}
	
	public double calculateForce(double v2, double t) {
		if(acc==0d)
			calculateAcceleration(v2, t);
		force = object.getMass()*acc;
		return force;
	}
	
	public String getAccelerationEquation() {
		String s = String.format("a(t) = (v - %.2d)/t", iVelocity);
		return s;
	}
	
	public String getDistanceEquation() {
		String s = String.format("s(t) = %.2d*t + %.2d*t^2", iVelocity,acc/2);
		return s;
	}

}
