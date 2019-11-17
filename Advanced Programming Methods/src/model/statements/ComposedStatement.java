package model.statements;

import model.ProgramState;
import model.collections.stack.IStack;

public class ComposedStatement implements IStatement {
    private IStatement first;
    private IStatement second;

    public ComposedStatement(IStatement first, IStatement second)
    {
        this.first = first;
        this.second = second;
    }

    @Override
    public ProgramState execute(ProgramState state) {
        IStack<IStatement> executionStack = state.getExecutionStack();
        executionStack.push(second);
        executionStack.push(first);
        return state;
    }

    @Override
    public String toString()
    {
        return "("+first.toString() + ";" + second.toString()+")";
    }
}
