import pandas as pd
import pdfkit

df = pd.read_csv("datalist.csv")
print(df)

with open("template.html", mode="r") as f:
    template_html = f.read()

for values in df.values:
    html = template_html

    student_id = values[0]
    name = values[1]
    score = values[2]

    html = html.replace("{% student_id %}", student_id)
    html = html.replace("{% name %}", name)
    html = html.replace("{% score %}", score)

    print(html)

    pdfkit.from_string(html, f"save/{student_id}.pdf")
        
   
