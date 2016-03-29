package com.ann.domains;

import java.util.ArrayList;

/**
 * Created by IntelliJ IDEA.
 * User: bhegde
 * Date: 29/3/16
 * Time: 2:22 PM
 * To change this template use File | Settings | File Templates.
 */
public abstract class Layer {

    private ArrayList<Neuron> listOfNeurons;
    private int numberOfNeuronsInLayer;

    public ArrayList<Neuron> getListOfNeurons() {
        return listOfNeurons;
    }

    public void setListOfNeurons(ArrayList<Neuron> listOfNeurons) {
        this.listOfNeurons = listOfNeurons;
    }

    public int getNumberOfNeuronsInLayer() {
        return numberOfNeuronsInLayer;
    }

    public void setNumberOfNeuronsInLayer(int numberOfNeuronsInLayer) {
        this.numberOfNeuronsInLayer = numberOfNeuronsInLayer;
    }
}
