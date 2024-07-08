# This class is used to create each item object 
class ItemToPurchase: 

    # Constructor with parameters with initialized values
    def __init__(self, name = "none", price = 0, quantity = 0, description = "none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    # function that prints individual item description
    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))    

    # function to print individual item cost
    def print_item_cost(self):
        total_cost = round(self.item_price * self.item_quantity)
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, total_cost))    

# this class contains all of the shopping cart functions 
class ShoppingCart:

    # constructor with paramters and default initialized values
    def __init__(self, customer_name = "none", date = "January 1, 2020"):
        self.customer_name = customer_name
        self.date = date 
        self.cart_items = []

    # this function is used to add an item into the shopping cart list
    def add_item(self, item):
        self.cart_items.append(item)

    # this function is used to remove an item from the shopping cart list
    def remove_item(self, item_to_remove):
        # use a boolean variable to determine if the item is found in the cart or not
        item_exists = False
        # checks every item in the list to check if it matches with item to remove
        for item in self.cart_items:
            if item.item_name == item_to_remove:
                  self.cart_items.remove(item)
                  item_exists = True
                  break
            # input validation for if the entered item does not exist in the cart
            if not item_exists:
                print("Item not found in cart. Nothing removed")

    # this function allows the user to modify the parameters of the item object i.e. name, description, price, quantity     
    def modify_item(self, item_to_buy):
        # similar logic to remove item
        item_exists = False
        for item in self.cart_items:
            if item.item_name == item_to_buy.item_name:
                item_exists = True
                # changes the value of 
                if item_to_buy.item_description != "none":
                    item.item_description = item_to_buy.item_description
                if item_to_buy.item_price != 0:
                    item.item_price = item_to_buy.item_price
                if item_to_buy.item_quantity != 0:
                    item.item_quantity = item_to_buy.item_quantity
                break
        # input validation for if the item to be modified does not exist in the cart    
        if not item_exists:
            print("Item not found in cart. Nothing modified.")

    # this function totals the number of item objects in the cart list
    def get_num_items_in_cart(self):
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        return total_items
    
    # this function gets the total cost of all item objects in cart list by compiling the prices and quantity
    def get_cost_of_cart(self):
        total_price = 0
        for item in self.cart_items:
            total_price += item.item_price * item.item_quantity
        return total_price
    
    # this function prints the users shopping cart number of items and total cost
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.date)) 
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print("Total: ${}".format(self.get_cost_of_cart()))    

    # this function prints the item object descriptions in the cart
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.date))
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


#main section of code

def print_menu(cart):

    menu = ("\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option: ")
    # keeps printing menu until condition is false
    while True:
        print(menu)
        option = input( "\n")
        # breaks out of the loop
        if option == 'q':
            break
        # calls the add_item function
        elif option == 'a':
            print("ADD ITEM TO CART")
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(item)
        # calls the remove_item function     
        elif option == 'r':
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)
        #calls modify_item function    
        elif option == 'c':
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name: ")
            description = "none"
            price = 0
            quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(name, price, quantity, description)
            cart.modify_item(item)
        # calls print_descriptions     
        elif option == 'i':
            print("Output items' descriptions ")
            cart.print_descriptions()
        #calls  print_total
        elif option == 'o':
            print("Output shopping cart")
            cart.print_total()
        # input validation if user selects an invalid option    
        else:
            print("Invalid choice. Enter a valid choice.")

def main():
    # asks user to input name and date and creates cart object 
    name = input("Enter customer's name: ")
    date = input("Enter today's date: ")
    cart = ShoppingCart(name, date)
    print("Customer name: {}".format(cart.customer_name))
    print("Today's date: {}".format(cart.date))
    print_menu(cart)

if __name__ == "__main__":
    main()
