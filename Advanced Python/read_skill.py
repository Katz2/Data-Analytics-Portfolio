import csv

with open("skills.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        scores = {
            "python": int(row["python"]),
            "sql": int(row["sql"]),
            "excel": int(row["excel"])
        }

        total = sum(scores.values())
        average = total / len(scores)

        print(f"{row['name']} → Total: {total}, Avg: {average:.2f}")
