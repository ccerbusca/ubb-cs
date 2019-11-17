package model.expressions.operations;

public enum ArithmeticOperation {
    ADDITION,
    SUBTRACTION,
    DIVISION,
    MULTIPLICATION;

    @Override
    public String toString()
    {
        return "ArithmeticOperation{" + this.name() + '}';
    }
}
