cat ../../src/groundTruthGenerator.py | python construct_call_graph.py > visualization.dot
cat visualization.dot | dot -Tpng > visualization.png
chromium-browser visualization.png