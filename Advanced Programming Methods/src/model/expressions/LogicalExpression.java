package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.expressions.operations.BooleanOperation;
import model.types.ValueType;
import model.values.BoolValue;
import model.values.IValue;

public class LogicalExpression implements IExpression {
    private IExpression first;
    private IExpression second;
    private BooleanOperation operation;

    public LogicalExpression(IExpression first,
                             IExpression second,
                             BooleanOperation operation)
    {
        this.first = first;
        this.second = second;
        this.operation = operation;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> table) throws SomeException
    {
        IValue v1, v2;
        v1 = first.eval(table);
        if (v1.getType().equals(ValueType.BoolType))
        {
            v2 = second.eval(table);
            if (v2.getType().equals(ValueType.BoolType))
            {
                BoolValue b1 = (BoolValue)v1;
                BoolValue b2 = (BoolValue)v2;
                boolean a, b;
                a = b1.getValue();
                b = b2.getValue();
                return switch(operation) {
                    case AND -> new BoolValue(a && b);
                    case OR -> new BoolValue(a || b);
                    case XOR -> new BoolValue(a ^ b);
                };
            }
            else
                throw new SomeException("Second operand is not a boolean");
        }
        else
            throw new SomeException("First operand is not a boolean");
    }

    @Override
    public String toString()
    {
        return "LogicalExpression{" +
                "first=" + first +
                ", second=" + second +
                ", operation=" + operation +
                '}';
    }
}
