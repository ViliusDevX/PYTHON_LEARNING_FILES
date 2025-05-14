# Assuming the 'My_item' class exists and can take 'text' as an argument
class My_item:
    def __init__(self, text):
        self.text = text

# Your initial list of items
items = [
    '1. Software developer - 90%',
    '2. games developer - 50%',
    '3. doctor - 10%'
]

# Creating a new list of My_item objects
new_items = []
for item in items:
    # Splitting each item by '-' to get the text before the '-'
    text = item.split('-')[0].strip()
    new_items.append(My_item(text=text))

# Displaying the new list of My_item objects
for idx, item in enumerate(new_items):
    print(f"My_item {idx + 1}: {item.text}")
