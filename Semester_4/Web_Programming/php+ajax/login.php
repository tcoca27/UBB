<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>

<body>
    <div id="form">
        <form action="access.php" method="POST">
            <?php
                if(@$_GET['Empty']== true) {
            ?>
                <div class="message">
                    <?php
                        echo @$_GET['Empty'];
                    ?>
                </div>
            <?php
                }
            ?>

            <?php
                if (@$_GET['Invalid'] == true) {
            ?>
                <div class="message">
                    <?php
                        echo @$_GET['INVALID'];
                    ?>
                </div>
            <?php
                }
            ?>
            <div>
                <label for="user">User:</label>
                <input type="text" id="user" name="username">
                <label for="pass">Password:</label>
                <input type="text" id="pass" name="password">
                <button id="submit">Login</button>
            </div>
        </form>
    </div>

</body>

</html>