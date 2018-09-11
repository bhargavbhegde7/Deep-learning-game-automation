package com.bhegde.ann;

import java.math.BigDecimal;
import java.math.RoundingMode;

public class MainApp {
    public static void main(String[] args) {
        ANN ann = new ANN(new Integer[]{2, 1});
        Double[][] targets = new Double[4][1];

        //LOGICAL AND
        targets[0][0] = 0.0;
        targets[1][0] = 0.0;
        targets[2][0] = 0.0;
        targets[3][0] = 1.0;

        Double[][] inputs = new Double[4][2];

        //TRUTH TABLE
        inputs[0][0] = 0.0;
        inputs[0][1] = 0.0;

        inputs[1][0] = 0.0;
        inputs[1][1] = 1.0;

        inputs[2][0] = 1.0;
        inputs[2][1] = 0.0;

        inputs[3][0] = 1.0;
        inputs[3][1] = 1.0;

        ann.train(inputs, targets, 100000);

        for(int i = 0; i<targets.length; i++)
        {
            System.out.println(inputs[i][0]+", "+inputs[i][1]+" : "+round(ann.predict(inputs[i])[0], 4));
        }
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = new BigDecimal(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}
