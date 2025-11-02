"""Inventory System - Cleaned version after static analysis."""

import json
import logging
from datetime import datetime


# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def add_item(item="default", qty=0, logs=None, stock_data=None):
    """Add an item to the inventory."""
    if logs is None:
        logs = []
    if stock_data is None:
        stock_data = {}

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid item or quantity type.")
        return stock_data, logs

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    return stock_data, logs


def remove_item(stock_data, item, qty):
    """Remove a given quantity of an item."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.error("Item not found: %s", e)
    return stock_data


def get_qty(stock_data, item):
    """Return quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        return stock_data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error("Error loading file: %s", e)
        return {}


def save_data(stock_data, file="inventory.json"):
    """Save inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f)
        logging.info("Inventory saved successfully.")
    except Exception as e:
        logging.error("Error saving file: %s", e)


def print_data(stock_data):
    """Print the inventory data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(stock_data, threshold=5):
    """Return items below threshold quantity."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program entry point."""
    stock_data = {}
    logs = []

    stock_data, logs = add_item("apple", 10, logs, stock_data)
    stock_data, logs = add_item("banana", 2, logs, stock_data)
    stock_data = remove_item(stock_data, "apple", 3)
    stock_data = remove_item(stock_data, "orange", 1)

    print(f"Apple stock: {get_qty(stock_data, 'apple')}")
    print(f"Low items: {check_low_items(stock_data)}")
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)


if __name__ == "__main__":
    main()
