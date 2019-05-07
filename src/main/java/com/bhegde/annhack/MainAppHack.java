package com.bhegde.annhack;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * from the blog post
 * http://karpathy.github.io/neuralnets/
 */
public class MainAppHack
{
    public static void main(String[] args)
    {
        Neuron neuron = new Neuron();
        neuron.forwardNeuron();
        System.out.println("iteration : 0 : "+round(neuron.s.value, 4));

        for(int i = 0; i<1000; i++)
        {
            neuron.s.grad = 1.0;
            neuron.sig0.backward(); // writes gradient into axpbypc
            neuron.addg1.backward(); // writes gradients into axpby and c
            neuron.addg0.backward(); // writes gradients into ax and by
            neuron.mulg1.backward(); // writes gradients into b and y
            neuron.mulg0.backward(); // writes gradients into a and x

            double step_size = 0.01;
            neuron.a.value += step_size * neuron.a.grad; // a.grad is -0.105
            neuron.b.value += step_size * neuron.b.grad; // b.grad is 0.315
            neuron.c.value += step_size * neuron.c.grad; // c.grad is 0.105
            neuron.x.value += step_size * neuron.x.grad; // x.grad is 0.105
            neuron.y.value += step_size * neuron.y.grad; // y.grad is 0.210

            neuron.forwardNeuron();

            int index = i+1;
            System.out.println("iteration : "+index+" : "+round(neuron.s.value, 4));
        }
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = new BigDecimal(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}
