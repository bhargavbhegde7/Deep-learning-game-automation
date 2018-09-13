package com.bhegde.annhack;

// every Unit corresponds to a wire in the diagrams
public class Unit
{

    public double
    // value computed in the forward pass
    value,
    // the derivative of circuit output w.r.t this unit, computed in backward pass
    grad;

    public Unit(double value, double grad)
    {
        this.value = value;
        this.grad = grad;
    }
}
