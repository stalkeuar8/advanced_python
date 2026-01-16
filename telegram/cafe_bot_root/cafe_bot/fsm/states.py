from aiogram.fsm import StatesGroup, State
from aiogram.filters.callback_data import CallbackData

class PayingProcess(StatesGroup, CallbackData):
    paying_currency = State()
    paying_currency_type: str = "💋"
    paying_currency_amount: int



