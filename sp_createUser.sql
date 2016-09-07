DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from normal_user where Username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into normal_user
        (
            Username,
            Email,
            UserPassword
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;