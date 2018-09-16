package com.bhegde.annhack.com.bhegde.annhack.svm;

import com.bhegde.annhack.Unit;

import java.util.Random;

public class StochasticGradientDescent
{
    double[][] data = {{1.2, 0.7},
                       {-0.3, -0.5},
                       {3.0, 0.1},
                       {-0.1, -1.0},
                       {-1.0, 1.1},
                       {2.1, -3.0}};

    int[] labels = {1,-1,1,-1,-1,1};

    SVM svm = new SVM();

    public double evalTrainingAccuracy()
    {
        Unit x = null, y = null;
        int trueLabel = 0;

        double numCorrect = 0;
        for(int i = 0; i < data.length; i++)
        {
            x = new Unit(data[i][0], 0.0);
            y = new Unit(data[i][1], 0.0);

            trueLabel = labels[i];


            int predictedLabel = svm.forward(x, y).value > 0 ? 1 : -1;

            if (predictedLabel == trueLabel)
            {
                numCorrect++;
            }
        }
        return numCorrect/data.length;
    }

    public void learn()
    {
        for(int iter = 0; iter < 5000; iter++)
        {
            int i = randomNumberInRange(0, data.length-1);
            //int i = iter%data.length;

            Unit x = new Unit(data[i][0], 0.0);
            Unit y = new Unit(data[i][1], 0.0);

            int label = labels[i];

            svm.learnFrom(x, y, label);

            if(iter%25 == 0)
            {
                double accuracy = evalTrainingAccuracy();
                System.out.println("training accuracy at iter "+iter + " : "+accuracy);
                /*if(accuracy == 1.0)
                {
                    break;
                }*/
            }
        }
    }

    public static int randomNumberInRange(int min, int max)
    {
        Random random = new Random();
        return random.nextInt((max - min) + 1) + min;
    }

    public void test()
    {
        Unit x = new Unit(-3.0, 0.0);
        Unit y = new Unit(3.0, 0.0);

        int predictedLabel = svm.forward(x, y).value> 0 ? 1 : -1;

        System.out.println(predictedLabel);
    }

    public static void main(String[] args)
    {
        StochasticGradientDescent s = new StochasticGradientDescent();
        s.learn();

        //s.test();

        System.out.printf("");
    }
}
