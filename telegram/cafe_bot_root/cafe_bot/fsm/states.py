from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.callback_data import CallbackData

class ValidatePayment(StatesGroup):
    paying_currency = State()

class PaymentMenuCB(CallbackData, prefix='payment menu'):
    variant_id: int
    paying_currency_amount: int



