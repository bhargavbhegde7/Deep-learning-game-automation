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
        System.out.println(round(neuron.s.value, 4));
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = new BigDecimal(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}
