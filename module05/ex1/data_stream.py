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


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        temps = []
        for item in data_batch:
            if isinstance(item, str) and item.startswith("temp:"):
                temps.append(float(item.split(":")[1]))
        avg_temp = sum(temps) / len(temps) if temps else 0
        return (f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria == "high_pass":
            return [x for x in data_batch if isinstance(x, (int, float))
                    and x > 20]
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        net_flow = 0
        count = 0
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                op, val = item.split(":")
                val = int(val)
                if op == "buy":
                    net_flow += val
                elif op == "sell":
                    net_flow -= val
                count += 1
        sign = "+" if net_flow >= 0 else ""
        return (f"Transaction analysis: {count} operations, "
                f"net flow: {sign}{net_flow} units")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] =
                    None) -> List[Any]:
        if criteria == "high_value":
            return [x for x in data_batch if isinstance(x, (int, float)) and
                    abs(x) > 100]
        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        events = [x for x in data_batch if isinstance(x, str)]
        errors = [e for e in events if "error" in e.lower()]
        return (f"Event analysis: {len(events)} events, "
                f"{len(errors)} error detected")


class StreamProcessor:
    def process_stream(self, stream: DataStream, data: List[Any]) -> None:
        try:
            print(f"Initializing {stream.stream_type.split()[0]} Stream...")
            print(f"Stream ID: {stream.stream_id}, Type: {stream.stream_type}")
            print("Processing "
                  f"{stream.stream_type.split()[0].lower()}"
                  f"batch: [{', '.join(data)}]")
            result = stream.process_batch(data)
            print(result)

        except Exception as e:
            print(f"[CRITICAL ERROR] Stream failed: {e}")

    def process_multiple_streams(self, streams: List[DataStream],
                                 data_batches: List[List[Any]]) -> None:
        sensor_data = []
        trans_data = []
        event_data = []

        for stream, data in zip(streams, data_batches):
            if isinstance(stream, SensorStream):
                sensor_data.append(data)
            elif isinstance(stream, TransactionStream):
                trans_data.append(data)
            elif isinstance(stream, EventStream):
                event_data.append(data)

        print(f"- Sensor Data: {len(sensor_data)} reading processes")
        print(f"- Transaction Data: {len(trans_data)} operations processed")
        print(f"- Event Data: {len(event_data)} events processed")

        print()

        critical_sensor = [for batch in streams if batch.filter_data(data, "high_pass")]
        print("Stream filtering active: High-priority data only")



def main() -> None:
    sensor = SensorStream("SENSOR_001")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    StreamProcessor().process_stream(sensor, sensor_data)

    print()

    trans = TransactionStream("TRANS_001")
    trans_data = ["buy:100", "sell:150", "buy:75"]
    StreamProcessor().process_stream(trans, trans_data)

    print()

    event = EventStream("EVENT_001")
    event_data = ["login", "error", "logout"]
    StreamProcessor().process_stream(event, event_data)

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print()

    streams = [(sensor, sensor_data),
               (trans, trans_data),
               (event, event_data)]
    StreamProcessor().process_multiple_streams([s[0] for s in streams],
                                               [s[1] for s in streams])


if __name__ == "__main__":
    print("\n=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    main()
    print()
