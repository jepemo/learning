# SOLID aplicado en El Mundo Real™️: Specification pattern

* También llamado patron "Criteria".
* Contiene estas partes:
  * Filtros (coleccion de filtros)
    * Filtro: field, operador, valor
  * Orden (orderby, orderType)
  * offset (int)
  * limit (int)
* Por ejemplo:

```php
final class Criteria
{
    private $filters;
    private $order;
    private $offset;
    private $limit;
    public function __construct(Filters $filters, ?Order $order, ?int $offset, ?int $limit)
    {
        $this->filters = $filters;
        $this->order   = $order;
        $this->offset  = $offset;
        $this->limit   = $limit;
    }
    // ...
```

La parte del filter:
```php
final class Filter
{
    private $field;
    private $operator;
    private $value;
    public function __construct(FilterField $field, FilterOperator $operator, FilterValue $value)
    {
        $this->field    = $field;
        $this->operator = $operator;
        $this->value    = $value;
    }
    // ...
```

La parte del order:

```php
final class Order
{
    private $orderBy;
    private $orderType;
    public function __construct(OrderBy $orderBy, OrderType $orderType)
    {
        $this->orderBy   = $orderBy;
        $this->orderType = $orderType ?: OrderType::asc();
    }
    // ....
```

Aunque el objeto pueda parecer complejo, luego en el repository es mas sencillo ya que tendremos un metodo con el parametro criteria para realizar las busquedas:
```php
interface VideoRepository
{
    public function save(Video $video): void;
    public function search(VideoId $id): ?Video;
    public function searchByCriteria(Criteria $criteria): Videos;
}
```

