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
            temps = []
            for item in data_batch:
                if isinstance(item, str) and item.startswith("temp:"):
                    temp_val = float(item.split(":")[1])
                    if temp_val > 20:
                        temps.append(temp_val)
            return temps
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
            values = []
            for item in data_batch:
                if isinstance(item, str) and ":" in item:
                    op, val = item.split(":")
                    val = int(val)
                    if abs(val) > 100:
                        values.append(val)
            return values
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
        sensor_stream = None
        trans_stream = None

        for stream, data in zip(streams, data_batches):
            if isinstance(stream, SensorStream):
                sensor_data.extend(data)
                sensor_stream = stream
            elif isinstance(stream, TransactionStream):
                trans_data.extend(data)
                trans_stream = stream
            elif isinstance(stream, EventStream):
                event_data.extend(data)

        print(f"- Sensor Data: {len(sensor_data)} reading processes")
        print(f"- Transaction Data: {len(trans_data)} operations processed")
        print(f"- Event Data: {len(event_data)} events processed")

        print()

        large_trans_count = 0
        critical_sensor_count = 0
        if sensor_stream:
            critical_sensor_count = len(sensor_stream.filter_data(sensor_data,
                                                                  "high_pass"))
        if trans_stream:
            large_trans_count = len(trans_stream.filter_data(trans_data,
                                                             "high_value"))
        print("Stream filtering active: High-priority data only")
        print("Filtered Results: "
              f"{critical_sensor_count} critical sensor alerts, "
              f"{large_trans_count} large transactions")


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

    new_sensor_data = ["temp:25.0", "temp:30.5", "temp:18.0",
                       "humidity:70", "humidity:60", "humidity:55",
                       "pressure:1010", "pressure:1020", "pressure:1005"]
    new_trans_data = ["buy:200", "sell:50", "buy:300", "sell:400", "buy:150"]
    new_event_data = ["startup", "error:disk full", "shutdown",
                      "error:network"]

    streams = [(sensor, new_sensor_data),
               (trans, new_trans_data),
               (event, new_event_data)]
    StreamProcessor().process_multiple_streams([s[0] for s in streams],
                                               [s[1] for s in streams])

    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("\n=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    main()
    print()
