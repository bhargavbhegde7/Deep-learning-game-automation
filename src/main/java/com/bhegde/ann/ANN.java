package com.bhegde.ann;

import java.util.ArrayList;
import java.util.List;

public class ANN
{

    private List<Layer> layers;

    public ANN(List<Integer> layerSizes)
    {
        layers = new ArrayList<Layer>();

        for(int i = 0; i < layerSizes.size(); i++)
        {
            int previousLayerSize = i == 0 ? 0 : layerSizes.get(i - 1);
            Layer layer = new Layer(i, layerSizes.get(i), previousLayerSize);
            this.layers.add(layer);
        }
    }
}
