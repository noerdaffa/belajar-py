#variabel adalah tempat menyimpan data

#asignment nilai
a = 10
x = 5
panjang = 1000

#pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

#penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 10000000 #ini_boleh
nilaiZ = 17.5 #ini_boleh

#pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

#assignment indirect
b = a
print("Nilai b = ", b)


<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Store - E-commerce Layout</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .banner-bg { background-color: #a3e3d3; }
        .promo-border { border: 2px dashed #0e5a71; }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans">

    <header class="bg-white border-b">
        <div class="container mx-auto px-4 py-2 flex justify-between items-center text-xs text-gray-500">
            <div>Contact us</div>
            <div class="flex gap-4">
                <span>Sign in</span>
                <span>Cart (0)</span>
            </div>
        </div>
        <nav class="container mx-auto px-4 py-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <h1 class="text-2xl font-bold text-blue-900">my <span class="text-black">store</span></h1>
            <ul class="flex gap-6 uppercase font-semibold text-sm">
                <li>Clothes</li>
                <li>Accessories</li>
                <li>Art</li>
            </ul>
            <div class="relative">
                <input type="text" placeholder="Search our catalog" class="border p-2 pr-10 text-sm w-64">
                <span class="absolute right-3 top-2">🔍</span>
            </div>
        </nav>
    </header>

    <section class="container mx-auto px-4 mt-6">
        <div class="relative h-64 md:h-96 overflow-hidden flex">
            <div class="w-1/3 banner-bg p-8 flex flex-col justify-center">
                <h2 class="text-3xl font-bold text-white mb-2">SAMPLE 3</h2>
                <p class="text-white text-xs leading-relaxed uppercase">Excepteur occaecat cupidatat non proident, sunt in culpa qui officia.</p>
            </div>
            <div class="w-2/3 bg-cover bg-center" style="background-image: url('https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=1000');">
                </div>
        </div>
    </section>

    <section class="container mx-auto px-4 py-12">
        <h3 class="text-center font-bold text-lg mb-8 uppercase tracking-widest">Popular Products</h3>
        
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <div class="bg-white p-4 shadow-sm group relative">
                <div class="relative bg-gray-100 h-64 mb-4 flex items-center justify-center">
                    <span class="absolute top-2 left-2 bg-yellow-500 text-white text-[10px] px-2 py-1">-20%</span>
                    <span class="absolute top-8 left-2 bg-blue-400 text-white text-[10px] px-2 py-1">NEW</span>
                    <img src="https://via.placeholder.com/150" alt="product" class="mix-blend-multiply">
                </div>
                <div class="text-center">
                    <p class="text-sm text-gray-600 truncate">Hummingbird printed t-shirt</p>
                    <p class="font-bold text-gray-900 mt-1">$19.12 <span class="line-through text-gray-400 text-xs font-normal">$23.90</span></p>
                </div>
            </div>
            <div class="bg-white p-4 shadow-sm group">
                <div class="bg-gray-100 h-64 mb-4 flex items-center justify-center">
                    <span class="absolute top-2 left-2 bg-blue-400 text-white text-[10px] px-2 py-1">NEW</span>
                    <img src="https://via.placeholder.com/120" alt="mug" class="mix-blend-multiply">
                </div>
                <div class="text-center">
                    <p class="text-sm text-gray-600">Mug Today Is A Good Day</p>
                    <p class="font-bold text-gray-900 mt-1">$11.90</p>
                </div>
            </div>
            </div>
        
        <div class="text-right mt-6">
            <a href="#" class="text-gray-500 text-sm hover:underline">All products ></a>
        </div>
    </section>

    <section class="container mx-auto px-4 py-8">
        <div class="promo-border p-8 text-center flex flex-col items-center justify-center">
            <h2 class="text-4xl font-bold text-blue-900 italic">20% OFF <span class="font-normal not-italic text-2xl ml-2">ON CLOTHES</span></h2>
            <a href="#" class="mt-4 text-xs font-bold border-b-2 border-black pb-1 uppercase">See More</a>
        </div>
    </section>

    <section class="container mx-auto px-4 py-12 text-center max-w-4xl">
        <h4 class="font-bold uppercase mb-4">Custom Text Block</h4>
        <p class="text-gray-500 text-sm leading-relaxed">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        </p>
    </section>

    <section class="bg-white py-8 border-t border-b">
        <div class="container mx-auto px-4 flex flex-col md:flex-row justify-between items-center">
            <p class="text-sm font-semibold mb-4 md:mb-0 uppercase">Get our latest news and special sales</p>
            <div class="flex w-full md:w-auto">
                <input type="email" placeholder="Your email address" class="border p-2 flex-grow md:w-80">
                <button class="bg-cyan-500 text-white px-6 py-2 uppercase text-sm font-bold">Subscribe</button>
            </div>
        </div>
    </section>

    <footer class="bg-white py-12">
        <div class="container mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-8 text-xs text-gray-500">
            <div>
                <h5 class="font-bold text-gray-800 uppercase mb-4">Products</h5>
                <ul class="space-y-2">
                    <li>Prices drop</li>
                    <li>New products</li>
                    <li>Best sales</li>
                </ul>
            </div>
            <div>
                <h5 class="font-bold text-gray-800 uppercase mb-4">Our Company</h5>
                <ul class="space-y-2">
                    <li>Delivery</li>
                    <li>Legal Notice</li>
                    <li>Terms and conditions</li>
                    <li>About us</li>
                </ul>
            </div>
            <div>
                <h5 class="font-bold text-gray-800 uppercase mb-4">Your Account</h5>
                <ul class="space-y-2">
                    <li>Personal info</li>
                    <li>Orders</li>
                    <li>Credit slips</li>
                </ul>
            </div>
            <div>
                <h5 class="font-bold text-gray-800 uppercase mb-4">Store Information</h5>
                <p>My Store<br>United States<br>Email us: sales@yourstore.com</p>
            </div>
        </div>
        <div class="text-center mt-12 text-[10px] text-gray-400">
            © 2026 - Ecommerce software by PrestaShop™
        </div>
    </footer>

</body>
</html>