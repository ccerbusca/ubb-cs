package controller;

import model.ProgramState;
import model.collections.stack.IStack;
import model.exceptions.SomeException;
import model.statements.IStatement;
import repository.IRepository;

public class Controller {

    private IRepository<ProgramState> programRepository;

    public Controller(IRepository<ProgramState> repository)
    {
        this.programRepository = repository;
    }

    public ProgramState oneStep(ProgramState state) throws SomeException
    {
        IStack<IStatement> executionStack = state.getExecutionStack();
        if (executionStack.isEmpty())
            throw new SomeException("Stack is empty");
        IStatement statement = executionStack.pop();
        return statement.execute(state);
    }

    public void allStep()
    {
        ProgramState currentProgram = programRepository.getCurrentProgram();
        programRepository.logPrgStateExec();
        while(!currentProgram.getExecutionStack().isEmpty())
        {
            oneStep(currentProgram);
            programRepository.logPrgStateExec();
        }
    }
}
