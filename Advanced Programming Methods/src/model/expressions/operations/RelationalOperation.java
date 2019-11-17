package model.expressions.operations;

public enum RelationalOperation
{
    LESS_THAN("<"),
    LESS_THAN_OR_EQUAL("<="),
    EQUAL("=="),
    NOT_EQUAL("!="),
    GREATER_THAN(">"),
    GREATER_THAN_OR_EQUAL(">=");

    private String symbol;

    RelationalOperation(String symbol)
    {
        this.symbol = symbol;
    }

    public String getSymbol()
    {
        return symbol;
    }

    @Override
    public String toString()
    {
        return this.symbol;
    }
}
