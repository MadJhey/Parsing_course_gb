from pymongo import MongoClient
from pprint import pprint
from pymongo import MongoClient

def load_data(update):
    import task1

    client = MongoClient('127.0.0.1', 27017)
    db = client['vacancies']
    vacs = db.vacancies
    if update:
        for vac in task1.main():  # 1, 3 задание - записываем только новые записи в базу
            vacs.update_one(vac, {'$set': vac}, upsert=True)

    # vacs.delete_many({})
    return vacs


def find_vac(vacs, salary):

    query = {'$or': [{"min": {"$gte": salary}}, {'max': {'$gte': salary}}]}
    for vac in vacs.find(query):
        pprint(vac)


def main():
    update = False
    vacs = load_data(update)
    salary = 150000
    find_vac(vacs, salary)


if __name__ == "__main__":
    main()
