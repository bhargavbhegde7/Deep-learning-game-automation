package com.bhegde.annhack.com.bhegde.annhack.svm;

import com.bhegde.annhack.AddGate;
import com.bhegde.annhack.Gate;
import com.bhegde.annhack.MultiplyGate;
import com.bhegde.annhack.Unit;

public class Circuit_axpbypc
{
    Gate mulg0 = new MultiplyGate();
    Gate mulg1 = new MultiplyGate();

    Gate addg0 = new AddGate();
    Gate addg1 = new AddGate();

    Unit ax;
    Unit by;
    Unit axpby;
    Unit axpbypc;

    public Unit forward(Unit x, Unit y, Unit a, Unit b, Unit c)
    {
        ax = mulg0.forward(a, x);
        by = mulg1.forward(b, y);

        axpby = addg0.forward(ax, by);
        axpbypc = addg1.forward(axpby, c);

        return axpbypc;
    }

    public void backward(double gradientFromTop)
    {
        axpbypc.grad = gradientFromTop;

        addg1.backward();
        addg0.backward();

        mulg1.backward();
        mulg0.backward();
    }
}
