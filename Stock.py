from dataclasses import dataclass
from dataclasses_json import dataclass_json
from decimal import Decimal

@dataclass_json
@dataclass
class Stock:
    symbol: str
    date: str
    securityType: str
    longName: str
    sector: str
    industry: str
    currentPrice: float
    previousClose: float
    oneDayDirection: str
    fiftyTwoWeekHigh: float
    fiftyTwoWeekLow: float
    percentHigh: float
    percentLow: float
    dividendStatus: bool
    exDivDate: str
    divRate: float
    divYield: float
    debtToEquity: float
    trailingEPS: float
    forwardEPS: float
    epsGrowth: float
    trailingPE: float
    forwardPE: float
    peGrowth: float