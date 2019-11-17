package model.values;

import model.types.ValueType;

public class StringValue implements IValue
{
    private String value;

    public StringValue(String value)
    {
        this.value = value;
    }

    @Override
    public ValueType getType()
    {
        return ValueType.StringType;
    }

    public String getValue()
    {
        return value;
    }

    @Override
    public boolean equals(Object another)
    {
        if (another instanceof StringValue)
        {
            return this.value.equals(((StringValue) another).getValue());
        }
        return false;
    }

    @Override
    public String toString()
    {
        return "StringValue{'" + value + "'}";
    }
}
