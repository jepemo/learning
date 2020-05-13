SELECT 
    CASE
        WHEN ((A+B <= C) OR (B+C <= A) OR (A+C <= B)) THEN 'Not A Triangle'
        WHEN (A = B AND B = C) THEN 'Equilateral'
        WHEN ((A = B AND B <> C) OR (A <> B AND B = C) OR (A = C AND B <> C)) THEN 'Isosceles'
        WHEN (A <> B AND B <> C) THEN 'Scalene'
    END
FROM
    TRIANGLES
    
