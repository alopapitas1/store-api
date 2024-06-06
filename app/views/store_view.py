def render_store_list(productos):
    return[
        {
            "id":store.id,
            "name":store.name,
            "description":store.description,
            "price":store.price,
            "stock":store.stock,
        }
        for store in productos
    ]
    
def render_store_detail(producto):
    return [
        {
            "id":producto.id,
            "name":producto.name,
            "description":producto.description,
            "price":producto.price,
            "stock":producto.stock,
        }
    ]

