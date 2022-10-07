import java.io.*;
import java.util.logging.*;
public class MyLogger
{
    public static void main(String args[])
    {
        Logger log = Logger.getLogger(practice.class.getName());

        try{
            FileHandler file = new FileHandler("mylog.log", true);
            log.addHandler(file);
            log.setLevel(Level.ALL);

            SimpleFormatter format = new SimpleFormatter();
            file.setFormatter(format);

            log.info("My first log");
        }
        catch(IOException i){
            i.printStackTrace();
        }
        catch(SecurityException se){
            se.printStackTrace();
        }
        log.info("How are you?");
    }
}
