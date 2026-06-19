class Cart():
    def __init__(self,request):
        self.session=request.session
        cart=request.session.get('cart')
        if 'cart' not in request.session:
            cart=self.session['cart']={}
        self.cart=cart
    
    def add(self,product,quantity):
        product_id = str(product.id)
        quantity = int(quantity)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}
        self.session.modified = True
    
    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())