"""
Задача
Дан файл access.log, содержащий большой объем текста, в котором встречаются email-адреса.
Необходимо:
    - с помощью регулярных выражений вытащить оттуда все email-адреса,
    - подсчитать количество вхождений каждого домена почтового сервиса,
    - сохранить результат в json-файле result.json.
"""

import json
import os
import re
from collections import Counter


def count_emails(input_file: str, output_file: str):  # type: ignore
    with open(input_file) as access_file:
        data_from_file = access_file.read()

    pattern = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"
    email_list = re.findall(pattern, data_from_file)

    domains = Counter(item.split("@")[1] for item in email_list)

    result = {"total_count": len(email_list), "domains": {}}

    for domain, count in domains.items():
        domain_emails = [email for email in email_list if email.split("@")[1] == domain]

        result["domains"][domain] = {"count": count, "emails": domain_emails}  # type: ignore

    with open(output_file, "w") as of:
        json.dump(result, of, indent=4)


if __name__ == "__main__":

    current_dir = os.path.dirname(__file__)
    input_path = os.path.join(current_dir, "data_13_2_10", "access.log")
    output_path = os.path.join(current_dir, "data_13_2_10", "result.json")

    count_emails(input_file=input_path, output_file=output_path)
