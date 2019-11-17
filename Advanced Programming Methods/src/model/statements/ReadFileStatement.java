package model.statements;

import model.ProgramState;
import model.exceptions.SomeException;
import model.expressions.IExpression;
import model.types.ValueType;
import model.values.IValue;
import model.values.IntValue;
import model.values.StringValue;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement
{
    private IExpression expression;
    private String variableName;

    public ReadFileStatement(IExpression expression, String variableName)
    {
        this.expression = expression;
        this.variableName = variableName;
    }


    @Override
    public ProgramState execute(ProgramState state)
    {
        if (state.getSymTable().exists(variableName))
        {
            if (state.getSymTable().lookup(variableName).getType().equals(ValueType.IntType))
            {
                IValue value = expression.eval(state.getSymTable());
                if (value.getType().equals(ValueType.StringType))
                {
                    StringValue stringValue = (StringValue) value;
                    if (state.getFileTable().exists(stringValue))
                    {
                        BufferedReader reader = state.getFileTable().lookup(stringValue);
                        IntValue intValue = new IntValue(0);
                        try
                        {
                            String line = reader.readLine();
                            if (line != null)
                                intValue.setValue(Integer.parseInt(line));
                        }
                        catch (IOException e)
                        {
                            throw new SomeException(e.getMessage());
                        }
                        state.getSymTable().put(variableName, intValue);
                        return state;
                    }
                    else
                        throw new SomeException("File does not exist in File Table");
                }
                else
                    throw new SomeException("Expression evaluation not of type StringValue");
            }
            else
                throw new SomeException(String.format("Variable %s is not of type int", variableName));
        }
        else
            throw new SomeException(String.format("Variable %s does not exist", variableName));
    }
}
