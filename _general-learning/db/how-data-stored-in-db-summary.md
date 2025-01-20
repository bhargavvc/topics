# Database Storage Types and Implementations - Quick Reference

## Quick Navigation
1. [Storage Models](#storage-models)
2. [Physical Storage](#physical-storage)
3. [Index Types](#index-types)
4. [Buffer Management](#buffer-management)
5. [Transaction Types](#transaction-types)
6. [Compression Methods](#compression-methods)
7. [Partitioning Approaches](#partitioning-approaches)
8. [Storage Engines](#storage-engines)
9. [Data Integrity](#data-integrity)
10. [Backup Types](#backup-types)
11. [Real-World Examples](#real-world-examples)
12. [Performance Metrics](#performance-metrics)

## Storage Models
| Type | Structure | Best For | Real Example |
|------|-----------|----------|--------------|
| Row | Records together | OLTP | MySQL@Facebook |
| Column | Columns together | OLAP | Vertica@Uber |
| Document | JSON/BSON | Flexible data | MongoDB@Cisco |
| Key-Value | Simple pairs | Fast access | Redis@Twitter |
| Graph | Nodes/Edges | Relationships | Neo4j@LinkedIn |

[Back to Top](#quick-navigation)

## Physical Storage
| Component | Traditional | Modern | Cloud |
|-----------|-------------|---------|--------|
| Page Size | 8KB fixed | Variable | Dynamic |
| Files | Fixed size | Extensible | Object store |
| Memory | Buffer pool | Smart cache | Distributed |
| Recovery | Hours | Minutes | Seconds |
| Scale | TB range | PB range | Unlimited |

[Back to Top](#quick-navigation)

## Index Types
| Type | Speed | Use Case | Example |
|------|--------|----------|---------|
| B-Tree | Log(n) | General | MySQL Primary |
| Hash | O(1) | Exact match | Redis Keys |
| Bitmap | Fast scan | Low cardinality | Oracle DW |
| Spatial | Range | Geo data | PostGIS Maps |
| Full-text | Variable | Search | Elasticsearch |

[Back to Top](#quick-navigation)

## Buffer Management
| Feature | Classic | Modern | Cloud |
|---------|---------|---------|--------|
| Cache | Fixed RAM | ML-based | Auto-scale |
| Policy | LRU | Adaptive | Predictive |
| Size | Static | Dynamic | Elastic |
| Sync | Immediate | Lazy | Eventual |
| Hit Ratio | 80-90% | 95%+ | 99%+ |

[Back to Top](#quick-navigation)

## Transaction Types
| Type | Consistency | Speed | Usage |
|------|-------------|-------|--------|
| ACID | Strong | Slower | Banking |
| BASE | Eventual | Fast | Social |
| NewSQL | Mixed | Balanced | E-commerce |
| Distributed | Variable | Network | Cloud apps |
| Saga | Eventual | Complex | Microservices |

[Back to Top](#quick-navigation)

## Compression Methods
| Method | Ratio | CPU Cost | Best For |
|--------|--------|-----------|-----------|
| Dict | 2-3x | Low | Text |
| RLE | 10x+ | Very low | Sequences |
| Delta | 5x | Low | Time series |
| LZ4 | 3-5x | Medium | General |
| Zstd | 5x+ | High | Backups |

[Back to Top](#quick-navigation)

## Partitioning Approaches
| Type | Scale | Complex | Use Case |
|------|--------|----------|----------|
| Range | TB | Low | Dates |
| Hash | PB | Medium | Users |
| List | TB | Low | Categories |
| Geo | PB | High | Location |
| Hybrid | PB+ | Very high | Enterprise |

[Back to Top](#quick-navigation)

## Storage Engines
| Engine | Speed | Features | Usage |
|--------|--------|----------|--------|
| InnoDB | High | ACID | OLTP |
| RocksDB | Very high | LSM | Write-heavy |
| WiredTiger | High | Compress | MongoDB |
| Memory | Extreme | Volatile | Cache |
| MyRocks | Very high | Space | Social |

[Back to Top](#quick-navigation)

## Data Integrity
| Method | Level | Impact | Use Case |
|--------|--------|---------|----------|
| Checksum | Basic | Low | Transport |
| RAID | Medium | Medium | Storage |
| MVCC | High | Medium | Consistency |
| Encrypt | Highest | High | Security |
| Audit | Complete | Medium | Compliance |

[Back to Top](#quick-navigation)

## Backup Types
| Type | Speed | Size | Recovery |
|------|--------|------|----------|
| Full | Slow | 100% | Simple |
| Incr | Fast | 10% | Complex |
| Snap | Instant | CoW | Fast |
| Replica | Real-time | 100% | Instant |
| Cloud | Variable | Dedupe | Flexible |

[Back to Top](#quick-navigation)

## Real-World Examples
| Company | DB Type | Scale | Usage |
|---------|----------|-------|--------|
| Facebook | MySQL+RocksDB | PB+ | Social |
| Google | Spanner | Global | Cloud |
| Netflix | Cassandra | Global | Streaming |
| LinkedIn | Espresso | PB | Social |
| Uber | MySQL+Vertica | PB | Transport |

[Back to Top](#quick-navigation)

## Performance Metrics
| Aspect | OLTP | OLAP | NoSQL |
|--------|------|------|--------|
| TPS | 100K+ | 100s | 1M+ |
| Latency | ms | sec | μs |
| Data Size | TB | PB | PB+ |
| QPS | 1M+ | 100s | 10M+ |
| Scale | Vertical | Horizontal | Any |

[Back to Top](#quick-navigation)
