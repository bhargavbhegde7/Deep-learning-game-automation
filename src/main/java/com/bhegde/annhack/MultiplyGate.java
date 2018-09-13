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
        this.u0 = unit0;
        this.u1 = unit1;

        this.utop = new Unit(u0.value * u1.value, 0.0);
        return this.utop;
    }

    /**
     * take the gradient in output unit and chain it with the
     * local gradients, which we derived for multiply gate before
     * then write those gradients to those Units.
     */
    @Override
    public void backward()
    {
        this.u0.grad += this.u1.value * this.utop.grad;
        this.u1.grad += this.u0.value * this.utop.grad;
    }
}
