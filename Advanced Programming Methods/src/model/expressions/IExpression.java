package model.expressions;

import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.values.IValue;

public interface IExpression {
    IValue eval(IDictionary<String, IValue> table) throws SomeException;
}
