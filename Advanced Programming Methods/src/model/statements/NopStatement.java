package model.statements;

import model.ProgramState;

public class NopStatement implements IStatement {
    @Override
    public ProgramState execute(ProgramState state)
    {
        return state;
    }

    @Override
    public String toString()
    {
        return "NopStatement{}";
    }
}
