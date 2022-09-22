from abc import ABC, abstractmethod
import random
from typing import List

class Exchange(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass

class CoinBaseExchange(Exchange):

    def connect(self):
        print(f"Connecting to CoinBase Exchange ...")

    def get_market_data(self, coin:str) -> List[float]:
        print(f"Pulling {coin} data from coinbase...")
        data = [random.randint(10, 20) for _ in range(4)]
        print(data)
        return data

class BitConnectExchange(Exchange):

    def connect(self):
        print(f"Connecting to BitConnect Exchange ...")

    def get_market_data(self, coin:str) -> List[float]:
        print(f"Pulling {coin} data from coinbase...")
        data = [random.randint(10, 20) for _ in range(4)]
        print(data)
        return data

class TradingBot(ABC):

    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)

        if should_buy:
            print(f"You sould buy {coin}")
        elif should_sell:
            print(f"you should sell {coin}")
        else:
            print(f"You should hold {coin}")

class MinMaxTradingBot(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] <= min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] >= max(prices)

class AverageTradeingBot(TradingBot):

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)


app = MinMaxTradingBot(BitConnectExchange())
app.check_prices("BTC/USD")

app2 = AverageTradeingBot(CoinBaseExchange())
app2.check_prices("ETH/USD")