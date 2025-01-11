Below is a typical pattern in PostgreSQL to remove duplicates for **all** given `mue_types` (e.g., `DME`, `PS`, `FOH`). The idea is:

- Partition by `(mue_type, code)` so that each combination of `(mue_type, code)` is considered its own group.
- Use `ROW_NUMBER()` to mark duplicates within each group (`rn > 1`).
- Delete those duplicate rows, leaving only the “first” row (sorted by `id`) in each group.

---

## Example Query

```sql
WITH duplicates AS (
    SELECT
        id,
        ROW_NUMBER() OVER (
            PARTITION BY mue_type, code
            ORDER BY id
        ) AS rn
    FROM public.mue_mcr_2025
    WHERE mue_type IN ('DME', 'PS', 'FOH')
)
DELETE FROM public.mue_mcr_2025 AS t
USING duplicates AS d
WHERE t.id = d.id
  AND d.rn > 1;
```

### Explanation

1. **`duplicates` CTE**  
   - We select rows from `public.mue_mcr_2025` only where `mue_type` is in the set `('DME','PS','FOH')`.  
   - We use `ROW_NUMBER() OVER (PARTITION BY mue_type, code ORDER BY id)` to label rows within each `(mue_type, code)` group.  
   - The row with `rn = 1` is the “first” row (lowest `id`) in that group; rows with `rn > 1` are duplicates.

2. **Delete duplicates**  
   - We then delete from the main table `t` (`public.mue_mcr_2025`) any row that appears in the `duplicates` CTE with `rn > 1`.  
   - This effectively removes all but one row for each `(mue_type, code)` combination.

If you prefer to remove duplicates *for every mue_type in the entire table*, simply remove the line:
```sql
WHERE mue_type IN ('DME', 'PS', 'FOH')
```
from the CTE. Then it will remove duplicates across all `mue_type` values found in the table.



Here’s a straightforward way to remove the `$` symbol from all the specified string fields in the `public.ambulence_fee_schedule_2025` table:

```sql
UPDATE public.ambulence_fee_schedule_2025
SET base_rate          = REPLACE(base_rate, '$', ''),
    urban_base_rate    = REPLACE(urban_base_rate, '$', ''),
    rural_base_rate    = REPLACE(rural_base_rate, '$', ''),
    rbr_lowest_quartile = REPLACE(rbr_lowest_quartile, '$', ''),
    rural_ground_miles = REPLACE(rural_ground_miles, '$', '');
```

This will replace any `$` in each of those columns with an empty string, effectively removing it.