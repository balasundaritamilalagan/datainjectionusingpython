import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image

# Define a custom dataset class
class CustomDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        # Assuming you have a list of file paths and corresponding labels
        self.file_paths = ['C:\\Users\\SSLTP11315\\Pictures\\1.jpg',
                           'C:\\Users\\SSLTP11315\\Pictures\\image.jpg']  # List of file paths
        # List of file paths
        self.labels = [0,1]  # Corresponding labels

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        img_path = self.file_paths[idx]
        image = Image.open(img_path)
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label

# Define data transformations
data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Create an instance of the custom dataset
custom_dataset = CustomDataset(data_dir='path_to_data_dir', transform=data_transform)

# Create a data loader
batch_size = 32
dataloader = DataLoader(custom_dataset, batch_size=batch_size, shuffle=True)

# Iterate through the data loader
for inputs, labels in dataloader:
    # Here, you can perform training steps with the batch of inputs and labels
    # For simplicity, we'll just print the shapes of inputs and labels
    print(f"Batch Inputs Shape: {inputs.shape}, Batch Labels: {labels}")
