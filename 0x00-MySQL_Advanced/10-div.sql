-- Safe divide
-- Create a division function
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
    RETURNS FLOAT
    DETERMINISTIC
    BEGIN
        DECLARE answer FLOAT DEFAULT 0;

        IF b != 0 THEN
            SET answer = a / b;
        ENDIF;

        RETURN answer;
    END //

DELIMITER ;