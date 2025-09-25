import yaml
from bot.config_validator import validate_config

def _lower_keys(d):
    if isinstance(d, dict):
        return {str(k).lower(): _lower_keys(v) for k, v in d.items()}
    if isinstance(d, list):
        return [_lower_keys(x) for x in d]
    return d

def load_config(path="config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    cfg = _lower_keys(raw or {})
    cfg.setdefault("mode","paper")
    cfg.setdefault("symbols", ["BTC/USDT:USDT","ETH/USDT:USDT"])
    return validate_config(cfg)
