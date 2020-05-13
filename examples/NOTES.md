Currently, all APIs use **GET method** only
# Response Format

```
{
    "status" : "success|error",
    "data" : {
        ...
    },
    "message": "Message text",
    "status_code": 200

}
```

<table>
<tr>
<th>Field</td>
<th>Description/Values</th>
<th>Data Type</th>
<th>Required</td>
</tr>
<tr>
<td>status</td>
<td>success|error</td>
<td>string</td>
<td>yes</td>
</tr>
<tr>
<td>data</td>
<td>more details in each api section</td>
<td>object/dict or a list (need to disscus options below)</td>
<td>yes|no, yes when status is success</td>
</tr>
<tr>
<td>message</td>
<td>A meaningful, end-user-readable, explaining what went wrong when status is error.</td>
<td>string</td>
<td>yes|no, yes when status is error</td>
</tr>
<tr>
<td>status_code</td>
<td>HTTP status code</td>
<td>number</td>
<td>yes</td>
</tr>
</table>

# Energy
## Endpoints
Example endpoints for NEM:
* /energy/nem/1d
* /energy/nem/3d
* /energy/nem/7d
* /energy/nem/30d
* /energy/nem/1y
* /energy/nem/all

Example endpoints for each state:
* /energy/{nsw|qld|sa|tas|vic}/1d
* /energy/{nsw|qld|sa|tas|vic}/3d
* /energy/{nsw|qld|sa|tas|vic}/7d
* /energy/{nsw|qld|sa|tas|vic}/30d
* /energy/{nsw|qld|sa|tas|vic}/1y
* /energy/{nsw|qld|sa|tas|vic}/all

### Brainstorm ???
Available time ranges are: 1d, 3d, 7d, 30d, 1y, all (monthly from 2005 to current)

Available intervals are:
* 1d: 5m
* 3d: 5m, 30m
* 7d: 5m, 30m
* 30d: day (daily)
* 1y: day, week, month
* all: month, season, quarter, half year, fin year, year
    * season: frontend will base on month to group and filter spring, summer, autumn or winter
    * quarter: frontend will base on month to group and filter q1, q2, q3 or q4

**We have three options:**

* request `1d, 3d and 7d` always return `5m data`; request `30d, 1y and all` always return `daily data` frontend has to group data to `30m, week, month` 
* request date range and interval together. Ex 3d+30m, 1y+week, 1y+month. Drontend doesn't have to group data. This apporach user click date range then click interval the web will fetch data and show charts
* request date range, api will include all intervals. The response obj could be large.

## Data Format
We will have same format for data for different ranges and intervals. The only thing different will be data length. For example: `1y+daily` will be 365 data points but `1y+month` only has 12 data points.

Data for NEM and each state are same in general except there are some fields in NEM can't be found in state data ex: `battery_discharging`. 
### NEM
[1D 5min for NEM](nem_1d5m_crunched.json)

### States
[1D 5min for NSW](nsw_1day_cru.json)

# Facilities
To be updated
