<?php
	function generateSalt($n){
		$values="abcdefghijklmnopqrstuvwxyz0123456789";
		$salt = "";
		$max = strlen($values)-1;
		for($i = 0;$i < $n; $i++){
			$salt .= $values[rand(0, $max)];
		}
		return $salt;
	}

	function createUser($name, $email, $key){
		require_once("db_connection.php");
		$query = "SELECT user_key, salt, name FROM users WHERE user_email = '$email';";
		if($result = getResult($query)){
			if(mysqli_num_rows($result) != 0){
				return "ALREADY_EXISTS";
			}
			else{
				$salt = generateSalt(128);
				$hashed_key = hash('sha512', $key + $salt);
				$query = "INSERT INTO users VALUES('$email','$hashed_key', '$name', NULL, '$salt');";
				if($qResult = getResult($query)){
					return true;
				}
				else{
					return "ERROR";
				}
			}
		}
		else{
			return "ERROR";
		}
	}
?>