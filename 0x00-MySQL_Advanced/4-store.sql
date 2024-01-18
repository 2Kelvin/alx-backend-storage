-- Buy buy buy
-- Creating a trigger that decreases item quantity after a new order
CREATE TRIGGER decreaseItemQuantity
AFTER
INSERT ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;