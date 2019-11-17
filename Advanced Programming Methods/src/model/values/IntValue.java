package model.values;

import model.types.ValueType;

public class IntValue implements IValue {
    private Integer value;

    public IntValue(Integer value)
    {
        this.value = value;
    }

    @Override
    public ValueType getType()
    {
        return ValueType.IntType;
    }

    public Integer getValue()
    {
        return value;
    }

    public void setValue(Integer value)
    {
        this.value = value;
    }

    @Override
    public String toString()
    {
        return "IntValue{" +
                "value=" + value +
                '}';
    }

    public boolean equals(Object another)
    {
        if (another instanceof IntValue)
        {
            return this.value.equals(((IntValue) another).getValue());
        }
        return false;
    }
}
