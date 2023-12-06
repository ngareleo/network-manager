from dataclasses import dataclass
from typing import List
import numpy as np
from enum import Enum


class Alignment(Enum):
    CENTER = 0
    RIGHT = 1
    LEFT = 3


@dataclass
class Cell:
    size: int | None = None
    content: int | None = None


@dataclass
class Header:
    row: list[Cell]


@dataclass
class Body:
    rows: list[list[Cell]]


class Table:
    """Custom table just because I can ^-^"""

    def __init__(self, header: Header, body: Body) -> None:
        self.header = header
        self.body = body

    def _draw_horizontal_border(self):
        return (
            "+".join(
                ["{:-<{size}}".format("", size=cell.size) for cell in self.header.row]
            )
            + "\n"
        )

    def _draw_header_content(self):
        return "|".join([f" {cell.content} |" for cell in self.header.row]) + "\n"

    def _draw_body(self):
        return "".join(
            [
                "|".join(
                    [f" {cell.content} |" for cell in row]
                    + ["\n", self._draw_horizontal_border()]
                )
                for row in self.body.rows
            ]
        )

    def draw_table(self):
        print(
            "".join(
                [
                    self._draw_horizontal_border(),
                    self._draw_header_content(),
                    self._draw_horizontal_border(),
                    self._draw_body(),
                ]
            )
        )

    @classmethod
    def draw_from_list(cls, content: List[List[str]]):
        """Assumes the first array is the header"""
        cells = np.transpose([[Cell(content=cell) for cell in row] for row in content])

        for col in cells:
            width = len(max(col, key=lambda a: len(a.content)).content) + 3
            for cell in col:
                cell.size = width
        [head, *rest] = list(np.transpose(cells))
        table = Table(header=Header(row=head), body=Body(rows=rest))
        table.draw_table()


if __name__ == "__main__":
    s = [
        ["Name", "Org", "Age"],
        ["Lead Jason", "Med", "23"],
        ["Ruthy Ljarson", "Eng", "23"],
    ]
    Table.draw_from_list(s)
