import plotly.graph_objects as go

# Data structure for sunburst chart
data = {
    "library_types": [
        {
            "name": "Static Libs", 
            "characteristics": ["Direct Python", "Simple impl", "Limited dyn", "Functions kw", "@keyword dec"]
        }, 
        {
            "name": "Dynamic Libs", 
            "characteristics": ["get_kw_names", "run_keyword", "Runtime disc", "Complex/flex", "Generate dyn"]
        }, 
        {
            "name": "Hybrid Libs", 
            "characteristics": ["Static+dyn", "Best of both", "Moderate", "Static+disc", "PythonLib"]
        }, 
        {
            "name": "Remote Libs", 
            "characteristics": ["Diff machines", "XML-RPC", "Lang indep", "Distributed", "Cross-plat"]
        }
    ]
}

# Prepare data for sunburst
ids = []
labels = []
parents = []
values = []

# Root
ids.append("Robot Framework")
labels.append("Robot Framework")
parents.append("")
values.append(100)

# Library types
for lib_type in data["library_types"]:
    lib_name = lib_type["name"]
    ids.append(lib_name)
    labels.append(lib_name)
    parents.append("Robot Framework")
    values.append(25)
    
    # Characteristics
    for i, char in enumerate(lib_type["characteristics"]):
        char_id = f"{lib_name}_{i}"
        ids.append(char_id)
        labels.append(char[:15])  # Ensure 15 char limit
        parents.append(lib_name)
        values.append(5)

# Brand colors
colors = ["#1FB8CD", "#FFC185", "#ECEBD5", "#5D878F", "#D2BA4C"]

# Create sunburst chart
fig = go.Figure(go.Sunburst(
    ids=ids,
    labels=labels,
    parents=parents,
    values=values,
    branchvalues="total",
    maxdepth=3,
    textinfo="label",
    textfont_size=10
))

fig.update_layout(
    title="Robot Framework Libs",
    font_size=12
)

# Save the chart
fig.write_image("robot_framework_libraries.png")