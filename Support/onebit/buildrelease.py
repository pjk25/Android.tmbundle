import onebit
import os

template = onebit.env.get_template("buildrelease.html")

print template.render(
    title='Build Android App', 
)

