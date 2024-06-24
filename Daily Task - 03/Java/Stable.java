public class Stable{
    public static void main(String[] args){
        int input1=124;
        // int input2=1313;
        // int input3=122;
        // int input4=678;
        // int input5=898;
        String str1 = String.valueOf(input1);
        // String str2 = String.valueOf(input2);
        // String str3 = String.valueOf(input3);
        // String str4 = String.valueOf(input4);
        // String str5 = String.valueOf(input5);
        // System.out.print(str.length());
        int lenght1=str1.length();
        if (lenght1%2!=0)
            System.out.println("Unstable Number");
        else
            System.out.println("Stable Number");
    }
}