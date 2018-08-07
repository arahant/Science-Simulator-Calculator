package physics.mechanics.motion.harmonic;

import physics.mechanics.object.Object;

public class Pendulum {
	
	private Object object;
	private double velocity;
	private double radius, time;
	private double iAngle;
	private double KE, PE;
	
	private static final double g = 9.86; //in m/s2
	
	public void initiate(Object o, double a, double r) {
		this.object = o;
		this.radius = r;
		this.iAngle = a;
	}
	
	public double calculateOscillationTime() {
		time = 2*Math.sqrt(radius*(1-Math.cos(iAngle))/g);
		return time;
	}
	
	public double calculatePotentialEnergy(double a) {
		PE = object.getMass()*g*radius*(1-Math.cos(a));
		return PE;
	}
	
	public double calculateKineticEnergy(double a) {
		KE = calculatePotentialEnergy(iAngle) - calculatePotentialEnergy(a);
		return KE;
	}
	
	public double calculateVelocity(double a) {
		velocity = Math.sqrt(2*g*radius*(1-Math.cos(a)));
		return velocity;
	}
	
	public String getPEEquation() {
		String s = String.format("PE = %.2d*(1-cos(@))", object.getMass()*g*radius);
		return s;
	}

}
