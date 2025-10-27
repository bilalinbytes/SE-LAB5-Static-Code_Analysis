"""Inventory System - Cleaned and Secure Version
Implements static analysis improvements: type checks, logging,
safe file handling, and PEP8 compliance.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def add_item(stock_data, item, qty, logs=None):
    """Add quantity to a specific item."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid types for item or quantity: %s, %s", item, qty
        )
        return stock_data

    stock_data[item] = stock_data.get(item, 0) + qty
    log_entry = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_entry)
    logging.info("Added %d of %s", qty, item)
    return stock_data


def remove_item(stock_data, item, qty):
    """Remove quantity from a specific item."""
    try:
        if not isinstance(item, str) or not isinstance(qty, (int, float)):
            logging.warning("Invalid input types for remove_item.")
            return stock_data

        if item not in stock_data:
            logging.warning("Tried to remove non-existent item: %s", item)
            return stock_data

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)
    except KeyError:
        logging.error("KeyError occurred while removing item: %s", item)
    return stock_data


def get_qty(stock_data, item):
    """Get the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load stock data from a JSON file safely."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            stock_data = json.load(file)
        logging.info("Inventory loaded successfully from %s", file_path)
        return stock_data
    except FileNotFoundError:
        logging.warning("Inventory file not found, creating new one.")
        return {}
    except json.JSONDecodeError:
        logging.error("JSON decode error — corrupted file.")
        return {}


def save_data(stock_data, file_path="inventory.json"):
    """Save current stock data to a JSON file."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(stock_data, file, indent=4)
        logging.info("Inventory saved successfully to %s", file_path)
    except (OSError, TypeError) as error:
        logging.error("Error saving data: %s", error)


def print_data(stock_data):
    """Print all stock items and quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return a list of items with quantity below the threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main execution flow for inventory management."""
    stock_data = {}

    stock_data = add_item(stock_data, "apple", 10)
    stock_data = add_item(stock_data, "banana", 3)
    stock_data = remove_item(stock_data, "apple", 2)
    stock_data = remove_item(stock_data, "orange", 1)

    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))

    save_data(stock_data)
    stock_data = load_data()

    print_data(stock_data)


if __name__ == "__main__":
    main()
