package com.bhegde.annhack;

public class MultiplyGate extends Gate
{
    /**
     * store pointers to input Units u0 and u1 and output unit utop
     * @param unit0
     * @param unit1
     * @return
     */
    @Override
    public Unit forward(Unit unit0, Unit unit1)
    {
        u0 = unit0;
        u1 = unit1;

        utop = new Unit(u0.value * u1.value, 0.0);
        return utop;
    }

    /**
     * take the gradient in output unit and chain it with the
     * local gradients, which we derived for multiply gate before
     * then write those gradients to those Units.
     */
    @Override
    public void backward()
    {
        double u0Gradient = u1.value; // because in multiply case one input's gradient is the other input.
        double u1Gradient = u0.value; // x derivative is y and y derivative is x
        u0.grad += u0Gradient * utop.grad;
        u1.grad += u1Gradient * utop.grad;
    }
}
