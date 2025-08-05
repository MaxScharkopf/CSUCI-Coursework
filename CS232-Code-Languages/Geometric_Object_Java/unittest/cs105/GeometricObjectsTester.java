package unittest.cs105;

import  edu.sbcc.cs105.Circle;
import  edu.sbcc.cs105.Rectangle;
import  edu.sbcc.cs105.GeometricObject;


import static java.lang.System.out;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

public class   GeometricObjectsTester {

    private static final double DELTA = 0.01;
    private static final int maximumScore = 12;
    private static int totalScore;

    @BeforeClass
    public static void setUpBeforeClass() throws Exception {
        totalScore = 0;
    }

    @AfterClass
    public static void afterTesting() {
        out.printf("Your program's functionality scores %d out of %d.\n\n", totalScore, maximumScore);
    }


    @Test
    public void demoTest() {
        assertTrue(true);
        assertEquals(1, 1, DELTA);
    }

    @Test
    public void testAreaCircle() {

        GeometricObject geoObject1 = new Circle(5);

        assertEquals(78.53, geoObject1.getArea(), DELTA);
        totalScore += 2;

    }

    @Test
    public void testPerimeterCircle() {

        GeometricObject geoObject2 = new Circle(5);

        assertEquals(31.42, geoObject2.getPerimeter(), DELTA);
        totalScore += 2;

    }
    @Test
    public void testAreaRectangle() {

        GeometricObject geoObject3 = new Rectangle(5, 3);

        assertEquals(15, geoObject3.getArea(), DELTA);
        totalScore += 2;

    }

    @Test
    public void testPerimeterRectangle() {

        GeometricObject geoObject4 = new Rectangle(5, 3);

        assertEquals(16, geoObject4.getPerimeter(), DELTA);
        totalScore += 2;

    }

    @Test
    public void testPerimeterRectangleCircleEqual() {

        GeometricObject geoObject5 = new Circle(10);
        GeometricObject geoObject6 = new Rectangle(11, 8);

        assertTrue(geoObject5.getPerimeter() != geoObject6.getPerimeter());
        totalScore += 2;

    }

    @Test
    public void testAreaRectangleCircleEqual() {

        GeometricObject geoObject7 = new Circle(23);
        GeometricObject geoObject8 = new Rectangle(18, 12);

        assertTrue(geoObject7.getPerimeter() != geoObject8.getPerimeter());
        totalScore += 2;

    }


}



