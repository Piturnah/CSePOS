# CSePOS
Computer Science A-Level group project.

We had to design and build an [ePOS](https://en.wikipedia.org/wiki/Point_of_sale) in Python. The requirements were that it must be able to take an arbitrary number of scanned barcodes via stdin and produce a receipt with details about the items purchased and their price. It must also keep track of stock and customer loyalty points.

## Usage

```console
$ python3 main.py
```

In `Make transaction` mode, enter as many barcodes as you like, then enter `n` to generate a receipt.

## Products

|Barcode|Price|Product|
|-|-|-|
|5051399748238|£4.99|NOTEBOOK|
|9781292183336|£22.99|MATHS TEXTBOOK|
|5057967252329|£5.99|BLUE FILE|
|5057967252343|£5.99|RED FILE|
|0076840600151|£4.00|B&J ICE CREAM|
|5053526205232|£1.50|BALL PENS|
|7599266811|£19.99|VINYL RECORD|
|5000399001003|£0.95|BLU TACK|
|4007817321027|£5.00|HIGHLIGHTERS|
|4007817525241|£1.40|ERASER|
|5000403110165|£1.20|PINK TACK|

## Authors

### [Peter](https://github.com/Piturnah) and [Kit](https://github.com/alfreaca)

Manage the product database, scan items, take payment, record sales.

### [Alex](https://github.com/AlexanderNoles)

Manage the stock information, request stock reorder if necessary.

### [Izzy](https://github.com/izzyav) and [Will](https://github.com/thegitwill)

Manage customer loyalty system.

### [Spencer](https://github.com/SenStrawberry)

Manage the application entry point.
