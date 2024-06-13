import torch
from torchvision import transforms
import PIL

# Define the path to the input image and the output image
input_image_path = "data/train/pid00001/study1/view1_frontal.jpg"
output_image_path = "2024/pp/figs/aug_image.png"

# Load the image
image = PIL.Image.open(input_image_path)

# Check dimensions
original_width, original_height = image.size
max_side = max(original_width, original_height)

# Calculate padding to make the image square
padding_left = (max_side - original_width) // 2
padding_right = max_side - original_width - padding_left
padding_top = (max_side - original_height) // 2
padding_bottom = max_side - original_height - padding_top

# Apply padding
image = transforms.functional.pad(image, (padding_left, padding_top, padding_right, padding_bottom), fill=0)

# Define the transformations
transform = transforms.Compose([
    transforms.RandAugment(),
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
    lambda x: x.repeat(3, 1, 1)  # Convert grayscale to RGB
])

# Apply transformations
transformed_image = transform(image)

# Convert tensor back to PIL image
transformed_image = transforms.ToPILImage()(transformed_image)

# Save the transformed image
transformed_image.save(output_image_path)

print(f"Transformed image saved at {output_image_path}")
