package model.statements;

import model.ProgramState;
import model.exceptions.SomeException;
import model.expressions.IExpression;
import model.types.ValueType;
import model.values.BoolValue;
import model.values.IValue;

public class IfStatement implements IStatement {
    private IExpression expression;
    private IStatement thenS;
    private IStatement elseS;

    public IfStatement(IExpression expression, IStatement thenS, IStatement elseS)
    {
        this.expression = expression;
        this.thenS = thenS;
        this.elseS = elseS;
    }

    @Override
    public ProgramState execute(ProgramState state) throws SomeException
    {
        IValue eval = expression.eval(state.getSymTable());
        if (eval.getType() == ValueType.BoolType)
        {
            BoolValue val = (BoolValue)eval;
            if (val.getValue())
            {
                return thenS.execute(state);
            }
            else
                return elseS.execute(state);
        }
        else
            throw new SomeException("If expression does not evaluate to boolean");
    }

    @Override
    public String toString()
    {
        return "IfStatement{" +
                "expression=" + expression +
                ", thenS=" + thenS +
                ", elseS=" + elseS +
                '}';
    }
}
