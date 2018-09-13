package com.bhegde.annhack;

public abstract class Gate {

    public Unit u0, u1, utop;

    abstract Unit forward(Unit unit0, Unit unit1);

    abstract void backward();
}
