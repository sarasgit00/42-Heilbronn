"""
Exercise 0: Data Processor Foundation
A polymorphic data processing system using abstract base classes.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    """Abstract base processor defining the common interface."""

    def __init__(self) -> None:
        """Initialize base processor."""
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the provided data."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate the data before processing."""
        pass

    def format_output(self, result: Optional[str]) -> str:
        """Format the processor output."""
        if result is None:
            return "Output: No result"
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """Processor for numeric datasets."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Ensure data is a list of numbers."""
        try:
            if not isinstance(data, list):
                return False
            return all(isinstance(value, (int, float)) for value in data)
        except Exception:
            return False

    def process(self, data: Any) -> str:
        """Process numeric data and compute statistics."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            print("Validation: Numeric data verified")

            numbers: List[Union[int, float]] = data
            count: int = len(numbers)
            total: Union[int, float] = sum(numbers)
            average: float = total / count if count > 0 else 0.0

            return (
                f"Processed {count} numeric values, sum={total}, avg={average}"
            )

        except Exception as error:
            return f"Error processing numeric data: {error}"


class TextProcessor(DataProcessor):
    """Processor for textual datasets."""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Ensure data is a string."""
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """Analyze text data."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            print("Validation: Text data verified")

            text: str = data
            characters: int = len(text)
            words: List[str] = text.split()

            return (
                f"Processed text: {characters} characters, {len(words)} words"
            )

        except Exception as error:
            return f"Error processing text data: {error}"


class LogProcessor(DataProcessor):
    """Processor for system log entries."""

    def __init__(self) -> None:
        super().__init__()

        # Dictionary used to demonstrate Dict typing
        self.log_levels: Dict[str, str] = {
            "ERROR": "[ALERT]",
            "INFO": "[INFO]",
            "WARNING": "[WARNING]",
            "DEBUG": "[DEBUG]",
        }

    def validate(self, data: Any) -> bool:
        """Ensure log entry is text."""
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        """Interpret the log level and message."""
        try:
            if not self.validate(data):
                raise ValueError("Invalid log entry")

            print("Validation: Log entry verified")

            entry: str = data

            if ":" not in entry:
                return f"Log entry: {entry}"

            level, message = entry.split(":", 1)
            level = level.strip().upper()
            message = message.strip()

            tag: Optional[str] = self.log_levels.get(level)

            if tag is None:
                tag = f"[{level}]"

            return f"{tag} {level} level detected: {message}"

        except Exception as error:
            return f"Error processing log data: {error}"


def main() -> None:
    """Run the processor demonstration."""

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Individual processor demonstrations
    print("Initializing Numeric Processor...")
    numeric_processor: DataProcessor = NumericProcessor()

    numeric_data: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")

    numeric_result: str = numeric_processor.process(numeric_data)
    print(numeric_processor.format_output(numeric_result))
    print()

    print("Initializing Text Processor...")
    text_processor: DataProcessor = TextProcessor()

    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')

    text_result: str = text_processor.process(text_data)
    print(text_processor.format_output(text_result))
    print()

    print("Initializing Log Processor...")
    log_processor: DataProcessor = LogProcessor()

    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')

    log_result: str = log_processor.process(log_data)
    print(log_processor.format_output(log_result))
    print()

    # Polymorphic demonstration
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    datasets: List[Any] = [[1, 2, 3], "Hello World", "INFO: System ready"]

    results: List[str] = []

    for processor, dataset in zip(processors, datasets):
        result: str = processor.process(dataset)
        results.append(result)

    for index, result in enumerate(results, start=1):
        print(f"Result {index}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
