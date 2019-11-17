package model;

import model.collections.dictionary.IDictionary;
import model.collections.queue.IQueue;
import model.collections.stack.IStack;
import model.statements.IStatement;
import model.values.IValue;
import model.values.StringValue;

import java.io.BufferedReader;

public class ProgramState {

    private IStack<IStatement> executionStack;
    private IQueue<IValue> out;
    private IDictionary<String, IValue> symTable;
    private IDictionary<StringValue, BufferedReader> fileTable;

    public ProgramState(IStack<IStatement> executionStack,
                        IQueue<IValue> out,
                        IDictionary<String, IValue> symTable,
                        IDictionary<StringValue, BufferedReader> fileTable,
                        IStatement program)
    {
        this.executionStack = executionStack;
        this.out = out;
        this.symTable = symTable;
        this.fileTable = fileTable;
        executionStack.push(program);
    }

    public IStack<IStatement> getExecutionStack() {
        return executionStack;
    }

    public void setExecutionStack(IStack<IStatement> executionStack) {
        this.executionStack = executionStack;
    }

    public IQueue<IValue> getOut() {
        return out;
    }

    public void setOut(IQueue<IValue> out) {
        this.out = out;
    }

    public IDictionary<String, IValue> getSymTable() {
        return symTable;
    }

    public void setSymTable(IDictionary<String, IValue> symTable) {
        this.symTable = symTable;
    }

    public IDictionary<StringValue, BufferedReader> getFileTable()
    {
        return fileTable;
    }

    public void setFileTable(IDictionary<StringValue, BufferedReader> fileTable)
    {
        this.fileTable = fileTable;
    }

    @Override
    public String toString()
    {
        return "ExecutionStack:\n" + executionStack + "\n" +
                "SymTable:\n" + symTable + "\n" +
                "Out:\n" + out + "\n" +
                "FileTable:\n" + fileTable + "\n";
    }
}
