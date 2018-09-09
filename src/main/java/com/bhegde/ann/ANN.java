package com.bhegde.ann;

public class ANN
{
    private Layer[] layers;
    private double learnRate = 0.1;

    public ANN(Integer[] layerSizes)
    {
        layers = new Layer[layerSizes.length];

        for(int i = 0; i < layerSizes.length; i++)
        {
            int previousLayerSize = i == 0 ? 0 : layerSizes[i - 1];
            Layer layer = new Layer(i, layerSizes[i], previousLayerSize);
            layers[i] = (layer);
        }
    }

    public void train(Double[][] inputs, Double[][] targets, int numOfEpochs)
    {
        for (int epoch = 0; epoch < numOfEpochs; epoch++)
        {
            for(int i = 0; i<inputs.length; i++)
            {
                setInput(inputs[i]);
                forwardPropagate();
                updateErrorOutput(targets[i]);
                backwardPropogate();
                updateWeights();
            }
        }
    }

    public Double[] predict(Double[] inputVector)
    {
        setInput(inputVector);
        forwardPropagate();
        Double[] outputVector = getOutput();
        return outputVector;
    }

    private void updateWeights()
    {
        for(int layerIndex = 1; layerIndex<layers.length; layerIndex++)
        {
            for(int j = 0; j<layers[layerIndex].numOfNeurons; j++)
            {
                for(int i = 0; i<layers[layerIndex-1].numOfNeurons+Constants.useBias; i++)
                {
                    double output = layers[layerIndex-1].outputs[i];
                    double error = layers[layerIndex].errors[j];
                    layers[layerIndex].weights[i][j] += learnRate*output*error;
                }
            }
        }
    }

    private void forwardPropagate()
    {
        for(int layerIndex = 0; layerIndex<(layers.length-1); layerIndex++)
        {
            Layer srcLayer = layers[layerIndex];
            Layer dstLayer = layers[layerIndex+1];

            for(int j = 0; j<dstLayer.numOfNeurons; j++)
            {
                double inputSum = 0;
                for(int i = 0; i<(srcLayer.numOfNeurons+Constants.useBias); i++)
                {
                    inputSum += dstLayer.weights[i][j] * srcLayer.outputs[i];
                }

                dstLayer.inputs[j] = inputSum;
                dstLayer.outputs[j + Constants.useBias] = squash(inputSum);
            }
        }
    }

    private double squash(double x)
    {
        return sigmoid(x);
    }

    /**
     * Sigmoid function
     * @param x
     * @return
     */
    private double sigmoid(double x)
    {
        return (1/( 1 + Math.pow(Math.E,(-1*x))));
    }

    private Double[] getOutput()
    {
        Layer outputLayer = layers[layers.length-1];
        Double[] result = new Double[outputLayer.numOfNeurons];
        for(int i = 0; i<outputLayer.numOfNeurons; i++)
        {
            result[i] = outputLayer.outputs[i + Constants.useBias];
        }

        return result;
    }

    private void setInput(Double[] inputVector)
    {
        Layer inputLayer = layers[0];

        for(int i = 0; i<inputLayer.numOfNeurons; i++)
        {
            inputLayer.outputs[i + Constants.useBias] = inputVector[i];
        }
    }

    private void updateErrorOutput(Double[] targetVector)
    {
        Layer outputLayer = layers[layers.length-1];
        for(int i = 0; i<outputLayer.numOfNeurons; i++)
        {
            double output = outputLayer.outputs[i + Constants.useBias];
            double error = targetVector[i] = output;
            outputLayer.errors[i] = derivSquash(outputLayer.inputs[i]) * error;
        }
    }

    private double derivSquash(double x)
    {
        double sigmoid = sigmoid(x);
        return (1-sigmoid)*sigmoid;
    }

    private void backwardPropogate()
    {
        for(int layerIndex = layers.length-1; layerIndex>0; layerIndex--)
        {
            Layer srcLayer = layers[layerIndex];
            Layer dstLayer = layers[layerIndex-1];

            for(int dstLayerIndex = 0; dstLayerIndex<dstLayer.numOfNeurons; dstLayerIndex++)
            {
                double error = 0;
                for(int srcLayerIndex = 0; srcLayerIndex<srcLayer.numOfNeurons; srcLayerIndex++)
                {
                    error += srcLayer.weights[dstLayerIndex+Constants.useBias][srcLayerIndex]*srcLayer.errors[srcLayerIndex];
                }
                dstLayer.errors[dstLayerIndex] = derivSquash(dstLayer.inputs[dstLayerIndex]) * error;
            }
        }
    }
}























