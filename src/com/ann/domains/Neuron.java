package com.ann.domains;

import java.util.ArrayList;
import java.util.Random;

/**
 * Created by IntelliJ IDEA.
 * User: bhegde
 * Date: 29/3/16
 * Time: 2:13 PM
 * To change this template use File | Settings | File Templates.
 */
public class Neuron {

    private ArrayList<Double> listOfWeightIn;
    private ArrayList<Double> listOfWeightOut;

    Random randomGenerator = new Random();
    public double initNeuron(){

        double pseudoRandom = randomGenerator.nextDouble();
        listOfWeightIn = new ArrayList<Double>();
        listOfWeightIn.add(pseudoRandom);
        listOfWeightOut = new ArrayList<Double>();
        listOfWeightIn.add(pseudoRandom);

        return pseudoRandom;
    }

    public ArrayList<Double> getListOfWeightOut() {
        return listOfWeightOut;
    }

    public void setListOfWeightOut(ArrayList<Double> listOfWeightOut) {
        this.listOfWeightOut = listOfWeightOut;
    }

    public ArrayList<Double> getListOfWeightIn() {
        return listOfWeightIn;
    }

    public void setListOfWeightIn(ArrayList<Double> listOfWeightIn) {
        this.listOfWeightIn = listOfWeightIn;
    }
}
