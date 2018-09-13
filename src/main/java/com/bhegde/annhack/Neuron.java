package com.bhegde.annhack;

public class Neuron
{
    Unit a = new Unit(1.0, 0.0);
    Unit b = new Unit(2.0, 0.0);
    Unit c = new Unit(-3.0, 0.0);
    Unit x = new Unit(-1.0, 0.0);
    Unit y = new Unit(3.0, 0.0);

    Gate mulg0 = new MultiplyGate();
    Gate mulg1 = new MultiplyGate();

    Gate addg0 = new AddGate();
    Gate addg1 = new AddGate();

    Gate sig0 = new SigmoidGate();

    Unit s;

    public void forwardNeuron()
    {
        Unit ax = mulg0.forward(a, x);
        Unit by = mulg1.forward(b, y);

        Unit axpby = addg0.forward(ax, by);
        Unit axpbypc = addg1.forward(axpby, c);

        s = sig0.forward(axpbypc, null);
    }
}
