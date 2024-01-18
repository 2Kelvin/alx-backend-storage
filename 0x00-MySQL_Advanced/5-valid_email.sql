-- Email validation
-- Resets valid_email attribute when the email changes
DELIMITER //

CREATE TRIGGER resetEmailAttribute
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END //

DELIMITER ;