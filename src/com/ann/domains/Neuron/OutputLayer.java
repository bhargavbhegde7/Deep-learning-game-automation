package com.ann.domains.Neuron;

import java.util.ArrayList;

/**
 * Created by IntelliJ IDEA.
 * User: bhegde
 * Date: 29/3/16
 * Time: 2:32 PM
 * To change this template use File | Settings | File Templates.
 */
public class OutputLayer extends Layer {
    public void initLayer(OutputLayer outputLayer){
        ArrayList<Neuron> neurons = new ArrayList<Neuron>();
        int neuronCount = 10;
        for(int i=0;i<neuronCount;i++){
            Neuron neuron = new Neuron();
            neuron.initNeuron();
            neurons.add(neuron);
        }
        outputLayer.setListOfNeurons(neurons);
        outputLayer.setNumberOfNeuronsInLayer(neuronCount);
    }

    public void printLayer(OutputLayer outputLayer){
        for(Neuron neuron : outputLayer.getListOfNeurons()){
            for(double outputWeight:neuron.getListOfWeightOut()){
                System.out.println(outputWeight);
            }
        }
    }
}
