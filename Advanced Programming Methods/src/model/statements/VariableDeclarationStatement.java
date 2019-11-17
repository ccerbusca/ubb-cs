package model.statements;

import model.ProgramState;
import model.collections.dictionary.IDictionary;
import model.exceptions.SomeException;
import model.types.Type;
import model.values.IValue;

public class VariableDeclarationStatement implements IStatement {
    private String name;
    private Type type;

    public VariableDeclarationStatement(String name, Type type)
    {
        this.name = name;
        this.type = type;
    }

    @Override
    public ProgramState execute(ProgramState state)
    {
        IDictionary<String, IValue> symTable = state.getSymTable();
        if (!symTable.exists(name))
        {
            symTable.put(name, type.getDefaultValue());
            return state;
        }
        else
            throw new SomeException("Variable already exists");
    }

    @Override
    public String toString()
    {
        return "VariableDeclarationStatement{" +
                "name='" + name + '\'' +
                ", type=" + type +
                '}';
    }
}
