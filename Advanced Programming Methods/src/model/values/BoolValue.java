package model.values;

import model.types.ValueType;

public class BoolValue implements IValue {
    private Boolean value;

    public BoolValue(Boolean value)
    {
        this.value = value;
    }

    @Override
    public ValueType getType()
    {
        return ValueType.BoolType;
    }

    public Boolean getValue()
    {
        return value;
    }

    @Override
    public String toString()
    {
        return "BoolValue{" +
                "value=" + value +
                '}';
    }

    @Override
    public boolean equals(Object another)
    {
        if (another instanceof BoolValue)
        {
            return this.value.equals(((BoolValue) another).getValue());
        }
        return false;
    }
}
