from hummingbot.strategy.script_strategy_base import ScriptStrategyBase

class MyStrategy(ScriptStrategyBase):
    markets = {
        "binance_paper_trade": {"ETH-USDT"},
        "kucoin_paper_trade": {"ETH-USDT"}
    }

    def on_tick(self):
        for connector_name, connector in self.connectors.items():
            self.logger().info(f"Current price on {connector_name}: {connector.get_mid_price('ETH-USDT')}")
