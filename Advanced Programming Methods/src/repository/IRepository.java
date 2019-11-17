package repository;

import model.ProgramState;
import model.exceptions.SomeException;

import java.util.List;

public interface IRepository<T> {
    void add(T e);
    List<ProgramState> getAll();
    ProgramState getCurrentProgram() throws IndexOutOfBoundsException;
    void logPrgStateExec() throws SomeException;
}
