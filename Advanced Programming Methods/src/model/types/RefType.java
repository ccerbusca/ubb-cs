package model.types;

import model.values.IValue;
import model.values.RefValue;

public class RefType implements Type
{
    private Type inner;

    public RefType(Type inner)
    {
        this.inner = inner;
    }

    public Type getInner()
    {
        return inner;
    }

    @Override
    public boolean equals(Object another)
    {
        if (another instanceof RefType)
        {
            return this.inner.equals(((RefType) another).getInner());
        }
        return false;
    }

    @Override
    public IValue getDefaultValue()
    {
        return new RefValue(0, inner);
    }
}
