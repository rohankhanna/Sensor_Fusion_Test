date
echo "------------"
cat ../../src/givenInputGenerator.py | python construct_call_graph.py > visualization.dot
cat visualization.dot | dot -Tpng > visualization.png
chromix-too reload "file://$PWD/visualization.png"
echo "------------"