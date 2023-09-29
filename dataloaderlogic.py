import random

class DataLoader:
    def __init__(self, data, batch_size=1, shuffle=False):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.index = 0

        if self.shuffle:
            random.shuffle(self.data)

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

# Example usage:
if __name__ == "__main__":
    # Dummy data points (replace with your own data)
    data_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a DataLoader instance
    dataloader = DataLoader(data_points, batch_size=3, shuffle=True)

    # Iterate through the DataLoader
    for batch in dataloader:
        print("Batch:", batch)
