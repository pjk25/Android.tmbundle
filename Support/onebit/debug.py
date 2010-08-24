import onebit
import os

template = onebit.env.get_template("debug.html")

print template.render(
    title='Build Android App', 
)

