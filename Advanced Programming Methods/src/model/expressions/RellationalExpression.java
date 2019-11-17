package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.expressions.operations.RelationalOperation;
import model.types.ValueType;
import model.values.BoolValue;
import model.values.IValue;
import model.values.IntValue;

public class RellationalExpression implements IExpression
{
    private IExpression first;
    private IExpression second;
    private RelationalOperation operation;

    public RellationalExpression(IExpression first, IExpression second, RelationalOperation operation)
    {
        this.first = first;
        this.second = second;
        this.operation = operation;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> table) throws SomeException
    {
        IValue eval1 = first.eval(table);
        if (eval1.getType().equals(ValueType.IntType))
        {
            IValue eval2 = second.eval(table);
            if (eval2.getType().equals(ValueType.IntType))
            {
                IntValue value1 = (IntValue) eval1;
                IntValue value2 = (IntValue) eval2;
                boolean result = switch (operation)
                {
                    case LESS_THAN ->value1.getValue() < value2.getValue();
                    case LESS_THAN_OR_EQUAL -> value1.getValue() <= value2.getValue();
                    case EQUAL -> value1.getValue().equals(value2.getValue());
                    case NOT_EQUAL -> !value1.getValue().equals(value2.getValue());
                    case GREATER_THAN -> value1.getValue() > value2.getValue();
                    case GREATER_THAN_OR_EQUAL -> value1.getValue() >= value2.getValue();
                };
                return new BoolValue(result);
            }
            else
                throw new SomeException("Second operand is not an int");
        }
        else
            throw new SomeException("First operand is not an int");
    }
}
