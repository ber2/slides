---
theme: default
class:
  - lead
paginate: true
# backgroundColor: #fff
marp: true
# header: Hello
footer: Alberto Cámara - Data Sketches for Reporting - 2023-03-16
---

<!-- _class: -->
# **Data Sketches for Reporting**

![bg left:30% width:300](img/hybrid-theory.png)

**Alberto Cámara**, Lead Data Scientist
**Hybrid Theory**, London
2023-03-16

---

![bg right:40%](img/bigdata.jpg)

# The problem of Reporting Big Data

* We process hundreds of billions of data points on a monthly basis
* Our **data is sparse**: it is hard to find events satisfying a search criteria 
* This makes simple queries on log-level data **slow and expensive**
* In our case, mapping user ids to third-party partners adds **huge costs & complications**

---

![bg left:40%](img/fast.jpg)

# What to do 

For any report, we prefer a fast estimation instead of a slow, exact computation.

* **Sampling**: only take into consideration a subset of the data.
* **Preaggregate**: precompute and store aggregations on most common dimensions of the data, then compute further aggregations on-demand.

---

In both cases:
* Counting total events is **easy**
* Estimating counts of unique users is **hard**

---

![bg right:30%](img/sampling.jpg)

## Sampling

- Consists of making estimations based on observing only a subset of the data
- We have `production_metastore.events_sampled`, which contains a sample of 5% of the events over each partition
- Until recently, we used this approach to compute the **overlap report**
- **Insider trends** report currently uses this approach

---

### Pros & Cons of Sampling

- Pro: you only store a very small amount of data
- Pro: some reports become very fast

- Con: looking for a sparse behaviour is hopeless
- Con: mapping user ids to other partners is still very slow
- Con: extrapolating unique counts to the whole of the data is **very hard**

---

![bg left:35%](img/hash_browns.jpeg)

## Preaggregation

Pass through the data daily and save aggregations across most common access patterns, eg: geolocation, pixel, device.

* Counting total events is straightforward, as it is an additive operation

* Estimating unique users is not additive; this is known as **the hotel problem**

---

## Data Sketches

This is a tool that allows for good estimations of unique counts. 

* When pre-aggregating data we look at hashes of user ids. This is a **binary fingerprint** of the user id. Counting distinct users is the same as counting distinct hashes.
* For each data partition, we store a **sketch**: a small amount of information related to the hashes of the users we've seen in that partition.
* The sketch is computed in such a way that enough information is retained to allow good uniques count estimations.

---

![bg left:30% width:350](img/compression.jpg)

### An analogy

A sketch works similarly to a **compression with loss**.

* We need much less space to store it in lieu of the list of user ids
* We cannot recover the original information
* We are still capable of doing some computations on it.

---

### Some properties of Sketches

* A sketching algorithm must describe how to **compute the sketch** from the given data.
* It must provide a way to **estimate uniques** from a given sketch.
* Given two sketches, it must provide a way to **merge** them into a new sketch.

* Some sketches can compute the **intersection** of two sketches
* Some sketches can compute the **set difference** of two sketches
* There are more sophisticated sketches designed to find most common items, estimation of percentiles...

---

### A few sketching algorithms

* **HyperLogLog**, for counting uniques. Available on Databricks as `approx_count_distinct`.
* **MinHash**, can also estimate intersections. Currently in use.
* **Theta Sketch** can estimate intersections & set differences. Under R&D.

---

# Work we've done with sketches

* Making sketching algorithms available in Databricks.

* Preaggregation of most frequent data available as a `production_metastore` table.
    * `events_preaggregated_minhashes_scala`
    * `domain_urls_preaggregated_minhashes_scala`
    * `segments_preaggregated_minhashes_scala`

* Providing methods to allow reporting users to further aggregate sketches.

---

![bg right:60% width:700](img/excel.jpeg)

# Thanks!
