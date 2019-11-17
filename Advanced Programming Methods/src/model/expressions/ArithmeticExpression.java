package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.expressions.operations.ArithmeticOperation;
import model.types.ValueType;
import model.values.IValue;
import model.values.IntValue;

public class ArithmeticExpression implements IExpression {
    private IExpression first;
    private IExpression second;
    private ArithmeticOperation operation;

    public ArithmeticExpression(IExpression first,
                                IExpression second,
                                ArithmeticOperation operation) {
        this.first = first;
        this.second = second;
        this.operation = operation;
    }

    @Override
    public IValue eval(IDictionary<String, IValue> table) throws SomeException {
        IValue v1, v2;
        v1 = first.eval(table);
        if (v1.getType().equals(ValueType.IntType))
        {
            v2 = second.eval(table);
            if (v2.getType().equals(ValueType.IntType))
            {
                IntValue i1 = (IntValue)v1;
                IntValue i2 = (IntValue)v2;
                int n1, n2;
                n1 = i1.getValue();
                n2 = i2.getValue();
                return switch (operation) {
                    case ADDITION -> new IntValue(n1 + n2);
                    case SUBTRACTION -> new IntValue(n1 - n2);
                    case MULTIPLICATION -> new IntValue(n1 * n2);
                    case DIVISION ->
                            {
                                if (n2 == 0)
                                    throw new SomeException("Division by zero");
                                else yield new IntValue(n1 / n2);
                            }
                };

            }
            else
                throw new SomeException("Second operand not and integer!");
        }
        else
            throw new SomeException("First operand not an integer");
    }

    @Override
    public String toString()
    {
        return "ArithmeticExpression{" +
                "first=" + first +
                ", second=" + second +
                ", operation=" + operation +
                '}';
    }
}
