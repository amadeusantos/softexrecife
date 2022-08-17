import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Main {
    public static void main(String[] args) {
        try {
            FileInputStream fileNew = new FileInputStream("test.json");
            ObjectInputStream arquvoNew = new ObjectInputStream(fileNew);
             Object obj = arquvoNew.readObject();
            arquvoNew.close();
            FileOutputStream file = new FileOutputStream("test.json");
            ObjectOutputStream arquivo = new ObjectOutputStream(file);
            arquivo.writeObject(obj);
            arquivo.close();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
