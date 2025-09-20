# 3484. Design Spreadsheet


class Spreadsheet:
    def __init__(self, rows: int):
        self.cell_values: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cell_values[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cell_values[cell] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]

        left_operand, right_operand = formula.split("+")

        def eval(op: str) -> int:
            if op[0].isdigit():
                return int(op)
            return self.cell_values.get(op, 0)

        return eval(left_operand) + eval(right_operand)


spread_sheet = Spreadsheet([3])
print(spread_sheet.getValue("=5+7"))
spread_sheet.setCell("A1", 10)
print(spread_sheet.getValue("=A1+6"))
spread_sheet.setCell("B2", 15)
print(spread_sheet.getValue("=A1+B2"))
spread_sheet.resetCell("A1")
print(spread_sheet.getValue("=A1+B2"))
