# Common Data Model

## Shared tables

### `opendoor.core.properties`
Property master record.

| Column | Type | Description |
|--------|------|-------------|
| `property_id` | STRING | Internal property ID |
| `address_token` | STRING | Hashed address |
| `market` | STRING | Market code (e.g. `PHX`, `ATL`) |
| `state` | STRING | Transaction state |
| `created_at` | TIMESTAMP | Record creation |

### `opendoor.core.customers`
Customer master record.

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | STRING | Internal customer ID |
| `email` | STRING | Customer email |
| `market` | STRING | Market |
| `created_at` | TIMESTAMP | First interaction |

### `opendoor.core.markets`
Market reference table.

| Column | Type | Description |
|--------|------|-------------|
| `market_code` | STRING | Market code |
| `market_name` | STRING | Display name |
| `state_abbr` | STRING | US state |
| `is_active` | BOOLEAN | Currently operating |
