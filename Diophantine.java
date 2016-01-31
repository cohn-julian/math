//a^3 + b^3 + c^3 = 33. What numbers solve this solution?
//https://www.youtube.com/watch?v=wymmCdLdPvM

import java.util.Scanner;
class Diophantine
{
    public static int[] dioph(int n, int range)
    {
        for (int a = (0-range); a <= range; a++)
        {
            for (int b = (0-range); b <= range; b++)
            {
                for (int c = (0-range); c <= range; c++)
                {
                    if ( ( (a * a * a) + (b * b * b) + (c*c*c) )== n)
                    {
                        return new int[]{a,b,c};
                    }
                }
            }
        }
        return new int[]{0,0,0};
    }
    public static void main(String[] args)
    {
        
        Scanner scan = new Scanner( System.in );
        System.out.println("Enter the number to find: ");
        int n  = scan.nextInt();
        System.out.println("Enter the limit: ");
        int limit = scan.nextInt();

        int[] ans = dioph(n,limit);
        for (int i: ans)
        {
            System.out.print (i + "  ");
        }
    }
}



