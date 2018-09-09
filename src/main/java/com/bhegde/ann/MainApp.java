package com.bhegde.ann;

public class MainApp {
    public static void main(String[] args) {
        ANN ann = new ANN(new Integer[]{2,1});
        Double[][] targets = new Double[4][1];

        targets[0][0] = 0.0;
        targets[1][0] = 1.0;
        targets[2][0] = 1.0;
        targets[3][0] = 1.0;

        Double[][] inputs = new Double[4][2];

        inputs[0][0] = 0.0;
        inputs[0][1] = 0.0;

        inputs[1][0] = 0.0;
        inputs[1][1] = 1.0;

        inputs[2][0] = 1.0;
        inputs[2][1] = 0.0;

        inputs[3][0] = 1.0;
        inputs[3][1] = 1.0;

        //ann.train(inputs, targets, 30000);

        for(int i = 0; i<targets.length; i++)
        {
            System.out.println(inputs[i][0]+", "+inputs[i][1]+" : "+ann.predict(inputs[i])[0]);
        }
    }
}
