from graphviz import Digraph

# Create directed graph
dot = Digraph("Route")

dot.attr(rankdir="LR", size="12")

# Nodes
dot.node("H", "Hyderabad")
dot.node("S1", "Suryapet")
dot.node("S2", "Kodad")
dot.node("S3", "Nandigama")
dot.node("S4", "Ibrahimpatnam")
dot.node("S5", "Gollapudi")
dot.node("V", "Vijayawada")

# Edges with Time and Distance
dot.edge("H", "S1", label="1 hr\n60 km")
dot.edge("S1", "S2", label="30 min\n50 km")
dot.edge("S2", "S3", label="40 min\n45 km")
dot.edge("S3", "S4", label="25 min\n30 km")
dot.edge("S4", "S5", label="15 min\n15 km")
dot.edge("S5", "V", label="10 min\n10 km")

# Save graph
dot.render("hyderabad_to_vijayawada", format="png", view=True)

print("Graph created successfully!")