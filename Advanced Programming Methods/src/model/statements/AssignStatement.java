package model.statements;

import model.ProgramState;
import model.exceptions.SomeException;
import model.expressions.IExpression;
import model.values.IValue;

public class AssignStatement implements IStatement {
    private String id;
    private IExpression expression;

    public AssignStatement(String id, IExpression expression)
    {
        this.id = id;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state)
    {
        if (state.getSymTable().exists(id))
        {
            IValue value = expression.eval(state.getSymTable());
            if (value.getType().equals(state.getSymTable().lookup(id).getType()))
            {
                state.getSymTable().put(id, value);
            }
            else
            {
                throw new SomeException("Type of expression and type of variable do not match");
            }
        }
        else
        {
            throw new SomeException(String.format("Variable %s is not declared", id));
        }
        return state;
    }

    @Override
    public String toString()
    {
        return "AssignStatement{" +
                "expression=" + expression +
                '}';
    }
}
