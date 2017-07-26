import java.io.*;
import java.util.*;

public class GetSong {

   public static void main(String args[]) throws IOException {  
      FileInputStream in = null;
      FileOutputStream out = null;
      try {
         in = new FileInputStream("input_song.txt");
         out = new FileOutputStream("output_song.txt");
	 BufferedReader br = new BufferedReader(new FileReader("input_song.txt"));
	 String line = null;
	System.out.print("<item>");
	while ((line = br.readLine()) != null) {
		String new_line = line.replace("'", "\\'");
		System.out.print(new_line);
		System.out.print("\\n");		
	}
	System.out.print("</item>\n");

      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}
