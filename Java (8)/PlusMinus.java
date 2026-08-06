import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
    // Write your code here
        int total = arr.size();
        int threshold = 0;
        List<Integer> signs = Arrays.asList(0 , 0, 0);
        for (int i = 0; i < arr.size(); i++)
        {
            int num = arr.get(i);
            if (num == threshold)
            {
                signs.set(2, signs.get(2) + 1);
            }
            else if (num > threshold)
            {
                signs.set(0, signs.get(0) + 1);   
            }
            else 
            {
                signs.set(1, signs.get(1) + 1);
            }
            
        }
         System.out.printf("%.6f%n", (double) signs.get(0)/total);   
         System.out.printf("%.6f%n", (double) signs.get(1)/total);   
         System.out.printf("%.6f%n", (double) signs.get(2)/total);   
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
