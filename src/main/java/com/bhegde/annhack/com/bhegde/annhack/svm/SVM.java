package com.bhegde.annhack.com.bhegde.annhack.svm;

import com.bhegde.annhack.Unit;

public class SVM
{
    Circuit_axpbypc circuit = new Circuit_axpbypc();

    Unit a = new Unit(1.0, 0.0);
    Unit b = new Unit(-2.0, 0.0);
    Unit c = new Unit(-1.0, 0.0);

    Unit unitOut = null;

    public Unit forward(Unit x, Unit y)
    {
        unitOut = circuit.forward(x, y, a, b, c);
        return unitOut;
    }

    public void backward(int label)
    {
        a.grad = 0.0;
        b.grad = 0.0;
        c.grad = 0.0;

        double pull = 0.0;
        if(label == 1 && unitOut.value < 1)
        {
            pull = 1;
        }
        if(label == -1 && unitOut.value > -1)
        {
            pull = -1;
        }

        circuit.backward(pull);

        a.grad += -a.value;
        b.grad += -b.value;

    }

    public void learnFrom(Unit x, Unit y, int label)
    {
        forward(x, y);
        backward(label);
        parameterUpdate();
    }

    public void parameterUpdate()
    {
        double stepSize = 0.009;
        a.value += stepSize * a.grad;
        b.value += stepSize * b.grad;
        c.value += stepSize * c.grad;
    }
}
