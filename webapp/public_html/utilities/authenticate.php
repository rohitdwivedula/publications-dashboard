<?php
	function authenticate($id, $key){
		require_once("db_connection.php");
		$query = "SELECT * FROM Researcher WHERE researcher_id = $id;";
		if($result = getResult($query)){
			if(mysqli_num_rows($result) == 1){
				$row = mysqli_fetch_array($result);
				session_start();
				$_SESSION['id'] = $id;
				$_SESSION['name'] = $row['name'];
				$_SESSION['h5'] = $row["h5_index"];
				header("Location: researcher.html");
				exit();

				//wrong password
				//header("Location: index.html?error=incorrect");
				//exit();
			}
			else{
				//email not registered
				header("Location: index.html?error=notexists");
				exit();
			}
		}
		else{
			header("Location: index.html?error=yes123");
			exit();
		}
	}
?>