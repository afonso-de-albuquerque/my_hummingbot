from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

class MyStrategy(ScriptStrategyBase):
    markets = { "binance_paper_trading": {"ETH-USDT"},
                "coinbase_pro_paper_trading": {"ETH-USDT"},
                "huobi_paper_trading": {"ETH-USDT"}}
    def __init__(self):
        super().__init__()

    def on_tick(self):
        for connector_name, connector in self.connectors.items():
            self.logger().info(f"Current price on {connector_name}: {connector.get_price()}")

