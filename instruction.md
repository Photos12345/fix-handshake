We need a short traffic summary from the Apache combined-format access log at `/app/access.log`. Each non-empty line is one HTTP request.

Write the result to `/app/report.json` as a JSON object with exactly these keys:

{"total_requests": <int>, "unique_ips": <int>, "top_path": "<str>"}

- `total_requests`: count of log lines (requests).
- `unique_ips`: count of distinct client IP addresses.
- `top_path`: the URL path requested most often; if there is a tie, any one of the tied paths is acceptable.

Success criteria:

1. `/app/report.json` exists and contains valid JSON matching the shape above.
2. `total_requests` equals the number of log lines (6), and `unique_ips` equals the number of distinct client IPs (3).
3. `top_path` is the single most-requested URL path (`/index.html`).
