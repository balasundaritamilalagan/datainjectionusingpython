import random

class DataLoader:
    def __init__(self, data, batch_size=1, shuffle=False):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.index = 0

    def __len__(self):
        return len(self.data) // self.batch_size

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch

class Dataset:
    def __init__(self, data_paths, labels=None, shuffle=False):
        self.data_paths = data_paths
        self.labels = labels

        if self.labels is None:
            self.labels = [None] * len(data_paths)

        self.data = list(zip(data_paths, labels))  # Combine data and labels

        if shuffle:
            random.shuffle(self.data)

    def __len__(self):
        return len(self.data_paths)

    def __getitem__(self, idx):
        data_point = self.data_paths[idx]
        label = self.labels[idx] if self.labels else None
        return data_point, label

# Example usage:
if __name__ == "__main__":
    # Dummy data paths and labels
    data_paths = ["C:\\Users\\SSLTP11315\\Pictures\\1.jpg", "C:\\Users\\SSLTP11315\\Pictures\\image.jpg",
                  "C:\\Users\\SSLTP11315\\Pictures\\solar.jpg"]
    labels = [0, 1, 0]

    # Create a Dataset instance
    dataset = Dataset(data_paths, labels, shuffle=True)

    # Create a DataLoader instance
    dataloader = DataLoader(dataset, batch_size=2)

    # Iterate through the DataLoader
    for batch in dataloader:
        print("Batch:", batch)
