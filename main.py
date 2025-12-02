class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.transaction = None

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("Transaction already in progress")
        self.transaction = {}

    def put(self, key, val):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction[key] = val

    def get(self, key):
        return self.data.get(key)

    def commit(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.data.update(self.transaction)
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction = None


if __name__ == "__main__":
    InMemoryDB = InMemoryDB()

    print(InMemoryDB.get("A"))

    try:
        InMemoryDB.put("A", 5)
    except Exception as e:
        print(f"Error: {e}")

    InMemoryDB.begin_transaction()

    InMemoryDB.put("A", 5)

    print(InMemoryDB.get("A"))

    InMemoryDB.put("A", 6)

    InMemoryDB.commit()

    print(InMemoryDB.get("A"))

    try:
        InMemoryDB.commit()
    except Exception as e:
        print(f"Error: {e}")

    try:
        InMemoryDB.rollback()
    except Exception as e:
        print(f"Error: {e}")

    print(InMemoryDB.get("B"))

    InMemoryDB.begin_transaction()

    InMemoryDB.put("B", 10)

    InMemoryDB.rollback()

    print(InMemoryDB.get("B"))
