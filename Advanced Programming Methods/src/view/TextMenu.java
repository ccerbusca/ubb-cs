package view;

import view.commands.Command;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class TextMenu
{
    private Map<String, Command> commands;

    public TextMenu()
    {
        commands = new HashMap<>();
    }

    public void addCommand(Command c)
    {
        commands.put(c.getKey(), c);
    }

    private void printMenu()
    {
        commands.values().stream()
                .map(l -> String.format("%4s : %s", l.getKey(), l.getDescription()))
                .forEach(System.out::println);
    }

    public void show()
    {
        Scanner scanner = new Scanner(System.in);
        while(true)
        {
            printMenu();
            System.out.print("Input the option: ");
            String key = scanner.nextLine();
            Command com = commands.get(key);
            if (com == null)
            {
                System.out.println("Invalid Option.");
                continue;
            }
            com.execute();
        }
    }
}
