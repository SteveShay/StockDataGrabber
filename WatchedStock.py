from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class WatchedStock:
    symbol: str
    shares: float
    cost_basis: float