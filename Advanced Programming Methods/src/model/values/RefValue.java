package model.values;

import model.types.RefType;
import model.types.Type;

public class RefValue implements IValue
{
    private Integer address;
    private Type locationType;

    public RefValue(Integer address, Type locationType)
    {
        this.address = address;
        this.locationType = locationType;
    }

    @Override
    public Type getType()
    {
        return new RefType(locationType);
    }

    public Integer getAddress()
    {
        return address;
    }
}
