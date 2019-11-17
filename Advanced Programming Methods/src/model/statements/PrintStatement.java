package model.statements;

import model.ProgramState;
import model.expressions.IExpression;

public class PrintStatement implements IStatement {
    private IExpression expression;

    public PrintStatement(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) {
        state.getOut().enqueue(expression.eval(state.getSymTable()));
        return state;
    }

    @Override
    public String toString()
    {
        return "PrintStatement{" +
                "expression=" + expression +
                '}';
    }
}
