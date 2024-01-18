-- Safe divide
-- Create a division function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
    RETURNS INT
    DETERMINISTIC
    BEGIN
        IF b == 0 THEN
            RETURN 0;
        ENDIF;

        RETURN a / b;
    END //

DELIMITER ;