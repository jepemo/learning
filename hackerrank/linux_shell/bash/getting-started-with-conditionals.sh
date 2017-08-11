read n

if [ "$n" == "Y" ] || [ "$n" == "y" ] ; then
    echo "YES"
elif [ "$n" == "N" ] || [ "$n" == "n" ] ; then
    echo "NO"
fi
