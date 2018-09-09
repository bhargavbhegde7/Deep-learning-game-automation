package com.bhegde.ann;

public class Layer
{

    private int id;
    private int numOfNeurons;
    private int biasVal;

    private Integer[] input;
    private Integer[] output;
    private Integer[] error;

    private Double[][] weight;

    public Layer(int id, int layerSize, int previousLayerSize)
    {
        this.id = id;
        this.numOfNeurons = layerSize;
        this.biasVal = 1;
        this.input = new Integer[numOfNeurons];
        this.output = new Integer[numOfNeurons + Constants.useBias];
        this.output[0] = this.biasVal;
        this.error = new Integer[numOfNeurons];

        weight = makeMatrix(previousLayerSize+Constants.useBias, this.numOfNeurons, Constants.initMin, Constants.initMax);
        
    }

    private Double[][] makeMatrix(int N, int M, double initMin, double initMax)
    {
        Double[][] matrix = new Double[N][M];

        for(int i = 0; i<N; i++)
        {
            for(int j = 0; j<M; j++)
            {
                matrix[i][j] = between(initMin, initMax);
            }
        }

        return matrix;
    }

    private double between(double min, double max)
    {
        double rand = Math.random();
        return rand*((max - min) + 1) + min;
    }
}
