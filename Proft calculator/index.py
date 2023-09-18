def profit(manifest): return round((manifest["sell_price"] - manifest["cost_price"]) * manifest["inventory"], 0)



print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))