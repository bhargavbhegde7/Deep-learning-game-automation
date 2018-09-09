package com.bhegde.ann;

public class Layer
{

    private int id;
    protected int numOfNeurons;
    private Double biasVal;

    protected Double[] inputs;
    protected Double[] outputs;
    protected Double[] errors;

    protected Double[][] weights;

    public Layer(int id, int layerSize, int previousLayerSize)
    {
        this.id = id;
        this.numOfNeurons = layerSize;
        this.biasVal = 1.0;
        this.inputs = new Double[numOfNeurons];
        initializeDoubleArray(inputs);
        this.outputs = new Double[numOfNeurons + Constants.useBias];
        initializeDoubleArray(outputs);
        this.outputs[0] = this.biasVal;
        this.errors = new Double[numOfNeurons];
        initializeDoubleArray(errors);

        weights = makeMatrix(previousLayerSize+Constants.useBias, this.numOfNeurons, Constants.initMin, Constants.initMax);

    }

    private void initializeDoubleArray(Double[] array)
    {
        for(int i = 0; i<array.length; i++)
        {
            array[i] = 0.0;
        }
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
