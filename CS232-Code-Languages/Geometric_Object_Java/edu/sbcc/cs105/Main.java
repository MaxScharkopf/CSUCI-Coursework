package edu.sbcc.cs105;

public class Main {
    public static void main(String[] args) {
        // Create a Circle object
        Circle circle = new Circle(5.0, "Red", true);
        System.out.println("Circle:");
        System.out.println("Color: " + circle.getColor());
        System.out.println("Filled: " + circle.isFilled());
        System.out.println("Radius: " + circle.getRadius());
        System.out.println("Diameter: " + circle.getDiameter());
        System.out.println("Area: " + circle.getArea());
        System.out.println("Perimeter: " + circle.getPerimeter());
        System.out.println();

        // Create a Rectangle object
        Rectangle rectangle = new Rectangle(4.0, 7.0, "Blue", false);
        System.out.println("Rectangle:");
        System.out.println("Color: " + rectangle.getColor());
        System.out.println("Filled: " + rectangle.isFilled());
        System.out.println("Width: " + rectangle.getWidth());
        System.out.println("Height: " + rectangle.getHeight());
        System.out.println("Area: " + rectangle.getArea());
        System.out.println("Perimeter: " + rectangle.getPerimeter());
    }
}