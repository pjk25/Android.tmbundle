import onebit
import os

template = onebit.env.get_template("builddebug.html")

print template.render(
    title='Build Android App', 
)

