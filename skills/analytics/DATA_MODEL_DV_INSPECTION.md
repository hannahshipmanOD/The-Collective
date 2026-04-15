# Maestro DV Inspection Scopes — Snowflake Data Model

The `HOMEWORK` schema contains line items from Maestro inspection scoping tasks. This is the **authoritative source** for DV-added scope items, including seller debris removal, that may NOT appear in `ACQ_L1_FINALIZED_OFFERS_REPAIR_SCOPES`.

---

## Join Chain

```
ACQ_L2_FLIP_DETAILS.flip_token
  → ABRA.POST_CONTRACT_DILIGENCE_REVIEWS.flip_token
  → HOMEWORK.DWH_PROJECTS_VIEW.address_id  (= pcdr.address_token)
  → HOMEWORK.DWH_LINE_ITEMS_VIEW.project_id
  → HOMEWORK.DWH_LINE_ITEM_SCOPES_VIEW.line_item_id
```

---

## Table Schemas

### `DWH.ABRA.POST_CONTRACT_DILIGENCE_REVIEWS`

| Column | Type | Note |
|--------|------|------|
| ID | TEXT | Review UUID |
| FLIP_TOKEN | TEXT | Join key to ACQ_L2_FLIP_DETAILS |
| ADDRESS_TOKEN | TEXT | Joins to HOMEWORK.DWH_PROJECTS_VIEW.address_id |
| DECISION_TYPE | TEXT | e.g., `addendum_required` |
| TASK_ID | TEXT | Maestro task UUID |
| CREATED_AT | TIMESTAMP_TZ | |

---

### `DWH.HOMEWORK.DWH_PROJECTS_VIEW`

| Column | Type | Note |
|--------|------|------|
| ID | TEXT | Project UUID |
| ADDRESS_ID | TEXT | Address token — joins to `pcdr.address_token` |
| CREATED_AT | TIMESTAMP_TZ | |

---

### `DWH.HOMEWORK.DWH_LINE_ITEMS_VIEW`

| Column | Type | Note |
|--------|------|------|
| ID | TEXT | Line item UUID |
| PROJECT_ID | TEXT | FK to DWH_PROJECTS_VIEW.ID |
| COMPUTED_COST_CENTS | NUMBER | Cents — total cost for this line item |
| DELETED_AT | TIMESTAMP_TZ | Filter `IS NULL` |

---

### `DWH.HOMEWORK.DWH_LINE_ITEM_SCOPES_VIEW`

| Column | Type | Note |
|--------|------|------|
| ID | TEXT | Scope UUID |
| LINE_ITEM_ID | TEXT | FK to DWH_LINE_ITEMS_VIEW.ID |
| DESCRIPTION | TEXT | Full scope description — search for `'debris'` here |
| REASON | TEXT | Reason for scope |
| LABOR_TOTAL_CENTS | NUMBER | Labor cost (cents) |
| MATERIAL_UNIT_CENTS | NUMBER | Per-unit material cost (cents) |
| MATERIAL_QUANTITY | FLOAT | Quantity |
| DELETED_AT | TIMESTAMP_TZ | Filter `IS NULL` |
| CREATED_AT | TIMESTAMP_TZ | |

---

## Ready-to-Run Query

Replace `[flip_token]` with the property's flip token:

```sql
SELECT
  lis.description,
  lis.reason,
  li.computed_cost_cents,
  lis.material_unit_cents,
  lis.material_quantity,
  lis.created_at
FROM DWH.HOMEWORK.DWH_LINE_ITEM_SCOPES_VIEW lis
JOIN DWH.HOMEWORK.DWH_LINE_ITEMS_VIEW li
  ON lis.line_item_id = li.id
JOIN DWH.HOMEWORK.DWH_PROJECTS_VIEW p
  ON li.project_id = p.id
JOIN DWH.ABRA.POST_CONTRACT_DILIGENCE_REVIEWS pcdr
  ON p.address_id = pcdr.address_token
JOIN DWH.ACQUISITION.ACQ_L2_FLIP_DETAILS f
  ON pcdr.flip_token = f.flip_token
WHERE f.flip_token = '[flip_token]'
  AND li.deleted_at IS NULL
  AND lis.deleted_at IS NULL
ORDER BY lis.created_at DESC
```

---

## Finding Seller Debris Specifically

Add this `WHERE` clause to filter to debris only:

```sql
AND (
  LOWER(lis.description) LIKE '%debris%seller%'
  OR LOWER(lis.description) LIKE '%debris left by%'
)
```

---

## Notes

- `COMPUTED_COST_CENTS` and all `*_CENTS` fields are in **cents** — divide by 100 to display as dollars.
- Always filter `deleted_at IS NULL` on both `DWH_LINE_ITEMS_VIEW` and `DWH_LINE_ITEM_SCOPES_VIEW`.
- This schema captures scope items added **after** the DV inspection, which is why it may differ from pre-contract repair scope tables.
