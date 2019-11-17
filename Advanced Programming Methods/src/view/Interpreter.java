package view;

import controller.Controller;
import model.ProgramState;
import model.collections.dictionary.Dictionary;
import model.collections.queue.Queue;
import model.collections.stack.Stack;
import model.expressions.ArithmeticExpression;
import model.expressions.ValueExpression;
import model.expressions.VariableExpression;
import model.expressions.operations.ArithmeticOperation;
import model.statements.*;
import model.types.ValueType;
import model.values.BoolValue;
import model.values.IntValue;
import model.values.StringValue;
import repository.IRepository;
import repository.ProgramStateRepository;
import view.commands.ExitCommand;
import view.commands.RunExample;

public class Interpreter
{

    private static Controller createProgram(IStatement statement, String filename)
    {
        ProgramState programState = new ProgramState(
                new Stack<>(),
                new Queue<>(),
                new Dictionary<>(),
                new Dictionary<>(),
                statement);
        IRepository<ProgramState> repository = new ProgramStateRepository(filename);
        repository.add(programState);
        return new Controller(repository);
    }

    private static Controller firstProgram()
    {
        IStatement statement = new ComposedStatement(
                new VariableDeclarationStatement("v", ValueType.IntType),
                new ComposedStatement(
                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))
                ));
        return createProgram(statement, "log1.txt");
    }

    private static Controller secondProgram()
    {
        IStatement statement = new ComposedStatement(
                new VariableDeclarationStatement("a", ValueType.IntType),
                new ComposedStatement(
                        new VariableDeclarationStatement("b", ValueType.IntType),
                        new ComposedStatement(
                            new AssignStatement("a",
                                new ArithmeticExpression(
                                        new ValueExpression(new IntValue(2)),
                                        new ArithmeticExpression(
                                                new ValueExpression(new IntValue(3)),
                                                new ValueExpression(new IntValue(5)),
                                                ArithmeticOperation.MULTIPLICATION),
                                        ArithmeticOperation.ADDITION)),
                            new ComposedStatement(
                                new AssignStatement("b",
                                        new ArithmeticExpression(
                                                new VariableExpression("a"),
                                                new ValueExpression(new IntValue(1)),
                                                ArithmeticOperation.ADDITION)),
                                new PrintStatement(new VariableExpression("b"))))));
        return createProgram(statement, "log2.txt");
    }

    private static Controller thirdProgram()
    {
        IStatement statement = new ComposedStatement(
                new VariableDeclarationStatement("a", ValueType.BoolType),
                new ComposedStatement(
                    new VariableDeclarationStatement("v", ValueType.IntType),
                    new ComposedStatement(
                        new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                        new ComposedStatement(
                            new IfStatement(
                                    new VariableExpression("a"),
                                    new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                    new AssignStatement("v", new ValueExpression(new IntValue(3)))
                            ),
                            new PrintStatement(new VariableExpression("v"))))));
        return createProgram(statement, "log3.txt");
    }

    private static Controller fourthProgram()
    {
        IStatement statement = new ComposedStatement(
            new VariableDeclarationStatement("varf", ValueType.StringType),
            new ComposedStatement(
                new AssignStatement("varf", new ValueExpression(new StringValue("test.in"))),
                new ComposedStatement(
                    new OpenFileRead(new VariableExpression("varf")),
                    new ComposedStatement(
                        new VariableDeclarationStatement("varc", ValueType.IntType),
                        new ComposedStatement(
                            new ReadFileStatement(new VariableExpression("varf"),"varc"),
                            new ComposedStatement(
                                    new PrintStatement(new VariableExpression("varc")),
                                    new ComposedStatement(
                                            new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                            new ComposedStatement(
                                                    new PrintStatement(new VariableExpression("varc")),
                                                    new CloseReadFileStatement(new VariableExpression("varf"))))))))));
        return createProgram(statement, "log4.txt");
    }

    public static void main(String[] args) {
       TextMenu textMenu = new TextMenu();

       textMenu.addCommand(new ExitCommand("exit", "exit"));
       textMenu.addCommand(new RunExample("1", "first program", Interpreter::firstProgram));
       textMenu.addCommand(new RunExample("2", "second program", Interpreter::secondProgram));
       textMenu.addCommand(new RunExample("3", "third program", Interpreter::thirdProgram));
       textMenu.addCommand(new RunExample("4", "fourth program", Interpreter::fourthProgram));
       textMenu.show();
    }

}
