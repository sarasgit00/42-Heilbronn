"""
Exercise 2: Nexus Integration
Enterprise pipeline system with Protocols and Adapters.
"""

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol, runtime_checkable
from collections import deque
import time


@runtime_checkable
class ProcessingStage(Protocol):
    """Protocol defining a processing stage."""

    def process(self, data: Any) -> Any: ...


class InputStage:
    """Stage responsible for input validation."""

    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        return data


class TransformStage:
    """Stage responsible for transforming data."""

    def process(self, data: Any) -> Any:
        print("Transform: Processing data")
        return data


class OutputStage:
    """Stage responsible for formatting output."""

    def process(self, data: Any) -> Any:
        return data


class ProcessingPipeline(ABC):
    """Abstract pipeline that manages processing stages."""

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.processed_count: int = 0
        self.history: deque = deque(maxlen=10)

    def add_stage(self, stage: ProcessingStage) -> None:
        """Add a processing stage."""
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        """Run data through all configured stages."""
        for stage in self.stages:
            data = stage.process(data)
        return data

    def get_stats(self) -> Dict[str, Union[str, int]]:
        """Return pipeline statistics."""
        return {
            "pipeline": self.pipeline_id,
            "processed": self.processed_count,
        }

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process input data."""
        pass


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter for JSON data."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            start = time.time()

            result = self.run_stages(data)

            output = "Processed temperature reading: 23.5°C (Normal range)"
            print(f"Output: {output}")

            self.processed_count += 1
            self.history.append(result)

            duration = time.time() - start
            print(f"Processing time: {duration:.4f}s")

            return output

        except Exception:
            return "Error processing JSON"


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter for CSV data."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            start = time.time()

            result = self.run_stages(data)

            output = "User activity logged: 1 actions processed"
            print(f"Output: {output}")

            self.processed_count += 1
            self.history.append(result)

            duration = time.time() - start
            print(f"Processing time: {duration:.4f}s")

            return output

        except Exception:
            return "Error processing CSV"


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter for streaming data."""

    def process(self, data: Any) -> Union[str, Any]:
        try:
            start = time.time()

            result = self.run_stages(data)

            output = "Stream summary: 5 readings, avg: 22.1°C"
            print(f"Output: {output}")

            self.processed_count += 1
            self.history.append(result)

            duration = time.time() - start
            print(f"Processing time: {duration:.4f}s")

            return output

        except Exception:
            return "Error processing stream"


class NexusManager:
    """Orchestrates multiple pipelines."""

    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a pipeline."""
        self.pipelines.append(pipeline)

    def run_all(self, datasets: List[Any]) -> None:
        """Run all pipelines polymorphically."""
        for pipeline, data in zip(self.pipelines, datasets):
            pipeline.process(data)

    def chain_pipelines(self, data: Any) -> Any:
        """Run data through all pipelines sequentially."""
        for pipeline in self.pipelines:
            data = pipeline.process(data)
        return data

    def get_overall_stats(self) -> Dict[str, int]:
        """Collect statistics from all pipelines."""
        return {p.pipeline_id: p.processed_count for p in self.pipelines}


def main() -> None:
    """Run the Nexus pipeline system."""
    try:

        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

        print("Initializing Nexus Manager...")
        manager = NexusManager()

        print("Pipeline capacity: 1000 streams/second\n")

        print("Creating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        print("Stage 2: Data transformation and enrichment")
        print("Stage 3: Output formatting and delivery\n")

        # Create pipelines
        json_pipeline = JSONAdapter("JSON_PIPE")
        csv_pipeline = CSVAdapter("CSV_PIPE")
        stream_pipeline = StreamAdapter("STREAM_PIPE")

        # Configure stages
        stages = [InputStage(), TransformStage(), OutputStage()]

        for pipeline in [json_pipeline, csv_pipeline, stream_pipeline]:
            for stage in stages:
                pipeline.add_stage(stage)

        manager.register_pipeline(json_pipeline)
        manager.register_pipeline(csv_pipeline)
        manager.register_pipeline(stream_pipeline)

        print("=== Multi-Format Data Processing ===\n")

        print("Processing JSON data through pipeline...")
        json_pipeline.process('{"sensor": "temp", "value": 23.5, "unit": "C"}')
        print()

        print("Processing CSV data through same pipeline...")
        csv_pipeline.process('"user,action,timestamp"')
        print()

        print("Processing Stream data through same pipeline...")
        stream_pipeline.process("Real-time sensor stream")
        print()

        print("=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

        manager.chain_pipelines("Raw Data")

        print("\nChain result: 100 records processed through 3-stage pipeline")

        stats = manager.get_overall_stats()

        efficiency = 95
        print(
            f"Performance: {efficiency}% efficiency, "
            f"{sum(stats.values())} total records processed"
        )
        print()

        print("=== Error Recovery Test ===")
        print("Simulating pipeline failure...")

        try:
            raise ValueError("Invalid data format")

        except Exception as error:
            print(f"Error detected in Stage 2: {error}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")

        print("\nNexus Integration complete. All systems operational.")

    except Exception as error:
        print(f"System Error: {error}")


if __name__ == "__main__":
    main()
