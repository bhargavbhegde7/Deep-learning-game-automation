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

    Unit ax;
    Unit by;
    Unit axpby;
    Unit axpbypc;
    Unit s;

    public void forwardNeuron()
    {
        ax = mulg0.forward(a, x); // a*x = -1
        by = mulg1.forward(b, y); // b*y = 6

        axpby = addg0.forward(ax, by); // a*x + b*y = 5
        axpbypc = addg1.forward(axpby, c); // a*x + b*y + c = 2

        s = sig0.forward(axpbypc, null); // sig(a*x + b*y + c) = 0.8808
    }
}
