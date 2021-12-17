dict = {"info": [600, 630, 620], "ril": [1430, 1490, 1567], "mtl": [234, 180, 160]}
print("Dictionary = ", dict)


def print_all():
    for k, v in dict.items():
        print(k, "==>", v, "==>", "avg: ", round(sum(v) / len(v), 2))


def add():
    add_stock_ticker_key = input("Enter a stock ticker key:").lower()
    add_stock_ticker_value = int(input("Enter a stock ticker value:"))
    # d = {"add_stock_ticker_key":add_stock_ticker_value}
    # print(d)
    if add_stock_ticker_key in dict:
        dict[add_stock_ticker_key].append(add_stock_ticker_value)
        print("Dictionary = ", dict)
    else:
        dict[add_stock_ticker_key] = [add_stock_ticker_value]
        print("New Dictionary after adding = ", dict)


def main():
    operations_list = ['print', 'add']
    user_input = input("Enter operations:").lower()
    if user_input in operations_list:
        if user_input == 'print':
            print_all()
        elif user_input == 'add':
            add()
    else:
        print("Invalid operations")


if __name__ == '__main__':
    main()
