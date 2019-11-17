package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.values.IValue;

public class ValueExpression implements IExpression {
    private IValue value;

    public ValueExpression(IValue value)
    {
        this.value = value;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> table) throws SomeException
    {
        return value;
    }

    @Override
    public String toString()
    {
        return "ValueExpression{" +
                "value=" + value +
                '}';
    }
}
