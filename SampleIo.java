/* IMPORTANT: Multiple classes and nested static classes are supported */

/*
 * uncomment this if you want to read input.
//imports for BufferedReader*/
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import for Scanner and other utility classes
import java.util.*;
import java.math.*;
    

// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail

class SampleIo {
    
    static int[][] arr = new int[10][10];
    static int n = 0;
    
    static void p(String s){
        System.out.println(s);
    }
    
    public static void main(String args[] ) throws Exception {
        /* Sample code to perform I/O:
         * Use either of these methods for input*/

        /*BufferedReader*/
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String name = br.readLine();                // Reading input from STDIN
        System.out.println("Hi, " + name + ".");    // Writing output to STDOUT

        /*Scanner*/
        Scanner s = new Scanner(System.in);
        n = s.nextInt();  
        s.close();

    }
}
