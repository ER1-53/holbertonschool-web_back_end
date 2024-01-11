#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ return dictionary"""
        
        assert 0 <= index < len(self.__indexed_dataset)

        next_index = index + page_size
        end_index = next_index - 1
        current_page = []
        end_of_page = min(end_index + 1, len(self.dataset()))

        for i in range(index, end_of_page):
            current_page.append(self.dataset()[i])

        return {
            "index": index,
            "data": current_page,
            "page_size": page_size,
            "next_index": next_index
        }
