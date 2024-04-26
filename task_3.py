import re 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern = r"^\+|38|[a-zA-Z;,\-:!\.\\()\s\+]"
    replacement = ""
    modified_number = re.sub(pattern, replacement, phone_number)
    modified_number = f"+38{modified_number}"
    return modified_number
    print(modified_number)  

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
