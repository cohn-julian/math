//simple program when givin amount right and total questions calculates the %

import java.util.Scanner;

class calculator
{
    private double points;
    private double total;

    public calculator(double pt, double ttl)
    {
        points = pt;
        total = ttl;
    }

    public double getPoints()
    {
        return points;
    }

    public double getTotal()
    {
        return total;
    }

    public double percent()
    {
        return ( (points/total) * 100);
    }
}
class score
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner( System.in );
        System.out.println("Enter The total number RIGHT:   ");
        double point = scan.nextDouble();
        System.out.println("Enter the total number of QUESIONS: ");
        double toal = scan.nextDouble();
        calculator per= new calculator(point,toal);
        System.out.println( Double.toString(per.percent()) + "%");
    }
}
