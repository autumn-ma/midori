# Midori

System design and implementation for a web crawler.

<p align="center">
<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/48282663/243183222-2e97f423-5dd6-4cdb-858d-883aa22d1471.png">
<h1 align="center">
   Midori
  </h1>
  
</p>

# System Design

## High Level Design

This will be the high level flow of the data, initally the api will call DB, which will inturn call the crawler which will fetch html pages and parse information. The crawler also needs URLs to fetch html pages which would be in our URL DB, we would initally feed some pages to the URL DB but it will be self sustaining loop where crawler would provide URLs to URL DB after parsing webpages.

![Untitled-2023-03-17-1604(8)](https://github.com/myan-ish/midori/assets/48282663/300068c7-190f-4ed3-83b7-9e817a54fe89)


## Low Level Design

### API interface

![Untitled-2023-03-17-1604(9)](https://github.com/myan-ish/midori/assets/48282663/2d6a642a-6321-4dec-9dbc-326dac7991c4)

### Database

#### Schema and APIs

![Untitled-2023-04-20-1131(12)](https://github.com/myan-ish/midori/assets/48282663/4344d385-c8b7-47b4-bd0a-3d90dc5add95)

#### Main Table

![Untitled-2023-04-20-1131(8)](https://github.com/myan-ish/midori/assets/48282663/ab5ce2fe-f3d5-4f50-8cef-a53c4d7794bd)

#### Global Index

![Untitled-2023-04-20-1131(9)](https://github.com/myan-ish/midori/assets/48282663/41eefbf5-e7c5-4193-a0fe-933d16ca616d)

#### Text Index

![Untitled-2023-04-20-1131(10)](https://github.com/myan-ish/midori/assets/48282663/2391ef8d-f8cb-4db6-8ab9-de18e1314918)




