package repository;

import model.ProgramState;
import model.exceptions.SomeException;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ProgramStateRepository implements IRepository<ProgramState> {
    private List<ProgramState> repo;
    private String logPath;

    public ProgramStateRepository(String logPath)
    {
        this.logPath = logPath;
        this.repo = new ArrayList<>();
    }

    @Override
    public void add(ProgramState e)
    {
        repo.add(e);
    }

    @Override
    public List<ProgramState> getAll()
    {
        return repo;
    }

    @Override
    public ProgramState getCurrentProgram() throws IndexOutOfBoundsException
    {
        return repo.get(0);
    }

    @Override
    public void logPrgStateExec() throws SomeException
    {
        try
        {
            var logFile = new PrintWriter(new BufferedWriter(new FileWriter(logPath, true)));

            logFile.println(getCurrentProgram());

            logFile.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
