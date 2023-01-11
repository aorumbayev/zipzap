from datetime import datetime

from algosdk.v2client.indexer import IndexerClient
from imgmaker import imgmaker

indexer = IndexerClient(
    "",
    "https://algoindexer.algoexplorerapi.io",
    headers={"User-Agent": "algosdk"},
)

creation_round = indexer.asset_info(265122)["asset"]["created-at-round"]
unix_timestamp = indexer.block_info(creation_round)["timestamp"]
mint_time = datetime.fromtimestamp(unix_timestamp)
current_time = datetime.now()
delta = current_time - mint_time
title = f"{delta.days} days since minting"
subtitle = "Algorand Brazil Community Token"

i = imgmaker()

i.generate(
    "watermark",
    {
        "left_text": subtitle,
        "fa_icon": "fas fa-link",
        "brand_text": title,
        "background": "https://i.imgur.com/Z4IRwW7.png",
    },
)
