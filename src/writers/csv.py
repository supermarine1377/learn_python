import csv

class CsvWriter:
    def __init__(self):
        pass
    def write(self, path:str, data:list[dict]=None):
        """
        Writes data to a CSV file.
        Args:
            path (str): The path to the CSV file.
            data (list[dict]): The data to write to the CSV file.
        """
        if not path:
            raise ValueError("path cannot be None or an empty string")
        
        if not data:
            raise ValueError("data cannot be None or an empty list")
        
        with open(path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
