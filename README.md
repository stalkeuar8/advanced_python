☕ Smart Cafe AI Bot

A feature-rich Telegram Bot simulating a modern coffee shop ordering system. The project integrates Machine Learning to predict order waiting times based on real-world factors and features a modular architecture for seamless payment system integration.
🚀 Key Features

    Dynamic Menu & Catalog: Interactive browsing of coffee types and size variants.

    Smart Cart System: Fully functional shopping cart with item limits (max 6), total price calculation, and bulk purchasing.

    AI-Powered Time Prediction: Integrated ML model that estimates preparation time based on current cafe load.

    Non-blocking Architecture: Uses asynchronous handlers and threaded database operations for high performance.

    Robust Logging: Detailed logging system separating sales, payments, cart actions, and system errors using loguru.

🧠 Machine Learning Module (The "Brain")

Unlike standard bots that show static "cooking time," this project uses a trained Machine Learning model (RandomForest / LinearRegression) to calculate realistic wait times.
How it works:

The predict_time engine analyzes multiple dynamic factors before confirming the order:

    Time Context: Splits the day into Morning, Lunchtime, and Evening shifts to estimate crowd levels.

    Day of Week: Accounts for weekend vs. workday traffic.

    Resource Availability: Considers the number of active coffee machines (Coffee maker qty).

    Product Complexity: Different coffee variants require different preparation times.

Optimization: The model (.pkl file) is loaded into memory once upon startup (Singleton pattern), ensuring instant predictions without disk I/O latency during high loads.
💳 Payment Architecture (Mock System)

The bot implements a modular payment interface designed for flexibility.

Currently, the bot demonstrates a "Mock Payment Validator":

    Validation Logic: Users confirm payment by sending a specific emoji (💋) a required number of times.

    Why this approach? Since this is a portfolio project without a legal entity, real banking APIs are not connected.

    Scalability: The validation logic is isolated in the payment_validator function and FSM flow. To connect Stripe, LiqPay, or WayForPay, you only need to replace the validation condition with an API call. The rest of the bot's logic (DB recording, ML prediction, receipt generation) remains unchanged.

🛠 Tech Stack

    Core: Python 3.10+

    Framework: aiogram 3.x (Asynchronous Telegram Bot API)

    Database: SQLite (with asyncio.to_thread for non-blocking I/O)

    Data Science: pandas, scikit-learn, joblib

    Logging: loguru

    Config: python-dotenv
