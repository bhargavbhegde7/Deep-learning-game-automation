package com.bhegde.annhack;

public class AddGate extends Gate
{
    @Override
    public Unit forward(Unit unit0, Unit unit1)
    {
        this.u0 = unit0;
        this.u1 = unit1;

        this.utop = new Unit(u0.value + u1.value, 0.0);
        return this.utop;
    }

    @Override
    public void backward()
    {
        this.u0.grad += 1 + this.utop.grad;
        this.u1.grad += 1 + this.utop.grad;
    }
}
