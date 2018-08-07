package physics.mechanics.motion.generic;

import physics.mechanics.object.Object;

public class Projectile {
	
	private Object object;
	private double iVelocity, iVX, iVY;
	private double range, height,time;
	private double angle;
	
	private static final double g = 9.86; //in m/s2
	
	public void initiate(Object o, double v1, double a) {
		this.object = o;
		this.angle = a;
		this.iVelocity = v1;
		iVX = iVelocity*Math.cos(angle);
		iVY = iVelocity*Math.sin(angle);
	}
	
	public double calculateTime() {
		time = iVY/g;
		return time;
	}
	
	public double calculateRange() {
		if(range==0d)
			calculateTime();
		range = iVX*time;
		return range;
	}
	
	public double calculateHeight() {
		if(height==0d)
			height = Math.pow(iVY,2)/(2*g);
		return height;
	}
	
	public String getVelocityYTimeEquation() {
		String s = String.format("Vy(t) = %.2d*t - %.2d*t^2", iVY,g/2);
		return s;
	}
	
	public String getVelocityYHeightEquation() {
		String s = String.format("Vy^2(t) = %.2d^2 - 2*%.2d*h", iVY,g/2);
		return s;
	}

}
