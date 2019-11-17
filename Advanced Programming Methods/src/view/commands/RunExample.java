package view.commands;

import controller.Controller;
import model.exceptions.SomeException;

import java.util.function.Supplier;

public class RunExample extends Command
{
    private Supplier<Controller> supplier;
    public RunExample(String key, String description, Supplier<Controller> supplier)
    {
        super(key, description);
        this.supplier = supplier;
    }

    @Override
    public void execute()
    {
        try
        {
            supplier.get().allStep();
        }
        catch (SomeException e)
        {
            e.printStackTrace();
            System.exit(1);
        }
    }
}
