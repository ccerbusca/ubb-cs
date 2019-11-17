package model.types;

import model.values.BoolValue;
import model.values.IValue;
import model.values.IntValue;
import model.values.StringValue;

public enum ValueType implements Type
{
    IntType("int", new IntValue(0)),
    BoolType("bool", new BoolValue(false)),
    StringType("string", new StringValue(""));

    private String message;
    private IValue defaultValue;
    ValueType(String message, IValue defaultValue)
    {
        this.message = message;
        this.defaultValue = defaultValue;
    }

    public String getMessage()
    {
        return message;
    }

    public IValue getDefaultValue()
    {
        return defaultValue;
    }
}
