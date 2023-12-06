from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class Cell:
    size: int
    content: str


@dataclass
class Header:
    row: List[Cell]


@dataclass
class Body:
    rows: List[List[Cell]]


class Table:
    """Custom table just because I can ^-^"""

    def __init__(self, header: Header, body: Body) -> None:
        self.header = header
        self.body = body

    def _draw_outside_border(self):
        return "+".join([f"{'-'*cell.size}+" for cell in self.header.rows]) + "\n"

    def _draw_header_content(self):
        return "|".join([f" {cell.content} |" for cell in self.header.rows]) + "\n"

    def _draw_header_lower_border(self):
        return "+".join([f"{'='*cell.size}+" for cell in self.header.rows]) + "\n"

    def _draw_body(self):
        return "".join(
            [
                "|".join([f" {cell.content} |" for cell in row])
                + "\n"
                + self._draw_header_lower_border
                for row in self.body.rows
            ]
        )


def draw_from_list(content: List[List[str]]):
    """Assumes the first array is the header"""

    np_content = np.array(content)
    x, y = np_content.shape
    np_transposed = np_content.reshape(y, x)
