<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KHADKA Ecommerce</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            background-image: url('i.png');
            background-size: cover;
        }
    </style>
    <script>
        function showPriceList(product) {
            var priceList = document.querySelector('.price-list');
            if (product === 'Freefire Diamond') {
                priceList.innerHTML = `
                    <ul>
                        <li>115 Diamonds = $85</li>
                        <li>210 Diamonds = $170</li>
                        <li>340 Diamonds = $230</li>
                    </ul>
                `;
            }
            priceList.style.display = 'block';
            document.querySelector('.place-order-btn').style.display = 'block';
        }

        function redirectToFacebook() {
            window.location.href = 'https://www.facebook.com/profile.php?id=100092196915636';
        }
    </script>
</head>
<body>
    <header>
        <h1><p><span style="color: Silver;">Senior Ecommerce</span></p></h1>
    </header>
    <main>
        <section class="product">
            <img src="dmd.png" width="300" height="200" alt="Freefire Diamond">           	
            <h2>Freefire Diamond</h2>
            <button onclick="showPriceList('Freefire Diamond')">Add to Cart</button>
        </section>
        <section class="product">
            <img src="uc.png" width="300" height="200" alt="Pubg UC">
            <h2>Pubg UC</h2>
            <button>Add to Cart</button>
        </section>
        <section class="product">
            <img src="ml.png" width="300" height="200" alt="MLBB Diamond">
            <h2>MLBB Diamond</h2>
            <button>Add to Cart</button>
        </section>
        <div class="price-list"></div>
        <button class="place-order-btn" onclick="redirectToFacebook()">Place Order</button>
    </main>
    <footer>
        <a href="https://www.facebook.com/profile.php?id=61556935483500">Contact Admin</a>
    </footer>
</body>
</html>
