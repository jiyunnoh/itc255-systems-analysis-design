import unittest
from user import User
from customer import Customer
from employee import Employee
from item import Item
from membership import Membership
from order import Order
from orderdetail import OrderDetail
from payment import Payment
from scale import Scale

class UserTest(unittest.TestCase):
    def setup(self):
        self.user=User('1', 'Jiyun', '2223334444')

    def test_getUserId(self):
        self.assertEqual(self.user.getUserId(), '1')

    def test_getUserName(self):
        self.assertEqual(self.user.getUserName(), 'Jiyun')

    def test_setUserPhone(self):
        self.user.setUserPhone('1115559999')
        self.assertEqual(self.user.getUserPhone(), '1115559999')

class MembershipTest(unittest.TestCase):
    def setUp(self):
        self.membership=Membership('10', '03012020', 'silver')

    def test_getJoinDate(self):
        self.assertEqual(self.membership.getJoinDate(), '03012020')

    def test_setLevel(self):
        self.membership.setLevel('gold')
        self.assertEqual(self.membership.getLevel(), 'gold')

class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer=Customer(User, 'j@gmail.com', Membership)
    
    def test_getMembership(self):
        self.assertEqual(self.customer.getMembership(), Membership)

    def test_setEmail(self):
        self.customer.setEmail('n@gmail.com')
        self.assertEqual(self.customer.getEmail(), 'n@gmail.com')

class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item('20', 'phonecase', '10.00')

    def test_setItemPrice(self):
        self.item.setItemPrice('13.00')
        self.assertEqual(self.item.getItemPrice(), '13.00')

class OrderDetailTest(unittest.TestCase):
    def setUp(self):
        self.orderdetail=OrderDetail(Item, '3')

    def test_getQuantity(self):
        self.assertEqual(self.orderdetail.getQuantity(), '3')

    def test_getItem(self):
        self.assertEqual(self.orderdetail.getItem(), Item)

class PaymentTest(unittest.TestCase):
    def setUp(self):
        self.payment=Payment('35.00')

    def test_paymentString(self):
        self.assertEqual(str(self.payment), 'The total amount is $35.00')
