# Practicando SOLID con la kata GildedRose

* En el ejemplo, se utiliza herencia para cada uno de los items para encapsular la logica de cada uno de ellos.
* Al final el bucle queda como:

``` java
final class GildedRose {
    void updateQuality(List<Item> items) {
        items.forEach(Item::update);
    }
}
```

La clase del item padre queda como:

```java
abstract class Item {
    private ItemName name;
    private ItemSellIn sellIn;
    private ItemQuality quality;

    Item(final ItemName name, final ItemSellIn sellIn, final ItemQuality quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }

    abstract void update();

    // ....
}
```

Y por ejemplo, una de las implementaciones concretas es:

```java
final class AgedBrie extends Item {
    private static final int DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD = 0;

    AgedBrie(final ItemName name, final ItemSellIn sellIn, final ItemQuality quality) {
        super(name, sellIn, quality);
    }

    @Override
    void update() {
        decreaseSellIn();

        increaseQuality();

        if (hasToBeSoldInLessThan(DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD)) {
            increaseQuality();
        }
    }
}
```

* Es decir, se sustituye el monton de ifs/swtich pasando el comportamiento a las clases
* switchcase -> polymorfism
