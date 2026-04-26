"""
Exercise 1: Polymorphic Streams
Advanced polymorphic system handling mixed data types.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Default filtering (returns all data)."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics."""
        return {
            "id": self.stream_id,
            "processed": self.processed_count
        }


class SensorStream(DataStream):
    """Handles environmental sensor data."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing sensor batch: {data_batch}")

            numbers: List[Union[int, float]] = [
                x for x in data_batch if isinstance(x, (int, float))
            ]

            self.processed_count += len(numbers)

            avg: float = sum(numbers) / len(numbers) if numbers else 0.0

            return (
                f"Sensor analysis: {len(numbers)} readings processed, "
                f"avg temp: {avg}°C"
            )

        except Exception as error:
            return f"Sensor processing error: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter high-priority sensor alerts."""
        if criteria == "High-priority":
            return [x for x in data_batch
                    if isinstance(x, (int, float)) and x > 30]
        return data_batch


class TransactionStream(DataStream):
    """Handles financial transactions."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing transaction batch: {data_batch}")

            net_flow: int = 0
            operations: int = 0

            for item in data_batch:
                if isinstance(item, dict):
                    operations += 1

                    if "buy" in item:
                        net_flow -= item["buy"]

                    if "sell" in item:
                        net_flow += item["sell"]

            self.processed_count += operations

            return (
                f"Transaction analysis: {operations} operations, "
                f"net flow: +{net_flow} units"
            )

        except Exception as error:
            return f"Transaction processing error: {error}"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter large financial transactions."""
        if criteria == "Critical":
            return [
                x for x in data_batch
                if isinstance(x, dict)
                and (x.get("buy", 0) > 100 or x.get("sell", 0) > 100)
            ]
        return data_batch


class EventStream(DataStream):
    """Handles system events."""

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing event batch: {data_batch}")

            events: List[str] = [
                x for x in data_batch if isinstance(x, str)
            ]

            errors: int = events.count("error")

            self.processed_count += len(events)

            return (
                f"Event analysis: {len(events)} events, "
                f"{errors} error detected"
            )

        except Exception as error:
            return f"Event processing error: {error}"


class StreamProcessor:
    """Manages multiple streams polymorphically."""

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        """Register a stream."""
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:
        """Process all streams through the same interface."""
        try:
            print("=== Polymorphic Stream Processing ===")
            print("Processing mixed stream types through unified interface...")
            print("Batch 1 Results:")

            for stream, batch in zip(self.streams, batches):

                filtered: List[Any] = stream.filter_data(batch)

                stream.process_batch(filtered)

                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {len(filtered)} readings processed")

                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: {len(filtered)} "
                          "operations processed")

                elif isinstance(stream, EventStream):
                    print(f"- Event data: {len(filtered)} events processed")

            print()

        except Exception as error:
            print(f"Stream processing error: {error}")


def main() -> None:
    """Run the polymorphic stream system."""

    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

        # Initialize streams
        print("Initializing Sensor Stream...")
        print("Stream ID: SENSOR_001, Type: Environmental Data")

        sensor = SensorStream("SENSOR_001")

        print(sensor.process_batch([22.5, 22.5, 22.5]))
        print()

        print("Initializing Transaction Stream...")
        print("Stream ID: TRANS_001, Type: Financial Data")

        transaction = TransactionStream("TRANS_001")

        print(transaction.process_batch([
            {"buy": 100},
            {"sell": 150},
            {"buy": 75}
        ]))
        print()

        print("Initializing Event Stream...")
        print("Stream ID: EVENT_001, Type: System Events")

        event = EventStream("EVENT_001")

        print(event.process_batch(["login", "error", "logout"]))
        print()

        # Create stream manager
        processor = StreamProcessor()

        processor.add_stream(sensor)
        processor.add_stream(transaction)
        processor.add_stream(event)

        # Batch processing
        batches: List[List[Any]] = [
            [60, 22, 55],  # sensor
            [{"buy": 50}, {"sell": 200}, {"buy": 20}, {"sell": 10}],
            ["login", "error", "logout"]  # event
        ]

        processor.process_all(batches)

        print("Stream filtering active: High-priority data only")

        filtered_sensor = sensor.filter_data(batches[0], "High-priority")
        filtered_transactions = transaction.filter_data(batches[1], "Critical")

        print(
            f"Filtered results: {len(filtered_sensor)} critical sensor alerts,"
            f" {len(filtered_transactions)} large transaction"
        )
        print()

        print("All streams processed successfully. Nexus throughput optimal.")

    except Exception as error:
        print(f"System Error: {error}")


if __name__ == "__main__":
    main()
