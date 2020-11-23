<?php
	function authenticate($email, $key){
		require_once("db_connection.php");
		$query = "SELECT user_key, salt, name FROM users WHERE user_email = '$email';";
		if($result = getResult($query)){
			if(mysqli_num_rows($result) == 1){
				$row = mysqli_fetch_array($result);
				$salt = $row['salt'];
				$hashed_key = hash('sha512', $key + $salt);
				if($row['user_key'] == $hashed_key){
					//correct password
					session_start();
					$_SESSION['name'] = $row['name'];
					$_SESSION['email'] = $email;
					header("Location: marks.html");
					exit();
				}
				else{
					//wrong password
					header("Location: index.html?error=incorrect");
					exit();
				}
			}
			else{
				//email not registered
				header("Location: index.html?error=notexists");
				exit();
			}
		}
		else{
			header("Location: index.html?error=yes");
			exit();
		}
	}
?>