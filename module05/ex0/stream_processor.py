from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: list[int]) -> str:
        try:
            n: int = len(data)
            sum_data: int = sum(data)
            return (f"Processing {n} numeric value, "
                    f"sum= {sum_data} avg= {sum_data/n}")
        except (ValueError, TypeError, ZeroDivisionError):
            return (f"Error: '{data}' is invalide!")

    def validate(self, data: list[int]) -> bool:
        try:
            summ: int = sum(data)
            if summ > 0:
                return True
            else:
                return False
        except (ValueError, TypeError):
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            lenn: int = len(data)
            word: int = len(data.split(' '))
            return (f"Processed text: {lenn} characters, {word} words")
        except (AttributeError, ValueError):
            return (f"ERROR: {data} Text Error!")

    def validate(self, data: str) -> bool:
        try:
            word: int = len(data.split(' '))
            if word:
                return True
            else:
                return False
        except (AttributeError, ValueError):
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            alert: list[str] = data.split(":")
            if (alert[0] == "ERROR"):
                level: str = "[ALERT]"
            elif (alert[0] == "INFO"):
                level = "[INFO]"
            else:
                level = "[UNKNOWN]"
            return (f"{level} {alert[0]} level detected:{alert[1]}")
        except Exception:
            return (f"ERROR: {data} is must be string")

    def validate(self, data: str) -> bool:
        try:
            split: list[str] = data.split(':')
            if len(split) != 2:
                return False
            else:
                return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")

    numeric_data: List[int] = [1, 2, 3, 4, 5]
    num_object: NumericProcessor = NumericProcessor()
    print(f"Processing data: {numeric_data}")
    process_result: str = num_object.process(numeric_data)
    verify: str
    if num_object.validate(numeric_data) is True:
        verify = "Numeric data verified"
    else:
        verify = "Numeric data is not verified"
    print(f"Validation: {verify}")
    print(num_object.format_output(process_result))

    print("\nInitializing Text Processor...")

    text_data: str = "Hello Nexus World"
    text_object: TextProcessor = TextProcessor()
    print(f"Processing data: \"{text_data}\"")
    process_result = text_object.process(text_data)
    if text_object.validate(text_data) is True:
        verify = "Text data verified"
    else:
        verify = "Text data is not verified"
    print(f"Validaton: {verify}")
    print(text_object.format_output(process_result))

    print("\nInitializing Log Processor...")

    log_data: str = "ERROR: Connection timeout"
    log_object: LogProcessor = LogProcessor()
    print(f"Processing data: \"{log_data}\"")
    process_result = log_object.process(log_data)
    if log_object.validate(log_data) is True:
        verify = "Log entry verified"
    else:
        verify = "Log entry is not verified"
    print(f"Validation: {verify}")
    print(log_object.format_output(process_result))

    print("\n=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")
    print("Result 1:", num_object.process([1, 2, 3]))
    print("Result 1:", text_object.process("hello world!"))
    print("Result 3:", log_object.process("INFO: System ready"))
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
