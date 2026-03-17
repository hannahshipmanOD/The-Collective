# Analytics Quick Reference

## Key metrics by team

### CX (Customer Support)
| Metric | Definition | Target |
|--------|-----------|--------|
| Contact volume | # contacts per day | Baseline |
| First response time | Time to first reply | <1hr (urgent), <4hr (high) |
| Resolution time | Time to solve | <24hr (normal) |
| CSAT | Customer satisfaction score | >4.5/5 |
| Recontact rate | % contacts that open again within 7d | <15% |

### TC (Transaction Management)
| Metric | Definition | Target |
|--------|-----------|--------|
| Pipeline count | Active transactions per TC | Baseline |
| Days to close | Avg days from contract to close | Baseline |
| At-risk rate | % transactions flagged at-risk | <10% |
| Fall-through rate | % contracts that cancel | Baseline |
| On-time close rate | % that close on scheduled date | >90% |

## Common time ranges
- Yesterday: `DATE(created_at) = CURRENT_DATE - 1`
- Last 7 days: `created_at >= CURRENT_TIMESTAMP - INTERVAL 7 DAY`
- Last 30 days: `created_at >= CURRENT_TIMESTAMP - INTERVAL 30 DAY`
- MTD: `DATE_TRUNC(created_at, MONTH) = DATE_TRUNC(CURRENT_DATE, MONTH)`
