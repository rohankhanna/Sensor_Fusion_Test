cat ../../src/testGenerator.py | python construct_call_graph.py > test.dot
cat visualization.dot | dot -Tpng > visualization.png
chromium-browser visualization.png