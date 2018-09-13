package com.bhegde.annhack;

public class AddGate extends Gate
{
    @Override
    public Unit forward(Unit unit0, Unit unit1)
    {
        u0 = unit0;
        u1 = unit1;// store pointers to input units

        utop = new Unit(u0.value + u1.value, 0.0);
        return utop;
    }

    /**
     * add gate. derivative wrt both inputs is 1
     */
    @Override
    public void backward()
    {
        u0.grad += 1 * utop.grad;
        u1.grad += 1 * utop.grad;
    }
}
