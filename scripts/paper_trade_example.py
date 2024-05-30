import pandas as pd

from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


class MyStrategy(ScriptStrategyBase):
    markets = {
        "binance_paper_trade": {"ETH-USDT"},
        "kucoin_paper_trade": {"ETH-USDT"},
        "gate_io_paper_trade": {"ETH-USDT"}
    }

    def format_status(self) -> str:
        """
        Returns status of the current strategy on user balances and current active orders. This function is called
        when status command is issued. Override this function to create custom status display output.
        """
        if not self.ready_to_trade:
            return "Market connectors are not ready."
        lines = []
        warning_lines = []
        warning_lines.extend(self.network_warning(self.get_market_trading_pair_tuples()))

        balance_df = self.get_balance_df()
        lines.extend(["", "  Balances:"] + ["    " + line for line in balance_df.to_string(index=False).split("\n")])
        prices_df = self.get_prices_df()
        lines.extend(["", "  Prices:"] + ["    " + line for line in prices_df.to_string(index=False).split("\n")])

        try:
            df = self.active_orders_df()
            lines.extend(["", "  Orders:"] + ["    " + line for line in df.to_string(index=False).split("\n")])
        except ValueError:
            lines.extend(["", "  No active maker orders."])

        warning_lines.extend(self.balance_warning(self.get_market_trading_pair_tuples()))
        if len(warning_lines) > 0:
            lines.extend(["", "*** WARNINGS ***"] + warning_lines)
        return "\n".join(lines)

    def get_prices_df(self) -> pd.DataFrame:
        """
        Returns a DataFrame containing the latest price of all trading pairs.
        """
        prices_df = self.market_status_data_frame(self.get_market_trading_pair_tuples())
        return prices_df
