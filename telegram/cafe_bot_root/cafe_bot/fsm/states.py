from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.callback_data import CallbackData

class ValidatePayment(StatesGroup):
    paying_currency = State()




