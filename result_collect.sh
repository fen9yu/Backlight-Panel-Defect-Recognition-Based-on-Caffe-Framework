cat caffemesg | awk -F '= ' '/Test net output #0/ {print $2}'
echo
cat caffemesg | awk '/Test net output #1/ {print $11}'
