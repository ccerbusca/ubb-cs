package model.statements;

import model.ProgramState;
import model.exceptions.SomeException;
import model.expressions.IExpression;
import model.types.ValueType;
import model.values.IValue;
import model.values.StringValue;

import java.io.IOException;

public class CloseReadFileStatement implements IStatement
{
    private IExpression expression;

    public CloseReadFileStatement(IExpression expression)
    {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state)
    {
        IValue value = expression.eval(state.getSymTable());
        if (value.getType().equals(ValueType.StringType))
        {
            StringValue stringValue = (StringValue) value;
            if (state.getFileTable().exists(stringValue))
            {
                try
                {
                    state.getFileTable().lookup(stringValue).close();
                    state.getFileTable().delete(stringValue);
                    return state;
                }
                catch (IOException e)
                {
                    throw new SomeException("File already closed!");
                }
            }
            else
                throw new SomeException("String already does not exist in the File Table!");
        }
        else
            throw new SomeException("Type not a string");
    }
}
