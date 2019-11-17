package model.statements;

import model.ProgramState;
import model.exceptions.SomeException;
import model.expressions.IExpression;
import model.types.ValueType;
import model.values.IValue;
import model.values.StringValue;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenFileRead implements IStatement
{
    private IExpression expression;

    public OpenFileRead(IExpression expression)
    {
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state)
    {
        IValue value = expression.eval(state.getSymTable());
        if (value.getType().equals(ValueType.StringType))
        {
            if (!state.getFileTable().exists((StringValue) value))
            {
                try
                {
                    var reader = new FileReader(((StringValue) value).getValue());
                    var buffReader = new BufferedReader(reader);
                    state.getFileTable().put((StringValue) value, buffReader);
                    return state;
                }
                catch (IOException e)
                {
                    throw new SomeException(String.format("I/O Error: %s", e.getMessage()));
                }
            }
            else
                throw new SomeException("File already exists in File Table!");
        }
        else
            throw new SomeException("Type not a string");
    }
}
