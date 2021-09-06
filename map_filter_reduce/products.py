

products=[
    {'p_name':'complan','mrp':220,'avl_qty':50},
    {'p_name':'horlicks','mrp':230,'avl_qty':20},
    {'p_name':'bournvita','mrp':250,'avl_qty':0},
    {'p_name':'nutricharge','mrp':200,'avl_qty':150},
    {'p_name':'mylo','mrp':150,'avl_qty':0}
]
#print all product names
product_name=list(map(lambda item:item['p_name'],products))
print(product_name)

#print all product names availabe in shop
avl_products=list(map(lambda item_name:item_name['p_name'],list(filter(lambda item:item['avl_qty']>0,products ))))
print(avl_products)

#print outof stock products:
out_of_stock_products=list(map(lambda item_name:item_name['p_name'],list(filter(lambda item:item['avl_qty']==0,products ))))
print(out_of_stock_products)
#costly product
prices=list(map(lambda price:price['mrp'],products))
print(max(prices))
#lowest price
print(min(prices))