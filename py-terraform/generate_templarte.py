# from string import Template

# with open ("main_terraform.template", "r") as aws_template:
#  file_data = aws_template.read()

#  print("Template Content Before Substitution:")
#  print(file_data)

#  template_data = Template(file_data)
#  sub_data = template_data.substitute({"providername": "aws", "region": "ap-south-1", "access_key": "goku", "resourcetype":"aws_instance","resourcename":"web",
#                                       "aminame":"ami-03f4878755434977f", "instancename":"t2.micro","tagsname":"web-app"})
#  with open ("main.tf", "w") as main_file:
#   main_file.write(sub_data)

from string import Template

# Define variables
variables = {
    "providername": "aws",
    "resourcetype": "aws_instance",
    "resourcename": "web",
    "region": "ap-south-1",
    "access_key": "goku",
    "ami_id": "ami-03f4878755434977f",
    "instancename": "t2.micro",
    "tagsname": "web-app"
}

# Read the Terraform template file
with open("main_terraform.template", "r") as template_file:
    template_content = template_file.read()

# Substitute variables into the template
template = Template(template_content)
substituted_content = template.substitute(variables)

# Write the substituted content to the main.tf file
with open("main.tf", "w") as main_file:
    main_file.write(substituted_content)

print("Template has been successfully processed.")
