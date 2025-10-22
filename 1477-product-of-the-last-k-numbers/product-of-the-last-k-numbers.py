class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_products = []
        self.size = 0
        self.last_0_index = -1
        
    def add(self, num):
        if self.size == 0:
            if num == 0:
                self.prefix_products.append(1)
                self.last_0_index = self.size
            else:
                self.prefix_products.append(num)
        else:
            if num == 0:
                self.prefix_products.append(self.prefix_products[self.size - 1])
                self.last_0_index = self.size
            else:
                self.prefix_products.append(self.prefix_products[self.size - 1] * num)
        self.size += 1

            
        

    def getProduct(self, k):
        if self.last_0_index >= self.size - k:
            return 0
        elif k == self.size:
            return self.prefix_products[self.size - 1]
        else:
            return self.prefix_products[self.size - 1] / self.prefix_products[self.size - k - 1]


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)