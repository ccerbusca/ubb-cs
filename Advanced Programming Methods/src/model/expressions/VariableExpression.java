package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.values.IValue;

public class VariableExpression implements IExpression {
    private String id;

    public VariableExpression(String id)
    {
        this.id = id;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> table) throws SomeException
    {
        return table.lookup(id);
    }

    @Override
    public String toString()
    {
        return "VariableExpression{" +
                "id='" + id + '\'' +
                '}';
    }
}
