from typing import Any, List, Optional, Dict, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self._precs_cont: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """"""
        if criteria is None:  # no filter
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self._precs_cont
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        print("\nInitializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        formatted: str = "[" + ", ".join(
            f"{k}:{v}" for item in data_batch for k, v in item.items()
        ) + "]"
        print(f"Processing sensor batch: {formatted}")
        temps: List[float] = [item["temp"] for item in data_batch]
        avg_temp: float = sum(temps) / len(temps)
        num_readings: int = sum(len(item) for item in data_batch)
        self._precs_cont += num_readings
        result: str = (f"Sensor analysis: {num_readings} "
                       f"readings processed, avg temp: {avg_temp:.1f}°C")
        print(result)
        return result

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return [
            item for item in data_batch
            if item["temp"] > 50 or item["temp"] < -10
        ]


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Dict[str, Any]]) -> str:
        formatted: str = "[" + ", ".join(
            f"{tx['type']}:{tx['amount']}" for tx in data_batch
        ) + "]"
        print(f"Processing transaction batch: {formatted}")
        net_flow: float = 0.0
        for tx in data_batch:
            if tx["type"] == "buy":
                net_flow += float(tx["amount"])
            elif tx["type"] == "sell":
                net_flow -= float(tx["amount"])
        self._precs_cont = len(data_batch)
        result: str = (f"Transaction analysis: {len(data_batch)} operations,"
                       f" net flow: {net_flow:+.0f} units")
        print(result)
        return result

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return [tx for tx in data_batch if float(tx["amount"]) > 100]


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        print("\nInitializing Event Stream...")
        print(
            f"Stream ID: {self.stream_id}, "
            f"Type: {self.stream_type}"
        )

    def process_batch(self, data_batch: List[str]) -> str:
        formatted: str = "[" + ", ".join(data_batch) + "]"
        print(f"Processing event batch: {formatted}")
        error_cont: int = data_batch.count("error")
        self._precs_cont += len(data_batch)
        result: str = (
            f"Event analysis: {len(data_batch)} events, "
            f"{error_cont} error detected"
        )
        print(result)
        return result


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_map: Dict[str, List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("\nBatch 1 Results:")
        for stream in self.streams:
            batch: List[Any] = data_map.get(stream.stream_id, [])
            if isinstance(stream, SensorStream):
                readings: int = sum(len(item) for item in batch)
                print(f"- Sensor data: {readings} readings processed")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")

    def filter_all(
        self, data_map: Dict[str, List[Any]]
    ) -> Dict[str, List[Any]]:
        print("\nStream filtering active: High-priority data only")
        results: Dict[str, List[Any]] = {}
        critical_sensors: int = 0
        large_transactions: int = 0
        for stream in self.streams:
            batch: List[Any] = data_map.get(stream.stream_id, [])
            filtered: List[Any] = stream.filter_data(batch)
            results[stream.stream_id] = filtered
            if isinstance(stream, SensorStream):
                critical_sensors = len(filtered)
            elif isinstance(stream, TransactionStream):
                large_transactions = len(filtered)
        print(
            "Filtered results: "
            f"{critical_sensors} critical sensor alerts, "
            f"{large_transactions} large transaction"
        )
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor_data: List[Dict[str, float]] = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013}
    ]
    transaction_data: List[Dict[str, Any]] = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]
    event_data: List[str] = ["login", "error", "logout"]

    sensor: SensorStream = SensorStream("SENSOR_001")
    sensor.process_batch(sensor_data)

    transaction: TransactionStream = TransactionStream("TRANS_001")
    transaction.process_batch(transaction_data)

    event: EventStream = EventStream("EVENT_001")
    event.process_batch(event_data)

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)
    # Batch 1 data for polymorphic processing
    batch1_data: Dict[str, List[Any]] = {
        "SENSOR_001": [{"temp": 55.0}, {"temp": -15.0}],
        "TRANS_001": [{"type": "buy", "amount": 50},
                      {"type": "sell", "amount": 60},
                      {"type": "buy", "amount": 70},
                      {"type": "sell", "amount": 150}],
        "EVENT_001": ["start", "process", "end"]
    }
    processor.process_all(batch1_data)
    processor.filter_all(batch1_data)
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
