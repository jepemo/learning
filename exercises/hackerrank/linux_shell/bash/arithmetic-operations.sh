read exp

res=$(python3 -c "print(eval(\"$exp\".replace(\"^\", \"**\")))" | awk '{printf("%.3f", $1)}')
echo $res
