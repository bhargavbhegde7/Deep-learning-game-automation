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
        u0.grad += u1.value * utop.grad;
        u1.grad += u0.value * utop.grad;
    }
}
