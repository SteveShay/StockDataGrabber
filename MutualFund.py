from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class MutualFund:
    symbol: str
    date: str
    securityType: str
    longName: str
    currentPrice: float
    previousClose: float
    oneDayDirection: str