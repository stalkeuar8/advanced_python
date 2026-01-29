from dataclasses import dataclass, field

@dataclass(frozen=True, order=True)
class ModelConfig:

    learning_rate: float
    batch_size: int
    optimizer: str

config1 = ModelConfig(1.0, 1, '111')
config2 = ModelConfig(1.0, 1, '111')

print(config1 == config2)
print(config1 is config2)