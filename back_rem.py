from rembg import remove
from PIL import Image

input_path = 'K:\INTERNSHIP\Zomato-Clone\restraunt2.jpg' 
output_path = 'K:\INTERNSHIP\Zomato-Clone\restraunt2.jpg'



input = Image.open(input_path) 
output = remove(input) 
output.save(output_path)