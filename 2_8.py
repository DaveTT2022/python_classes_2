import prettytable


class WebStore(object):
    INST_NUM = 0    
    product_list = set()
    def __new__(cls, **kwargs):
        WebStore.product_list.add(kwargs["product"])
        if not kwargs["address"] in WebStore.dict_info.keys():
            WebStore.INST_NUM += 1
            return super().__new__(cls)
        else:
            cls.duplicate_item(**kwargs)

    dict_info = {}

    def __init__(self, address, product, quantity):
        WebStore.dict_info.update({address : {product: quantity}})

    @staticmethod
    def duplicate_item(**kwargs):
        if kwargs["product"] in WebStore.dict_info[kwargs["address"]].keys():
            WebStore.dict_info[kwargs["address"]][kwargs["product"]] += kwargs["quantity"]
        else:
            WebStore.dict_info[kwargs["address"]][kwargs["product"]] = kwargs["quantity"]

    @staticmethod
    def top_requests():
        list_keys = list(WebStore.dict_info.keys())
        list_keys.sort(reverse = True, key = lambda add : sum(WebStore.dict_info[add].values()))
        return list_keys

def product_nums(prod_list: dict):
    list_prod = []
    for product in WebStore.product_list:
        list_prod.append(product)
        for prods in prod_list.values():
            if product in prods.keys():
                list_prod.append(prods[product])
                continue
            else:
                list_prod.append(0)

        yield list_prod
        list_prod = []

table = prettytable.PrettyTable()
table.set_style(16)
text = ""
while True:
    text = input("Send Webstore info by this format (Address product quantity), if you want to stop write 'stop' \n")
    if text == "stop":
        break
    text = text.split(" ")
    obj = WebStore(address = text[0], product = text[1], quantity = int(text[2]))

address_list = ["Addresses"] + [x for x in WebStore.dict_info]
table.field_names = address_list

product_gen = product_nums(WebStore.dict_info)
for list_ in product_gen:
    table.add_row(list_)
table.align = "c"
print(table)

top_table = prettytable.PrettyTable()
top_table.set_style(16)

most = WebStore.top_requests()

top_table.add_column("", [x for x in range(1, len(most) + 1)])
top_table.add_column("Top purchases", [x for x in most])

print(top_table)