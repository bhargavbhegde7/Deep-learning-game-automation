package com.ann.domains.Neuron;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by IntelliJ IDEA.
 * User: bhegde
 * Date: 29/3/16
 * Time: 2:24 PM
 * To change this template use File | Settings | File Templates.
 */
public class InputLayer extends Layer {

    public void initLayer(InputLayer inputLayer){
        ArrayList<Neuron> neurons = new ArrayList<Neuron>();
        int neuronCount = 10;
        for(int i=0;i<neuronCount;i++){
            Neuron neuron = new Neuron();
            neuron.initNeuron();
            neurons.add(neuron);
        }
        inputLayer.setListOfNeurons(neurons);
        inputLayer.setNumberOfNeuronsInLayer(neuronCount);
    }

    public void printLayer(InputLayer inputLayer){
        for(Neuron neuron : inputLayer.getListOfNeurons()){
            for(double inputWeight:neuron.getListOfWeightIn()){
                System.out.println(inputWeight);
            }
        }
    }
}
