from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ETF:
    symbol: str
    date: str
    securityType: str
    longName: str
    currentPrice: float
    previousClose: float
    oneDayDirection: str
    fiftyTwoWeekHigh: float
    fiftyTwoWeekLow: float
    percentHigh: float
    percentLow: float
    yieldStatus: bool
    yearlyRate: float
    yearlyYield: float
