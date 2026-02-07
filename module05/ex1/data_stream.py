#!/usr/bin/env python3
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.stream_type = "Generic"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "type": self.stream_type}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        valid_ops = [x for x in data_batch if isinstance(x, (int, float))]
        net_flow = sum(valid_ops)
        return (f"Transaction analysis: {len(valid_ops)} operations,"
                f"net flow: {net_flow}")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any]:
        if criteria == "high_value":
            return [x for x in data_batch if isinstance(x, (int, float)) and
                    abs(x) > 100]
        return data_batch


class SensorStream(DataStream):
    def __init__(self, stream_id) -> None:
        super().__init__(stream_id)
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        try:

            print("Initializing Sensor Stream...")

            if not data_batch:
                return f"Stream {self.stream_id}: No data to process"

            total: int = sum(data_batch)
            avarage: int = total / len(data_batch)

            return (f"Sensor analysis: {len(data_batch)} readings,"
                    f"avg: {avarage:.2f}")

        except TypeError:
            return "[ERROR] Invalid data types in sensor batch"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == "high_pass":
            return [x for x in data_batch if isinstance(x, Union(int, float))
                    and x > 20]

        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        events = [x for x in data_batch if isinstance(x, str)]
        errors = [e for e in events if "ERROR" in e or "error" in e]
        return (f"Event analysis: {len(events)} events, "
                f"{len(errors)} errors detected")


class StreamProcessor:
    def process_stream(self, stream: DataStream, data: List[Any]) -> None:
        print(f"--- Processing Stream: {stream.stream_id} ---")

        try:
            cleaned_data = stream.filter_data(data, criteria="clean")

            result = stream.process_batch(cleaned_data)

            print(f"Input items: {len(data)} -> "
                  f"Filtered items: {len(cleaned_data)}")
            print(f"Result: {result}")

        except Exception as e:
            print(f"[CRITICAL ERROR] Stream failed: {e}")


def main() -> None:
    processor = StreamProcessor()

    streams: List[DataStream] = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
    ]

    sensor_data: List[Any] = [22.5,
                              "errore_lettura",
                              23.0,
                              21.8,
                              None]
    trans_data: List[Any] = [100, -50, "hack_attempt", 200, -10]
    event_data: List[Any] = ["Login success",
                             "ERROR: Disk full",
                             "Logout",
                             404]

    all_data = [sensor_data,
                trans_data,
                event_data]

    for stream, data in zip(streams, all_data):
        processor.process_stream(stream, data)
        print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("\n=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    main()
    print()
