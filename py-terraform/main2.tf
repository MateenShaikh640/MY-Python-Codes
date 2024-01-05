provider "aws" {
    region = "ap-south-1"
    access_key = "goku"
}
resource "aws_instance" "web" {
    ami = "ami-03f4878755434977f"
    instance_type = "t2.micro"

    tags = {
      Name =  "web-app"
    }
  
}


