package com.bhegde.annhack.com.bhegde.annhack.ann;

import com.bhegde.annhack.Unit;

import java.util.Random;

public class AnnReLU
{
    double[][] data = {{1.2, 0.7},
            {-0.3, -0.5},
            {3.0, 0.1},
            {-0.1, -1.0},
            {-1.0, 1.1},
            {2.1, -3.0}};

    int[] labels = {1,-1,1,-1,-1,1};

    Unit a1;
    Unit a2;
    Unit a3;
    Unit a4;

    Unit b1;
    Unit b2;
    Unit b3;
    Unit b4;

    Unit c1;
    Unit c2;
    Unit c3;
    Unit c4;

    Unit d4;

    public AnnReLU()
    {
        a1 = new Unit(between(-0.5, 0.5), 0.0);
        a2 = new Unit(between(-0.5, 0.5), 0.0);
        a3 = new Unit(between(-0.5, 0.5), 0.0);
        a4 = new Unit(between(-0.5, 0.5), 0.0);

        b1 = new Unit(between(-0.5, 0.5), 0.0);
        b2 = new Unit(between(-0.5, 0.5), 0.0);
        b3 = new Unit(between(-0.5, 0.5), 0.0);
        b4 = new Unit(between(-0.5, 0.5), 0.0);

        c1 = new Unit(between(-0.5, 0.5), 0.0);
        c2 = new Unit(between(-0.5, 0.5), 0.0);
        c3 = new Unit(between(-0.5, 0.5), 0.0);
        c4 = new Unit(between(-0.5, 0.5), 0.0);

        d4 = new Unit(between(-0.5, 0.5), 0.0);
    }

    private double between(double min, double max)
    {
        double rand = Math.random();
        return rand*((max - min) + 1) + min;
    }

    public void train()
    {
        for(int iter = 0; iter < 100000; iter++)
        {
            int i = randomNumberInRange(0, data.length - 1);

            double x = data[i][0];
            double y = data[i][1];
            int label = labels[i];

            double n1 = Math.max(0, a1.value*x + b1.value*y + c1.value);
            double n2 = Math.max(0, a2.value*x + b2.value*y + c2.value);
            double n3 = Math.max(0, a3.value*x + b3.value*y + c3.value);
            double score = a4.value*n1 + b4.value*n2 + c4.value*n3 + d4.value;

            double pull = 0;

            if(label == 1 && score < 1) pull = 1;
            if(label == -1 && score > -1) pull = -1;

            double dscore = pull;
            a4.grad     = n1        * dscore;
            double dn1  = a4.value  * dscore;
            b4.grad     = n2        * dscore;
            double dn2  = b4.value  * dscore;
            c4.grad     = n3        * dscore;
            double dn3  = c4.value  * dscore;
            d4.grad     = 1.0       * dscore;

            dn3 = n3 == 0 ? 0 : dn3;
            dn2 = n2 == 0 ? 0 : dn2;
            dn1 = n1 == 0 ? 0 : dn1;

            a1.grad = x * dn1;
            b1.grad = y * dn1;
            c1.grad = 1.0 * dn1;

            a2.grad = x * dn2;
            b2.grad = y * dn2;
            c2.grad = 1.0 * dn2;

            a3.grad = x * dn3;
            b3.grad = y * dn3;
            c3.grad = 1.0 * dn3;

            a1.grad += -a1.value; a2.grad += -a2.value; a3.grad += -a3.value;
            b1.grad += -b1.value; b2.grad += -b2.value; b3.grad += -b3.value;
            a4.grad += -a4.value; b4.grad += -b4.value; c4.grad += -c4.value;

            double stepSize = 0.01;
            a1.value += stepSize * a1.grad;
            b1.value += stepSize * b1.grad;
            c1.value += stepSize * c1.grad;
            a2.value += stepSize * a2.grad;
            b2.value += stepSize * b2.grad;
            c2.value += stepSize * c2.grad;
            a3.value += stepSize * a3.grad;
            b3.value += stepSize * b3.grad;
            c3.value += stepSize * c3.grad;
            a4.value += stepSize * a4.grad;
            b4.value += stepSize * b4.grad;
            c4.value += stepSize * c4.grad;
            d4.value += stepSize * d4.grad;
        }
    }

    public void test()
    {
        for(int i =0; i<6; i++)
        {
            double x = data[i][0];
            double y = data[i][1];

            double n1 = Math.max(0, a1.value*x + b1.value*y + c1.value);
            double n2 = Math.max(0, a2.value*x + b2.value*y + c2.value);
            double n3 = Math.max(0, a3.value*x + b3.value*y + c3.value);
            int testScore = a4.value*n1 + b4.value*n2 + c4.value*n3 + d4.value > 0 ? 1 : -1;;

            System.out.println(testScore);
        }
    }

    public static int randomNumberInRange(int min, int max)
    {
        Random random = new Random();
        return random.nextInt((max - min) + 1) + min;
    }

    public static void main(String[] args) {
        AnnReLU ann = new AnnReLU();
        ann.train();
        ann.test();
    }
}
