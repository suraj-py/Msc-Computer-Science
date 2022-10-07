
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.InputStreamReader;
public class WordSearch {
 public static void main(String[] args) throws IOException{

        String str = "";
        String ser = "";
        int flag = 0;

        FileReader file = new FileReader("hello.txt");
        BufferedReader buff_r = new BufferedReader(file);
        str = buff_r.readLine();

        InputStreamReader i = new InputStreamReader(System.in);
        BufferedReader buff_s = new BufferedReader(i);
        System.out.println("Enter the word that you want to search: ");
        ser = buff_s.readLine();

        String[] s = new String[str.length()];
        s = str.split(" ");

        for(int a=0; a<s.length; a++){
            if(ser.equalsIgnoreCase(s[a])){
                System.out.println("Text "+ser+" found");
                flag = 1;
            }
            if(flag==0){
                System.out.println("Text "+ser+" not found");
            }
        }


    }
}
