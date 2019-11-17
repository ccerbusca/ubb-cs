package model.expressions.operations;

public enum BooleanOperation
{
    AND,
    OR,
    XOR;

    @Override
    public String toString()
    {
        return "BooleanOperation{" + this.name() + '}';
    }
}
