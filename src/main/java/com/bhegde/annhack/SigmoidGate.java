package com.bhegde.annhack;

public class SigmoidGate extends Gate
{
    @Override
    public Unit forward(Unit unit0, Unit unit1)
    {
        this.u0 = unit0;

        this.utop = new Unit(sigmoid(u0.value), 0.0);
        return this.utop;
    }

    @Override
    void backward()
    {
        double s = sigmoid(u0.value);
        u0.grad += (s * (1 - s)) * utop.grad;
    }

    /**
     * Sigmoid function
     * @param x
     * @return
     */
    private double sigmoid(double x)
    {
        return (1/( 1 + Math.pow(Math.E,(-1*x))));
    }
}
