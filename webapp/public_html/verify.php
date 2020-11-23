<?php
session_start();
$user_name = $_SESSION["name"];
$user_email = $_SESSION["email"];
$set = isset($user_name) && isset($user_email);
if(!$set){
    session_destroy();
    header("Location: index.html?error=timed_out");
}
?>

<?php
	if($_SERVER["REQUEST_METHOD"] == "POST"){
		if($_POST['action'] == "Verify"){
			$eval_id = $_POST['eval_id'];
			$query = "SELECT * FROM marks WHERE user_email = '$user_email' AND eval_id = $eval_id;";
			require_once("./utilities/db_connection.php");
			if($result = getResult($query)){
				if(mysqli_num_rows($result) == 1){
					$row = mysqli_fetch_array($result);
					$marks_id = $row['record_number'];
					$query = "UPDATE marks SET verified=1 WHERE record_number = $marks_id;";
					if(getResult($query)){
						header("Location: marks.html?success=yes&marks_id=$marks_id");
					}
					else{
						header("Location: marks.html?success=no");
					}
				}

			}
			else{
				header("Location: marks.html?success=no");
			}
		}
	}
	else{
		header("Location: index.html?error=timed_out");
	}
?>