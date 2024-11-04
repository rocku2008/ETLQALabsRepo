import pandas as pd
import xml.etree.ElementTree as ET

# Read the text file (assuming it's comma-separated)
df = pd.read_csv('Employees.txt', header=0)

# Create the root XML element
root = ET.Element("employees")

# Convert DataFrame to XML
for _, row in df.iterrows():
    employee = ET.SubElement(root, "employee")
    id_elem = ET.SubElement(employee, "id")
    id_elem.text = str(row['id'])

    name_elem = ET.SubElement(employee, "name")
    name_elem.text = row['name']

    department_elem = ET.SubElement(employee, "department")
    department_elem.text = row['department']

    salary_elem = ET.SubElement(employee, "salary")
    salary_elem.text = str(row['salary'])

# Create a new XML tree and write it to a file
tree = ET.ElementTree(root)
tree.write("Employees.xml", encoding='utf-8', xml_declaration=True)

print("Conversion complete! XML file created as Employees.xml.")
