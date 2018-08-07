package physics.mechanics.motion.generic;

import physics.mechanics.object.Object;

public class TwoDimension {

	private Object object;
	private double distanceX, accX, distanceY, accY;
	private double forceX, forceY;

	public void initiate(Object o) {
		this.object = o;
	}

	//X dimension
	public double calculateAccelerationX(double v1X, double v2X, double t) {
		accX = (v2X-v1X)/t;
		return accX;
	}

	public double calculateDistanceX(double v1X, double v2X, float t) {
		if(accX==0d)
			calculateAccelerationX(v1X, v2X, t);
		distanceX = v1X*t + (double)1/2*accX*t*t;
		return distanceX;
	}

	public double calculateForceX(double v1X, double v2X, double t) {
		if(accX==0d)
			calculateAccelerationX(v1X, v2X, t);
		forceX = object.getMass()*accX;
		return forceX;
	}

	//Y dimension
	public double calculateAccelerationY(double v1Y, double v2Y, double t) {
		accY = (v2Y-v1Y)/t;
		return accY;
	}

	public double calculateDistanceY(double v1Y, double v2Y, float t) {
		if(accY==0d)
			calculateAccelerationY(v1Y, v2Y, t);
		distanceY = v1Y*t + (double)1/2*accY*t*t;
		return distanceY;
	}

	public double calculateForceY(double v1Y, double v2Y, double t) {
		if(accY==0d)
			calculateAccelerationY(v1Y, v2Y, t);
		forceY = object.getMass()*accY;
		return forceY;
	}

	//final
	public double calculateAcceleration() {
		return Math.sqrt(Math.pow(accX,2)+Math.pow(accY,2));
	}
	
	public double calculateDistance() {
		return Math.sqrt(Math.pow(distanceX,2)+Math.pow(distanceY,2));
	}
	
	public double calculateForce() {
		return Math.sqrt(Math.pow(forceX,2)+Math.pow(forceY, 2));
	}

}