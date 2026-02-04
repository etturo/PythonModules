#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return ("Output: " + result)


class NumericProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return self.format_output("[ERROR] non numeric values inserted")
        lenght: int = len(data)
        total: int = sum(data)
        avarage: float = total / lenght
        return self.format_output(f"Processed {lenght} numeric values,"
                                  f" sum={total}, avg={avarage:.1f}")

    def validate(self, data) -> bool:
        if isinstance(data, list) and all(
           isinstance(x, (int, float)) for x in data
           ) and len(data) > 0:
            print("Validation: Numeric data verified")
            return True
        else:
            print("Validation: Numeric data  not valid")
            return False


class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return self.format_output("[ERROR] non text data")
        strlen: int = len(data)
        words: list[str] = data.split(' ')
        word_count: int = len(words)
        result: str = f"Processed text: {strlen} character, {word_count} words"
        return self.format_output(result)

    def validate(self, data) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        else:
            print("Validation: Text data  not valid")
            return False


class LogProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            return self.format_output("[ERROR] no log data")
        try:
            result: str
            error_type: str
            message: str
            error_type, message = data.split(':', 1)
            clean_error: str = error_type.strip()
            clean_message: str = message.strip()
            result = clean_error + " level detected " + clean_message
            return self.format_output(result)
        except ValueError:
            return ("Failed Parsing")

    def validate(self, data) -> bool:
        if isinstance(data, str) and ":" in data:
            print("Validation: Log data verified")
            return True
        else:
            print("Validation: Log data  not valid")
            return False

    def format_output(self, result: str) -> str:
        return f"[ALERT] {result}"


def main():
    numeric_list: list[int] = [1, 2, 3, 4, 5]
    text: str = "Hello Nexus World"
    log: str = "ERROR: Connection timeout"
    processor = NumericProcessor()
    print(f"Processing data: {numeric_list}")
    print(processor.process(numeric_list))
    print()
    processor = TextProcessor()
    print(f"Processing data: \"{text}\"")
    print(processor.process(text))
    print()
    processor = LogProcessor()
    print(processor.process(log))
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    print("\n=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    main()
    print()
