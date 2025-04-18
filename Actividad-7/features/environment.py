from src.belly import Belly
from unittest.mock import MagicMock

def before_scenario(context, scenario):
    # Puedes usar el clock mockeado si deseas (opcional)
    fake_clock = MagicMock()
    context.belly = Belly(clock_service=fake_clock)
    context.exception = None