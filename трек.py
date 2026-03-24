import csv
import sys

time_zalupa = []
slovar = ["date", "category", "price", "comment"]
trati = []
def start():
    with open("tati.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["price"] = int(row["price"])
            trati.append(row)
def save(trati):
    with open("tati.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=slovar
        )
        writer.writeheader()
        writer.writerows(trati)
        print("Success")
def zapisi(data):
    for i, stroka in enumerate(data, start=1):
        print(i, stroka["date"], stroka["category"], stroka["price"], stroka["comment"])

def __main__():
    start()
    while True:
        try:
            z = int(input("1-add, 2-show_trati, 3-sum, 4-del, 5-edit, 6-find, 0 - exit"))
            if z == 1:
                    expense = {
                        "date": input("Введите дату"),
                        "category": input("category?"),
                        "price": int(input("price?")),
                        "comment": input("comment?")
                    }
                    if all(expense.values()):
                        trati.append(expense)
                        save(trati)
                    else:
                        print("ne v add")
            elif z == 0:
                print("Bye bye")
                sys.exit()
            elif not trati:
                print("pysto")
            elif z == 2:
                zapisi(trati)
                sort = input("Сортируем?, y/n")
                if sort == "y":
                    za = int(input(str(slovar)))
                    key = slovar[za - 1]
                    zz = sorted(trati, key=lambda k: k[key], reverse=True)
                    zapisi(zz)


            elif z == 4:
                zapisi(trati)
                to_delete = int(input("какую запись хотите удалить?")) -1
                if to_delete in range(0, len(trati)):

                    zapisi([trati[to_delete]])

                    if input("y/n") == "y":
                        del trati[to_delete]
                        save(trati)
                    else:
                        print("Хорошо")
                else:
                    print("ne v delete")
            elif z == 5:
                zapisi(trati)
                to_edit = int(input("какую запись изменить?")) -1
                if to_edit in range(0, len(trati)):
                    a = trati[to_edit]
                    row_to_edit = int(input("какой столбик хотите изменить? 1 - date 2 - category 3 - price 4 - comment")) -1
                    key = slovar[row_to_edit]
                    a[key] = int(input("На что?"))
                    save(trati)
            elif z == 6:
                type_search = int(input("Поиск по 1-дате, 2-категории"))
                if type_search == 2:
                    search_row = input("Что ищем?")
                    for finding in trati:
                        if finding["category"] == search_row:
                            time_zalupa.append(finding)

                elif type_search == 1:
                    search_row = input("Какую дату ищем?")
                    for finding in trati:
                            if finding["date"] == search_row:
                                time_zalupa.append(finding)
                zapisi(time_zalupa)
                time_zalupa.clear()
            elif z == 3:
                category_find = int(input("категорически - 1, общий - 2"))
                if category_find == 2:
                    print(sum(expense["price"] for expense in trati))
                elif category_find == 1:
                    search_row = input("Что сыщим?")
                    for finding in trati:
                        if finding["category"] == search_row:
                            time_zalupa.append(finding)
                    print(sum(expense["price"] for expense in time_zalupa))
                time_zalupa.clear()

            elif z == 7:
                zapisi(time_zalupa)

        except ValueError:
            print("error")

__main__()


