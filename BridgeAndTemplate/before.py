import random
from typing import List

class Application:

    def __init__(self, trading_strategy = "greedy") -> None:
        self.trading_strategy = trading_strategy

    def connect(self):
        print(f"Connecting to Cryto Exchange ...")

    def get_market_data(self, coin:str) -> List[float]:
        return [random.randint(10, 20) for _ in range(4)]

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] <= min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        if self.trading_strategy == "minmax":
            return prices[-1] >= max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)

        if should_buy:
            print(f"You sould buy {coin}")
        elif should_sell:
            print(f"you should sell {coin}")
        else:
            print(f"You should hold {coin}")



app = Application("minmax")
app.check_prices("BTC/USD")
app.check_prices("ETH/USD")