read x
read y
read z

if [ $x -eq $y ] && [ $y -eq $z ]; then
    echo "EQUILATERAL"
elif [ $x -ne $y ] && [ $y -ne $z ] && [ $x -ne $z ]; then
    echo "SCALENE"
elif [ $x -eq $y ] && [ $x -ne $z ]; then
    echo "ISOSCELES"
elif [ $y -eq $z ] && [ $x -ne $z ]; then
    echo "ISOSCELES"
fi
