<html>
    <head>
        <title>My Shop</title>
    </head>

    <body>
        <h1>Welcome to my website </h1>
        <h3>f5 demo </h3>

        

        <!-- Load icon library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<!-- The form -->
<form class="example" action="Rediswebsite.py">
  <input type="text" placeholder="Search List.." name="search">
  <button type="submit"><i class="fa fa-search"></i></button>
</form>

<!-- The form -->
<form class="example" action="Rediswebsite.py">
  <input type="text" placeholder="add name to list.." name="search">
  <button type="submit"><i class="fa fa-search"></i></button>
</form>

<h4> List of names in vip list</h4>
        <ul>
            <?php
            $json = file_get_contents('http://product-service/');
            $obj = json_decode($json);
            $products = $obj->products;
            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>

